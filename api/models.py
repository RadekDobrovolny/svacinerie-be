from django.db import models

class IngredientType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class IngredientVariant(models.Model):
    type = models.ForeignKey(
        IngredientType,
        on_delete=models.CASCADE,
        related_name="variants"
    )
    name = models.CharField(max_length=100)
    is_default = models.BooleanField(default=False)

    class Meta:
        unique_together = ("type", "name")

    def __str__(self):
        return f"{self.type.name} – {self.name}"


class Stock(models.Model):
    variant = models.ForeignKey(
        IngredientVariant,
        on_delete=models.CASCADE,
        related_name="stock_items"
    )
    quantity = models.PositiveIntegerField()

    class Meta:
        unique_together = ("variant",)


class Recipe(models.Model):
    name = models.CharField("recipe name", max_length=100, unique=True)
    ingredients = models.ManyToManyField(
        IngredientType,
        through="RecipeIngredient",
        related_name="recipes"
    )

    class Meta:
        verbose_name = "recipe"
        verbose_name_plural = "recipes"

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="recipe_ingredients"
    )
    ingredient_type = models.ForeignKey(
        IngredientType,
        on_delete=models.CASCADE,
        related_name="ingredient_in_recipes"
    )
    quantity = models.PositiveIntegerField()

    class Meta:
        verbose_name = "recipe ingredient"
        verbose_name_plural = "recipe ingredients"
        unique_together = ("recipe", "ingredient_type")


class Order(models.Model):
    STATUS_CHOICES = [
        ("received", "Přijatá"),
        ("completed", "Dokončená"),
        ("cancelled", "Stornovaná"),
    ]
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="received")

    def __str__(self):
        return f"Objednávka {self.id} ({self.get_status_display()})"


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="items"
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="order_items"
    )
    variants = models.JSONField()

    def __str__(self):
        return f"{self.recipe.name} v objednávce {self.order.id}"


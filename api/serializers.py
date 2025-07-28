from django.db.models import Sum
from rest_framework import serializers
from .models import IngredientVariant, IngredientType, Recipe, RecipeIngredient, Stock

'''
class StockSerializer(serializers.ModelSerializer):
    # Read nested ingredient details, write via ingredient_id
    ingredient = IngredientSerializer(read_only=True)
    ingredient_id = serializers.PrimaryKeyRelatedField(
        queryset=Ingredient.objects.all(), source='ingredient', write_only=True
    )

    class Meta:
        model = Stock
        fields = ['id', 'ingredient', 'ingredient_id', 'quantity']
'''


class IngredientVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = IngredientVariant
        fields = ['id', 'name', 'is_default']


class IngredientTypeSerializer(serializers.ModelSerializer):
    variants = IngredientVariantSerializer(many=True)

    class Meta:
        model = IngredientType
        fields = ['id', 'name', 'variants']


class RecipeIngredientSerializer(serializers.ModelSerializer):
    ingredient_type = IngredientTypeSerializer(read_only=True)
    ingredient_type_id = serializers.PrimaryKeyRelatedField(
        queryset=IngredientType.objects.all(),
        source='ingredient_type',
        write_only=True
    )

    class Meta:
        model = RecipeIngredient
        fields = ['id', 'ingredient_type', 'ingredient_type_id', 'quantity']



class RecipeSerializer(serializers.ModelSerializer):
    recipe_ingredients = RecipeIngredientSerializer(many=True)
    preparable = serializers.SerializerMethodField()

    class Meta:
        model = Recipe
        fields = ['id', 'name', 'recipe_ingredients', 'preparable']

    @staticmethod
    def get_preparable(recipe):
        for ri in recipe.recipe_ingredients.all():
            total_stock = (Stock.objects
                .filter(variant__type=ri.ingredient_type)
                .aggregate(total=Sum('quantity'))
                .get('total') or 0)
            if total_stock < ri.quantity:
                return False
        return True

    def create(self, validated_data):
        ingredients_data = validated_data.pop('recipe_ingredients')
        recipe = Recipe.objects.create(**validated_data)
        for item in ingredients_data:
            RecipeIngredient.objects.create(recipe=recipe, **item)
        return recipe

    def update(self, instance, validated_data):
        ingredients_data = validated_data.pop('recipe_ingredients')
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        # Replace all recipe ingredients
        instance.recipe_ingredients.all().delete()
        for item in ingredients_data:
            RecipeIngredient.objects.create(recipe=instance, **item)
        return instance


class OrderItemSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    variants = serializers.JSONField()


class OrderCreateSerializer(serializers.Serializer):
    items = OrderItemSerializer(many=True)

from django.contrib import admin
from .models import (
    IngredientType,
    IngredientVariant,
    Stock,
    Recipe,
    RecipeIngredient,
    Order,
    OrderItem
)


class IngredientVariantInline(admin.TabularInline):
    model = IngredientVariant
    extra = 1


@admin.register(IngredientType)
class IngredientTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [IngredientVariantInline]


@admin.register(IngredientVariant)
class IngredientVariantAdmin(admin.ModelAdmin):
    list_display = ('type', 'name', 'is_default')


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('variant', 'quantity')


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [RecipeIngredientInline]


@admin.register(RecipeIngredient)
class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'ingredient_type', 'quantity')


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'status')
    inlines = [OrderItemInline]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'recipe', 'variants')

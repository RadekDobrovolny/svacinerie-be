from django.urls import path
from .views import RecipeList, OrderCreateView

urlpatterns = [
    path(
        'recipes/',
        RecipeList.as_view(),
        name='recipe-list'
    ),
    path("order-create/",
         OrderCreateView.as_view(),
         name="order-create"
    ),
]

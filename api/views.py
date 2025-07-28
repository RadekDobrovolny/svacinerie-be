from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import IngredientType, Stock, Recipe, Order, OrderItem
from .serializers import RecipeSerializer, OrderCreateSerializer


class RecipeList(generics.ListAPIView):
    """
    List all recipes with a 'preparable' flag.
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class OrderCreateView(APIView):
    def post(self, request):
        serializer = OrderCreateSerializer(data={"items": request.data})
        serializer.is_valid(raise_exception=True)
        order = Order.objects.create()
        for item in serializer.validated_data["items"]:
            recipe = Recipe.objects.get(id=item["id"])
            OrderItem.objects.create(
                order=order,
                recipe=recipe,
                variants=item["variants"]
            )
        return Response({"order_id": order.id}, status=status.HTTP_201_CREATED)
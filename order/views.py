from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer



class OrderViewSet(ModelViewSet):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer
	permission_classes = [IsAuthenticated]

	def get_queryset(self):
		return self.queryset.filter(user=self.request.user)

	@action(["GET"], detail=True)
	def pay(self, request, pk):
		order: Order = self.get_object()
		# order = get_object_or_404(Order, id=pk)
		if order.is_paid:
			return Response("already paid", status=400)
		if order.user.billing.withdraw(order.total_price):
			order.is_paid = True
			order.save()
			return Response("Заказ оплачен", status=200)
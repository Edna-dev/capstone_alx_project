from rest_framework import generics, permissions
from .models import Budget, Expense
from .serializers import BudgetSerializer, ExpenseSerializer

# 💰 Budget Views
class BudgetListCreateView(generics.ListCreateAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
    permission_classes = [permissions.IsAuthenticated]  # Require login

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # Automatically assign logged-in user


class BudgetDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
    permission_classes = [permissions.IsAuthenticated]


class ExpenseListCreateView(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    # permission_classes = [permissions.IsAuthenticated]  # enable later
    def perform_create(self, serializer):
        serializer.save()


class ExpenseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated]

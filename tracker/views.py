from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Budget, Expense
from .serializers import BudgetSerializer, ExpenseSerializer


class BudgetListCreateView(generics.ListCreateAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
    permission_classes = [AllowAny]


class BudgetDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
    permission_classes = [AllowAny]


class ExpenseListCreateView(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [AllowAny]


class ExpenseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [AllowAny]


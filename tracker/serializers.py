from rest_framework import serializers
from .models import Budget, Expense

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = '__all__'
        read_only_fields = ['user']


class ExpenseSerializer(serializers.ModelSerializer):
    # Accept PrimaryKey for writing, and return budget_name for reading
    budget = serializers.PrimaryKeyRelatedField(queryset=Budget.objects.all())
    budget_name = serializers.CharField(source='budget.name', read_only=True)

    class Meta:
        model = Expense
        fields = ['id', 'budget', 'budget_name', 'category', 'amount', 'description', 'date']

    def create(self, validated_data):
        # If budget was passed as string (e.g. '1'), PrimaryKeyRelatedField normally handles it,
        # but we add a safe fallback to convert string -> int -> Budget instance
        budget_value = validated_data.get('budget')
        if isinstance(budget_value, str):
            try:
                validated_data['budget'] = Budget.objects.get(pk=int(budget_value))
            except (ValueError, Budget.DoesNotExist):
                raise serializers.ValidationError({"budget": "Invalid budget id."})
        return super().create(validated_data)

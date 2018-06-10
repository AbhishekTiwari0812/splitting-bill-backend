from rest_framework import serializers

from .models import User, Group, Expense


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        # Each room only has one event per day.
        model = User
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        # Each room only has one event per day.
        model = Group
        fields = '__all__'


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        # Each room only has one event per day.
        model = Expense
        fields = '__all__'

# TODO: Add for other models

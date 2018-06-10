from rest_framework.viewsets import ModelViewSet

from .serializers import UserSerializer, GroupSerializer, ExpenseSerializer
from .models import User, Expense, Group


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class ExpenseViewSet(ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

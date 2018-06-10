from django.urls import path
from rest_framework.routers import SimpleRouter

from .viewset import UserViewSet, GroupViewSet, ExpenseViewSet
from . import views

router = SimpleRouter()
router.register("user", UserViewSet)
router.register("group", GroupViewSet)
router.register("expense", ExpenseViewSet)

urlpatterns = [
    path('health', views.health),
    path('friendids', views.get_friend_ids),
    path('users/(?P<user_id>\d+)/addcontact', views.add_friend_to_network)
]

urlpatterns += router.urls

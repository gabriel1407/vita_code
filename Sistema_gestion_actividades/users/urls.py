from django.urls import re_path
from rest_framework.routers import DefaultRouter


from users.views import UserCustomerViewSet

router = DefaultRouter()
router.register(r'users', UserCustomerViewSet)

urlpatterns = [
    #re_path(r'^task/<int:pk>/', TaskViewSet, name='login'),
    #re_path(r'^dashboard_manager/', DashboardUserViewSet.as_view(), name='dashboard_manager'),

]

urlpatterns += router.urls
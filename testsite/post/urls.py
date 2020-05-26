from django.urls import path, include
# from rest_framework import routers
from . import views

# routers = routers.DefaultRouter()
# routers.register('developer_endpoint', views.DeveloperView)  # auto generate endpoint

urlpatterns = [
    path('', views.post_all, name='post_all'),
    path('<int:pk>', views.post_detail, name='post_detail'),
    # path('api/', include(routers.urls)),
]

from django.conf.urls import url
from rest_framework import routers
from .views import userViewSet

from . import views

'''urlpatterns = [
	
	url(r'^list$', views.index, name='custom'),
 
]'''


router = routers.DefaultRouter()

router.register(r'users', userViewSet)

urlpatterns = router.urls

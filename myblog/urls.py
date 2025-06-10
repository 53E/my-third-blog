from django.conf.urls import url, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Post', views.IntruderImage)

urlpatterns = [
    url(r'^, views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/, views.post_detail, name='post_detail'),
    url(r'^post/new/, views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/, views.post_edit, name='post_edit'),
    url(r'^api_root/', include(router.urls)),
]
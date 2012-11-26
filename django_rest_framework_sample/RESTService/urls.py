from django.conf.urls import patterns, include, url
from RESTService.views import RestaurantList, RestaurantDetail
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns("",
                       url(r'^restaurants/$', RestaurantList.as_view(), name='restaurant-list'),
                       url(r'^restaurants/(?P<pk>\d+)/$', RestaurantDetail.as_view(), name='restaurant-detail'),
)

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])

urlpatterns += patterns('',
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
from django.conf.urls import url

from market.apps.social.views import (UserProfileCreateView,
                                      UserProfileDetailView,
                                      UserProfileListView,
                                      UserProfileUpdateView)


app_name = 'social'
urlpatterns = [
    url(r'^$', UserProfileListView.as_view(), name='list'),
    url(r'^new/$', UserProfileCreateView.as_view(), name='create'),
    url(r'^(?P<slug>[-\w]+)/edit/$', UserProfileUpdateView.as_view(), name='update'),
    url(r'^(?P<slug>\w+)/$', UserProfileDetailView.as_view(), name='detail'),
]

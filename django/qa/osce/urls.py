from django.conf.urls import url
from . import views

urlpatterns = [
#	url(r'^$', views.osce, name='osce'),
	url(r'^(?P<stn>[0-9]+)/$', views.osce, name='osce'),
#	url(r'^(?P<chpt>[0-9]+)/(?P<qnum>[0-9]+)/$', views.check_card, name='check_card'),
#	url(r'^(?P<chpt>[0-9]+)/(?P<qtext>.+)/$', views.check_card_text, name='check_card_text'),
]

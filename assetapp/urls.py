from django.urls import re_path, path
from . import views

urlpatterns = [
	re_path(r'^$', views.index, name='index'),
	re_path(r'^members/$', views.members, name='members'),
	re_path(r'^members/(?P<id>[0-9]+)$', views.membersdetails, name='members'),
	re_path(r'^members/membersupdate/([0-9]+)$', views.membersupdate, name='membersupdate'),
	re_path(r'^members/membersdelete/([0-9]+)$', views.membersdelete, name='membersdelete'),
	re_path(r'^addmembers/$', views.addmembers, name='addmembers'),
	re_path(r'^assets/$', views.assets, name='assets'),
	re_path(r'^assets/(?P<id>[0-9]+)$', views.assetsdetails, name='assets'),
	re_path(r'^assets/assetupdate/([0-9]+)$', views.assetupdate,name='assetupdate'),
	re_path(r'^assets/assetdelete/([0-9]+)$', views.assetdelete,name='assetdelete'),
	re_path(r'^addasset/$', views.addasset, name='addasset'),
	re_path(r'^distribution/$', views.distribution, name='distribution'),
	re_path(r'^show_distribution/distributionupdate/(?P<id>[0-9]+)$', views.distributionupdate, name='distributionupdate'),
	re_path(r'^show_distribution/distributiondelete/(?P<id>[0-9]+)$', views.distributiondelete, name='distributiondelete'),
	re_path(r'^show_distribution/$', views.index, name='show_distribution'),
]
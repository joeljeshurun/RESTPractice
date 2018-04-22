from django.conf.urls import url
from students import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^students/$', views.StudentList.as_view()),
    url(r'^students/(?P<pk>[0-9]+)/$', views.StudentDetail.as_view()),
]

urlpatterns=format_suffix_patterns(urlpatterns)
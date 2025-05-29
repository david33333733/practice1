from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path("polls/", include("polls.urls")),  # polls 앱의 URL 연결
    path("apage/", include("apage.urls")),
    path("bpage/", include("bpage.urls")),
    path("cpage/", include("cpage.urls")),
    path("introducepage/", include("introducepage.urls")),
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
]

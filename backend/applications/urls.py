from django.urls import path

from applications.views import ApplicationCreateView, QueueCreateView

urlpatterns = [
    path("applications/", ApplicationCreateView.as_view()),
    path("queues/", QueueCreateView.as_view()),
]

from django.urls import path

from .views import (
    TaskListView,
    TaskDetailView,
    TagListView,
    TaskCreateView,
    TagCreateView
)


urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    # path("/tags/update/", TagUpdateView, name="tag-update")
]

app_name = "tasks"

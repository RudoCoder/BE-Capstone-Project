from django.urls import path
from .views import MyApplicationsList, ApplicationCreate, ManageApplicationsList

urlpatterns = [
    path("applications/", MyApplicationsList.as_view(), name="my_applications"),
    path("applications/create/", ApplicationCreate.as_view(), name="create_application"),
    path("applications/manage/", ManageApplicationsList.as_view(), name="manage_applications"),
]

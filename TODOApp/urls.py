from django.urls import path
from .views import *

urlpatterns = [
    path('create-item', TodoItemCreate.as_view(), name='create-item'),
    path('read-item/<int:pk>', TodoItemRead.as_view(), name='read-item'),
    path('list-items', TodoItemListAll.as_view(), name='list-items'),
    path('update-item/<int:pk>', TodoItemUpdate.as_view(), name='update-item'),
    path('delete-item/<int:pk>', TodoItemDelete.as_view(), name='delete-item')
]
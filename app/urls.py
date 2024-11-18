from django.urls import path
from .views import index, index_item, add_item

app_name = 'app'

urlpatterns = [
    path('', index, name='index'),
    path('<int:id>/', index_item, name='detail'),
    path('add/', add_item, name='add'),
]

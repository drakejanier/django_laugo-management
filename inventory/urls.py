from django.conf.urls import url
from .views import *


urlpatterns = [

    url(r'^$', index, name='index'),
    url(r'^inventory$', inventory, name='inventory'),

    url(r'^display_items$', display_items, name='display_items'),
    url(r'^add_Item$', add_Item, name='add_Item'),
    url(r'^edit_inventory/(?P<pk>\d+)$', edit_inventory, name='edit_inventory'),

]
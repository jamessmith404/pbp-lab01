# from lab01
from django.urls import path 
from wishlist.views import show_wishlist, show_wishlist_xml, show_wishlist_json #sesuaikan dengan nama fungsi yang dibuat
from wishlist.views import show_json_by_id #sesuaikan dengan nama fungsi yang dibuat
from wishlist.views import register #sesuaikan dengan nama fungsi yang dibuat || Week 03
from wishlist.views import login_user #sesuaikan dengan nama fungsi yang dibuat
from wishlist.views import logout_user #sesuaikan dengan nama fungsi yang dibuat



app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', show_wishlist_xml, name="show_wishlist_xml"), #sesuaikan dengan nama fungsi yang dibuat
    path('json/', show_wishlist_json, name="show_wishlist_json"), #sesuaikan dengan nama fungsi yang dibuat
    path('json/<int:id>', show_json_by_id, name="show_json_by_id"), #sesuaikan dengan nama fungsi yang dibuat
    path('register/', register, name='register'), #sesuaikan dengan nama fungsi yang dibuat || WEEK 03
    path('login/', login_user, name='login'), #sesuaikan dengan nama fungsi yang dibuat
    path('logout/', logout_user, name='logout'), #sesuaikan dengan nama fungsi yang dibuat
]
from django.urls import path
from .views import ( userList, userDetail, removeBodyPart, clickMatrix)


urlpatterns = [
    #path('', Home, name = 'home_api'),
    path('click/<str:matrix>', clickMatrix, name = 'click_matrix'),
    path('remove-part/<str:partbody>', removeBodyPart, name = 'remove_part'),
    path('user-list/', userList, name = 'user_list'),
    path('user-detail/<int:pk>', userDetail, name = 'user_detail'),
]
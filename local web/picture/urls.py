from django.urls import path
from picture.views import login, index, upload_image,image_list,delete_img,edit_tag

urlpatterns = [
    path('login/', login, name="login"),
    path('index/', index, name="index"),
    path('upload_image/', upload_image, name="upload_image"),
    path('image_list/',image_list,name="image_list"),
    path('delete_img/',delete_img,name="delete_img"),
    path('edit_tag/',edit_tag,name="edit_tag")
]

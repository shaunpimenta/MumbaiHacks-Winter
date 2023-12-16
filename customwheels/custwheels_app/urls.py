from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("select_model/", views.select_model, name="select_model"),

    path('chat/', views.chat_view, name='chat_view'),


    path("customemodel", views.customemodel, name="customemodel"),

    # path("test", views.test, name="test"),
    # path("help", views.help, name="help"),

    path('user_login/',      views.user_login,     name='user_login'),
    path('user_logout/',     views.user_logout,    name='user_logout'),
    path('user_register/',   views.user_register,  name='user_register'),


    # path("business", views.business, name="Business"),
    # path("about/", views.about, name="AboutUs"),
    # path("contact/", views.contact, name="ContactUs"),
    # path("products/<int:myid>", views.productView, name="ProductView"),
    # path("products/<str:myslug>", views.productView, name="ProductView"),

]
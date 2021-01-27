from django.urls import path
from . import views

app_name='drishya'
urlpatterns=[path('',views.index,name="index"),
             path('login/',views.login,name="login"),
             path('login/register',views.register,name="register"),
             path('login/allposts',views.allposts,name="allposts"),
             path('login/myposts/<int:pk>/',views.myposts,name="myposts"),
             path('login/addposts',views.addposts,name="addposts"),
             path('login/payment/<int:pk>/',views.payment,name="payment"),
             path('login/afterpayment/<int:pk>/',views.afterpayment,name="afterpayment"),
             path('login/like',views.like, name="like"),
             path('login/dislike',views.dislike, name="dislike"),
             path('login/logout',views.logout,name="logout"),
             path('login/mine',views.mine,name="mine"),
             path('login/payment/<int:pk>/afterpayment',views.afterpayment,name="afterpayment"),
             path('login/payment/<int:pk>/payment',views.payment,name="payment"),
             path('login/payment/<int:pk>/newallposts',views.newallposts,name="newallposts"),
             path('login/myposts/<int:pk>/newallposts',views.newallposts,name="newallposts"),
             path('login/myposts/<int:pk>/newlogout',views.newlogout,name="newlogout"),
             path('login/addwallet',views.addwallet,name="addwallet"),
             path('login/myposts/<int:pk>/newaddwallet',views.newaddwallet,name="newaddwallet"),
             path('login/getwallet',views.getwallet,name="getwallet"),
             path('login/myposts/<int:pk>/newgetwallet',views.newgetwallet,name="newgetwallet"),
             path('login/payment/<int:pk>/newaddwallet',views.newaddwallet,name="newaddwallet"),
             path('login/payment/<int:pk>/newgetwallet',views.newgetwallet,name="newgetwallet"),
            ]

from django.urls import path
from . import views
urlpatterns=[path("",views.index,name="index"),
             path("html/",views.index2,name="index2"),
             path("model/",views.index3,name="index3"),
             path("model1/",views.index4,name="index4"),
             path("model1/add/",views.add,name="add"),
             path("model1/add/addrecord/",views.addrecord,name="addrecord"),
             path("model1/delete/<int:id>",views.delete,name="del"),
             path("model1/update/<int:id>",views.update,name="update"),
             path("model1/update/updaterecord/<int:id>",views.updaterecord,name="del")]
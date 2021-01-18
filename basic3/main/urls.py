
from django.urls import path
from main import views
from main.models import ProductModel
urlpatterns = [
    path('index/',views.greet),
    path('table/',views.table),
    path('pro/<int:id>/',views.product),
    # path('form/',views.form),
    path('create/',views.create),
     path('create/hai/',views.hai)
]
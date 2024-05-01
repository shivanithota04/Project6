from django.urls import path
from . import views  # Assuming views.py is in the same directory as urls.py

app_name = 'MIMEapp'

urlpatterns = [
    path('html', views.htmlview.as_view(), name='htmlview'),
    path('excel', views.excelview.as_view(), name='excelview'),
    path('xml', views.xmlview.as_view(), name='xmlview')
]
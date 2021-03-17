from django.contrib import admin
from django.urls import path
from blog.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('create_user/', create_contact),
    path('contact/<id>/', contact_details, name = 'contact_details'),
    path('update_contact/<contact_id>/', update_contact, name='update_contact'),
    path('delete_contact/<contact_id>/', delete_contact, name='delete_contact')
]

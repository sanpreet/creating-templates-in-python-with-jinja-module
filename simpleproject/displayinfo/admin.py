from django.contrib import admin
# this is the model/table and is imported here.
from .models import PersonInfo

# Register your models here.
# this model/table/class is registed here so that one can see it in the admin panel
# One can login to the admin panel by visiting the url as http://127.0.0.1:8000/admin/
# one need to create the super user by issuing the below command
# python manage.py create superuser
admin.site.register(PersonInfo)
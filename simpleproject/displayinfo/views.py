from django.shortcuts import render
# by adding . it means on the same directory
from .models import PersonInfo

# Create your views here.
def index(request):
        # Getting all the posts from database
        # i have saved the objects using the python manage.py shell
        personinfo = PersonInfo.objects.all()  
        # returing the objects in the web by passing objects as dictionary to an html template
        return render(request, 'information.html', { 'personinfo': personinfo })

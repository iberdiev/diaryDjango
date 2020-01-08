import os, django, requests
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "diary.settings")
django.setup()
from main_api import models


##############################
#Registering all availabe schools

# URL = "http://127.0.0.1:8080/api/v1/rest-auth/registration/"
# schools = models.JkitepSchools.objects.all()
# for school in schools:
#    data = {"username":str(school.schoolsid),
#            "password1":str(school.schoolsid),
#            "password2":str(school.schoolsid),
#            "school_id":school.schoolsid}
#    requests.post(url = URL, data = data)

##############################

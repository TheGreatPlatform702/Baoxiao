from django.contrib import admin
from registration.models  import *

RegisterClass = (
    Administrator,
    CommonUser,
)

for item in RegisterClass:
    admin.site.register(item)
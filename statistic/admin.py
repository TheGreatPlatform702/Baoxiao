from django.contrib import admin
from statistic.models  import *

RegisterClass = (
    DetailMoney,
    BaoXiaoTable,
)
for item in RegisterClass:
    admin.site.register(item)
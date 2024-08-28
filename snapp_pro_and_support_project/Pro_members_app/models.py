from django.db import models
from django.http import HttpResponse, JsonResponse


class Pro_members(models.Model, Snapp_users):
    is_pro_options = [
        ('T', )
    ]
    is_pro
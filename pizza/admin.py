from django.contrib import admin
from pizza import models
# Register your models here.
admin.site.register([
    models.Size,
    models.Pizza
])

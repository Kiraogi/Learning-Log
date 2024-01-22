from django.contrib import admin
from .models import Topic, Entry

# Зарегистрируйте вашу модель здесь
admin.site.register(Topic)
admin.site.register(Entry)

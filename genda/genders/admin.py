from django.contrib import admin

# Register your models here.


from .models import Pronoun, Gender

admin.site.register(Pronoun)
admin.site.register(Gender)

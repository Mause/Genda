from django.contrib import admin

# Register your models here.


from .models import Pronoun, Gender, UserToPronoun

admin.site.register(Pronoun)
admin.site.register(Gender)
admin.site.register(UserToPronoun)

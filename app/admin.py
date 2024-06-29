from django.contrib import admin
from app.models import Men, About_me, Skills, ContactInfo, AvatarImage

# Register your models here.

admin.site.register(Men)
admin.site.register(About_me)
admin.site.register(Skills)
admin.site.register(ContactInfo)
admin.site.register(AvatarImage)
from django.shortcuts import render

from app.models import Men, ContactInfo, About_me, Skills, AvatarImage

# Create your views here.


def resume_views(request):
    men = Men.objects.all()
    contactinfo = ContactInfo.objects.all()
    about = About_me.objects.all()
    skills = Skills.objects.all()
    avatar = AvatarImage.objects.all()

    context = {'men': men,
               'contactinfo': contactinfo,
               'about': about,
               'skills': skills,
               'avatar': avatar,
               }
    return render(request, 'index.html', context)


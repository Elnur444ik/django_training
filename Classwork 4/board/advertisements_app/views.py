from django.shortcuts import render
from advertisements_app.models import Advertisement


def advertisements_list(request, *args, **kwargs):
    advertisements = Advertisement.objects.all()
    return render(request, 'advertisements_app/advertisements.html', {
        'advertisements': advertisements
    })

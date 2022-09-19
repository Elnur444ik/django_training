from django.shortcuts import render


# Create your views here.

def advertisement_list(request, *args, **kwargs):
    return render(request, 'advertisement/advertisement_list.html', {})


def advertisement_details(request, *args, **kwargs):
    return render(request, 'advertisement/advertisement_details.html', {})




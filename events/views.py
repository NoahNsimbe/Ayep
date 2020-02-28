from django.shortcuts import render

# from .models import Image


def index(request):
    # images = Image.objects()
    eventspage = 'active'
    navigation = True
    # join = True
    context = {
        'eventspage': eventspage,
        'navigation': navigation,
        # 'images': images,
        # 'join': join,
    }
    return render(request, 'events/index.html', context)
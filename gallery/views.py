from django.shortcuts import render
from events.models import Event
# from .models import Image


def index(request):
    # images = Image.objects()
    navigation = True
    gallerypage = 'active'
    nos = 4
    join = True
    recent_events = Event.objects.all()
    context = {
        'gallerypage': gallerypage,
        # 'images': images,
        'join': join,
        'navigation': navigation,
        'recent_events': recent_events,
        'nos': nos,
    }
    return render(request, 'gallery/index.html', context)

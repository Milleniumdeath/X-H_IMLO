from django.shortcuts import render
from .models import *



def index_view(request):

    togri = None
    notogrilar = None
    message = None
    soz = request.GET.get('soz')
    if soz is not None:
        soz = soz.lower()
        togrilar = Togri.objects.filter(soz=soz)
        if togrilar.exists():
            togri = togrilar.first()
            notogrilar = togri.notogri_set.all()
        else:
            notogrilar = Notogri.objects.filter(soz=soz)
            if notogrilar.exists():
                notogri = notogrilar.first()
                togri = notogri.togri
                notogrilar = togri.notogri_set.all()
            else:
                if 'x' not in soz and 'h' not in soz:
                    message = "So'z tarkibida 'x' yoki 'h' harfi mavjud emas❗"
                else:
                    message = "So'z omborda mavjud emas❗"

    context = {
        'togri': togri,
        'notogrilar': notogrilar,
        'message' : message,
        'soz': soz,
    }
    return render(request, 'index.html', context)

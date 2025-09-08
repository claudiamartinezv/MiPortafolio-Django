from django.shortcuts import render
from .models import Nav, SobreMi, Hobbie, Footer

def index(request):
    context = {
        "nav_items": Nav.objects.all(),
        "sobre_mi": SobreMi.objects.all(),  
        "hobbies": Hobbie.objects.all(),
        "footer": Footer.objects.first()  # mejor usar .first(), porque normalmente solo hay un footer
    }
    return render(request, "portafolio/index.html", context)

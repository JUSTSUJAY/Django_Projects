from django.shortcuts import render
from django.http import HttpResponse
from translate import Translator
# Create your views here.
def home(request):
    if request.method == "POST":
        ip_text = request.POST['ip_text']
        into_lang = request.POST['into_lang']
        translator_instanct = Translator(to_lang = into_lang)
        translation = translator_instanct.translate(ip_text)
        return HttpResponse(f'<body style="background-color: #1a1a1a; color: #ffffff; font-size:3em">{translation}</body>')
    return render(request, 'home.html')

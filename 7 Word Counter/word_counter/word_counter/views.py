from django.shortcuts import render

def home(request):
    return render(request, 'website/index.html', {"on_frontend": "on_frontend"}) 
def counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render(request, 'website/counter.html', {"text":amount_of_words}) 

# def counter(request):
#     if request.method == 'POST':
#         text = request.POST['text']
#         return render(request, 'website/counter.html', {"text": len(text.split())})
#     else:
#         return render(request, 'website/counter.html', {"text": "Please submit the form first"})
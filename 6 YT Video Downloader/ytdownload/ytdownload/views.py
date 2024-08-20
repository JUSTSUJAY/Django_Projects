from django.shortcuts import render, redirect
from pytube import YouTube

def index(request):
    if request.method == "POST":
        link = request.POST.get('link')
        if link:
            try:
                video = YouTube(link)
                stream = video.streams.get_lowest_resolution()
                stream.download()
                return redirect("index")
            except Exception as e:
                # Handle any exceptions that might occur during video processing
                return render(request, "index.html", {"error": str(e)})
        else:
            # Handle case where 'link' is not provided in the POST data
            return render(request, "index.html", {"error": "Please provide a valid YouTube link"})
    return render(request, "index.html")
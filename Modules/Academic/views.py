from django.shortcuts import render

def contactForm(request):
    return render(request, "contact-form.html")

def contact(request):
    if request.method == "POST":
        pass    

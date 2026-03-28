from django.shortcuts import render

def page1(request):
    return render(request, 'sahifa1.html')

def page2(request):
    return render(request, 'sahifa2.html')

def page3(request):
    return render(request, 'sahifa3.html')

def page4(request):
    return render(request, 'sahifa4.html')

def page5(request):
    return render(request, 'sahifa5.html')
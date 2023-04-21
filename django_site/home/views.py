from django.shortcuts import render


def home(request):
    return render(request, 'home/home_page.html', {})


def reports(request):
    return render(request, 'home/reports.html', {})

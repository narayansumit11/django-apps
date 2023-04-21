from django.shortcuts import render


def home(request):
    return render(request, 'home/home_page.html', {})


def reports_sumit(request):
    return render(request, 'reports/sumit.html', {})

def reports_prem(request):
    return render(request, 'reports/prem.html', {})

def reports_chitralekha(request):
    return render(request, 'reports/chitralekha.html', {})

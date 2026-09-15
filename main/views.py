from django.shortcuts import render
# from django.http import HttpResponse

def home(request):
    return render(request, "home.html")
def batken(request):
    return render(request, "batken.html")
def osh(request):
    return render(request, "osh.html")
def jalal_abad(request):
    return render(request, "jalal-abad.html")
def naryn(request):
    return render(request, "naryn.html")
def ysyk_kol(request):
    return render(request, "ysyk-kol.html")
def talas(request):
    return render(request, "talas.html")
def chuy(request):
    return render(request, "chuy.html")

# районы

def b_rayon(request):
    return render(request, "regions/b_rayon.html")
def ch_rayon(request):
    return render(request, "regions/ch_rayon.html")
def ja_rayon(request):
    return render(request, "regions/ja_rayon.html")
def n_rayon(request):
    return render(request, "regions/n_rayon.html")
def o_rayon(request):
    return render(request, "regions/o_rayon.html")
def t_rayon(request):
    return render(request, "regions/t_rayon.html")
def yk_rayon(request):
    return render(request, "regions/yk_rayon.html")
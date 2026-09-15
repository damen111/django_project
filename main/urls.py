from .views import *
from django.urls import path

urlpatterns = [
    path('', home, name='home'),
    path('batken/', batken, name='batken'),
    path('chuy/', chuy, name='chuy'),
    path('osh/', osh, name='osh'),
    path('talas/', talas, name='talas'),
    path('ysyk-kol/', ysyk_kol, name='ysyk-kol'),
    path('jalal-abad/', jalal_abad, name='jalal-abad'),
    path('naryn/', naryn, name='naryn'),

    # районы
    path('batken/rayony/', b_rayon, name='b_rayon'),
    path('chuy/rayony/', ch_rayon, name='ch_rayon'),
    path('jalal-abad/rayony/', ja_rayon, name='ja_rayon'),
    path('naryn/rayony/', n_rayon, name='n_rayon'),
    path('osh/rayony/', o_rayon, name='o_rayon'),
    path('talas/rayony/', t_rayon, name='t_rayon'),
    path('ysyk-kol/rayony/', yk_rayon, name='yk_rayon'),
]
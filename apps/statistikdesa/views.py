from django.shortcuts import render

# Create your views here.
def statistik_penduduk(request):

    return render(request, 'statistik_desa.html')
from django.shortcuts import render

dados = {
    1:{"nome": "Catarata",},
    2:{"nome": "ceratocone",},
}
def index(request):
    return render(request, 'clinicaPV/index.html' )

def sobre(request):
    return render(request, 'clinicaPV/sobre.html')

def home(request):
    return render(request, 'clinicaPV/index.html')
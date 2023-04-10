from django.shortcuts import render


#funções de URL de link
def home(request):
    return render(request,"Home.html")

def tarefas(request):
    return render(request,"Tasks.html")

def include(request):
    return render(request,"index.html")
from django.http import JsonResponse


# Create your views here.

def usuarios(request):
    if request.method == 'GET':
        usuario = {'id': 1, 'nome': 'Thiago Macedo', 'apellido': 'Thiago'}
        return JsonResponse(usuario)

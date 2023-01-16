from django.shortcuts import render

import requests



def getAndPostData(request):
    if request.method == 'GET':
        return render(request, 'cep/pages/home.html')
    else:
        cep = request.POST.get('cep')
        endpoint = f'https://viacep.com.br/ws/{cep}/json/'
        requisicao = requests.get(endpoint).json()
        uf = requisicao['uf']
        localidade = requisicao['localidade']
        logradouro = requisicao['logradouro']
        arr = [cep, uf, localidade, logradouro]
        context = {
            'requisicao': arr,
        }
        return render(request, 'cep/pages/content.html', context=context)
        
def resultView(request):
    return render(request, 'cep/pages/content.html')
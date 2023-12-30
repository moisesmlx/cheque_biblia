'''
pip install werkzeug
pip install django_extensions

para rodar o site local

py manage.py runserver_plus --print-sql
'''
from django.shortcuts import render
import Cheque
from django.http import HttpResponse

def index(request):  
    return render(request, 'index.html')

def ver_pesquisa(request):
    try:
        palavra = request.POST.get('p')
        if palavra != '':
            Cheque.Cheque_Palavras(palavra)
            text_area = Cheque.checagem
            contidade_cap_verso = Cheque.contidade_cap_verso
            lista = {
                'p': palavra,
                'texto': text_area,
                'contia': contidade_cap_verso,
                'que_palavra': f'{palavra}'
            }
            return render(request, 'ver_pesquisa.html', lista)
        else:
            return HttpResponse('''<h1>
                                <center>Cheque se digitou uma palavra ou frase que tenha em nossa tradução; 
                                tente outras palavras com o mesmo significado!<br>
                                <a href="javascript: history.go(-1)">Voltar</a>
                                </center></h1>''')
    except:
        return render(request, 'ver_pesquisa.html', lista)

    

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
    palavra = request.POST.get('p')

    try:

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
            return HttpResponse(f'''<h1>
                                        <center>Não foi encontrada a palavra {palavra}.
                                        Cheque, se escreveu a palavra corretamente, ou tente uma outra palavra com o mesmo significado.<br>
                                        Lembre_se escrever com letra maiúscula quando for nomes próprio, senão escreva com letras minúsculas, e de usar a acentuação corretamente ok!<br>
                                        Lembrando que a Tradução da biblia do site e de João Ferreira de Almeida Revista e atualizada.<br>
                                        Exemplo: Salmo 1 verso 1 -> nesta tradução começa com bem aventurado e não com feliz,<br>
                                        Fica mais fácil se procurar palavras chaves como: fé, amor, socorro, Daví, Eliseu...<br>
                                <a href="javascript: history.go(-1)">Voltar</a>
                                </center></h1>''')
    except Exception as error:
        return HttpResponse(f'Não foi possivel checar a palavra ou frase "{palavra}"\n O erro foi{error}')

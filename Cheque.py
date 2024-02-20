#from tkinter import *
import os
from tkinter import scrolledtext
#from tkinter import messagebox
#import threading

checagem = ''
contidade_cap_verso  = ''
pa = ''
class Cheque_Palavras():
    def __init__(self, p, *kwargs):
        super().__init__(*kwargs)
        global checagem, contidade_cap_verso, pa
        self.livros = []
        self.textos = []
        self.cont = 0

        pa = f'Checagem da palavra ou frase "{p}"'

        self.text_area = ''
        for diretorio, subpastas, arquivos in os.walk('./biblia'):
            for arquivo in arquivos:
                self.livros.append(os.path.join(diretorio, arquivo))

            for item in self.livros:
                livro_format = item
                livro_format = livro_format.replace('./biblia', '')
                livro_format = livro_format.replace('.txt', '')
                livro_format = livro_format.replace('''\\''', '')
                livro_format = livro_format.replace('''/''', '')
                livro_format = livro_format.upper()
                self.cheque_livro = livro_format
                self.cont_cap = 0

                try:
                    with open(item, encoding='latin-1') as livro:
                         lv = livro.readlines()
                         for line in lv:
                            if self.cheque_livro in line:
                                self.cont_cap += 1
                            if p == 'arrebatamento':
                                p = 'arrebatados'
                            if p in line:
                                if f' {p}ais '  in line or f' {p}do '  in line or f' {p}da ' in line or f' {p}ndo ' in line or f' {p}ão ' in line or f' {p}va '  in line or f' {p} '  in line or f' {p}, '  in line or f' {p}. '  in line or f' {p}: '  in line or f' {p}; '  in line:
                                    self.cont += 1
                                    linha = line
                                    for n in range(0, 200):
                                        if str(n) in str(line):
                                            linha = str(linha).replace(f'{n} ', f'{n}\n')
                                    linha = linha.strip()
                                    self.textos.append(f'{self.cheque_livro} Capítulo {self.cont_cap}\nversículo {linha}\n')

                except:
                    with open(item, encoding='utf-8') as livro:
                         lv = livro.readlines()
                         for line in lv:
                            if self.cheque_livro in line:
                                self.cont_cap += 1
                            if p == 'arrebatamento':
                                p = 'arrebatados'

                            if p in line:
                                if f' {p}ais '  in line or f' {p}do '  in line or f' {p}da ' in line or f' {p}ndo ' in line or f' {p}ão ' in line or f' {p}va '  in line or f' {p} '  in line or f' {p}, '  in line or f' {p}. '  in line or f' {p}: '  in line or f' {p}; '  in line:
                                    self.cont += 1
                                    linha = line
                                    for n in range(0, 200):
                                        if str(n) in str(line):
                                            linha = str(linha).replace(f'{n} ', f'{n}\n')
                                    linha = linha.strip()
                                    self.textos.append(f'{self.cheque_livro} Capítulo {self.cont_cap}\nversículo {linha}\n')

        key = int(len(self.textos))-1

        for i in range(len(self.textos)):
            if p in self.textos[i]:
                self.text_area = self.text_area + f'{self.textos[key]}\n'
                key -= 1


        if str(self.textos) == "[]":
            self.text_area = f'''Não foi indentificada a palavra "{p}" nesta tradução.
Cheque, se escreveu a palavra corretamente, ou tente uma outra palavra com o mesmo significado.
Lembre_se escrever com letra maiúscula quando for nomes próprio, senão escreva com letras minúsculas, e de usar a acentuação corretamente ok!
Lembrando que a Tradução da biblia do site e de João Ferreira de Almeida Revista e atualizada.
Exemplo: Salmo 1 verso 1 -> nesta tradução começa com bem aventurado e não com feliz,
Fica mais fácil se procurar palavras chaves como: fé, amor, socorro, Daví, Eliseu...'''


        if p in str(self.textos):
            contidade_cap_verso = f'Foram encontrados {len(self.textos)} versículos com a palavra ou frase "{p}"'

        checagem = self.text_area
        #threading.Thread(target=p).start()

if __name__ == '__main__':
    Cheque_Palavras('fé')

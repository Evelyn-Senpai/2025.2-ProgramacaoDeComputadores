import requests
import json
import os
import sys
from datetime import datetime

ano_atual = datetime.now().year #pega o ano atual do computador

def solicitar_ano(): #função para a validação de ano
    while True:
        try:
            ano = int(input('Informe o ano desejado: ')) #o usuário digita o ano

            if 2021 <= ano <= ano_atual: #se for encontrado
                return ano #retorna o ano
            else: #se não
                print('Erro: Digite um ano válido.') #dispara o erro

        except ValueError: #exceção para somente números
            print('Erro: Digite apenas números.')
        except Exception as Erro: #exceção genérica
            sys.exit(f'Erro: {Erro}.')

def origem_dos_dados(ano): #função para buscar a origem dos dados
    try:
        if ano == ano_atual: #se o ano digitado pelo usuário for igual o ano atual
            url = 'https://api.cartolafc.globo.com/atletas/mercado' #pega a url do site do cartola
            return requests.get(url).json() #e os dados vem emformato de dicionário

        else: #se o ano digitado pelo usuário não for igual ao ano atual
            for arquivo in os.listdir(): #busca o arquivo json local
                if str(ano) in arquivo and arquivo.endswith(".json"):
                    with open(arquivo, encoding="utf-8") as f:
                        return json.load(f) #retorna um dicionário
            
            raise FileNotFoundError

    except FileNotFoundError: #exceção para arquivo não encontrado
        sys.exit('Erro: Arquivo não encontrado.')

    except requests.exceptions.RequestException: #exceção para o erro de conexão com o site
        sys.exit('Erro: Erro de conexão com API.')

    except Exception as Erro: #exceção genérica
            sys.exit(f'Erro: {Erro}.')

def tratar_atletas(dados): #função para tratar os dados dos atletas
    atletas = {} #dicionário para cada atleta

    clubes = dados["clubes"] #chave para clube
    posicoes = dados["posicoes"] #chave para posição

    for atleta in dados["atletas"]: #em cada informação de cada atleta do dado atleta

        try:
            media = atleta["media_num"] #chave para a média
            jogos = atleta["jogos_num"] #chave para os jogos

            pontuacao = media * jogos #pontuação do atleta é a média x os jogos

            clube = clubes[str(atleta["clube_id"])] #chave para o id do clube
            posicao = posicoes[str(atleta["posicao_id"])] #chave para o id da posição

            if atleta['foto']: #se o atleta tiver foto
                foto = atleta['foto'].replace('_FORMATO_', '_220x220_').replace('_FORMATO', '_220x220') #pega a foto do atleta
            else: #se não
                foto = None #a foto é igual a vázio

            atletas[str(atleta["atleta_id"])] = { #dados dos atletas
                "nome_atleta": atleta["nome"],
                "apelido": atleta["apelido"],
                "url_foto": foto,
                "nome_clube": clube["nome"],
                "escudo_clube": clube["escudos"]["60x60"],
                "posicao": posicao["nome"],
                "pontuacao": round(pontuacao, 2)
            }

        except Exception as Erro: #exceção genérica
            sys.exit(f'Erro: {Erro}.')

    return atletas #retorna os dados do atleta

ESQUEMAS = { #esquemas taáticos
    "3-4-3": {"Zagueiro":3,"Lateral":0,"Meia":4,"Atacante":3},
    "4-4-2": {"Zagueiro":2,"Lateral":2,"Meia":4,"Atacante":2},
    "4-3-3": {"Zagueiro":2,"Lateral":2,"Meia":3,"Atacante":3},
    "4-5-1": {"Zagueiro":2,"Lateral":2,"Meia":5,"Atacante":1},
    "5-3-2": {"Zagueiro":3,"Lateral":2,"Meia":3,"Atacante":2},
    "5-4-1": {"Zagueiro":3,"Lateral":2,"Meia":4,"Atacante":1}
}

def selecionar_time(atletas, esquema): #função para selecionar os melhores atletas
    selecionados = {} #dicionário dos selecionados

    for posicao in ["Goleiro","Zagueiro","Lateral","Meia","Atacante","Técnico"]: #ordem dos que serão selecionados

        if posicao == "Goleiro" or posicao == "Técnico": #a quantidade de técnico e goleiro é sempre 1
            quantidade = 1
        else: #para as outras posições busca no dicionário
            quantidade = ESQUEMAS[esquema][posicao]

        jogadores = [ #cria uma lista com o id o atleta e os dados
            (id_, dados) 
            for id_, dados in atletas.items()
            if dados["posicao"] == posicao
        ]

        jogadores.sort(key=lambda x: x[1]["pontuacao"], reverse=True) #ordenada os jogadores por pontuação de cada posição do maior para o menor

        for id_, dados in jogadores[:quantidade]: #seleciona a quantidade de acor com o esquema tático digitado pelo usuário
            selecionados[id_] = dados

    return selecionados #retorna os selecionados

def salvar_json(selecao, ano, esquema): #função para saltar a seleção em um arquivo json
    try:
        nome = f'selecao_cartolafc_{ano}_{esquema}.json'.lower() #nome do arquivo com o ano e esquema tático escolhido pelo usuário

        with open(nome, "w", encoding="utf-8") as f: #abre ou cria o arquivo, escreve as informações e depois o fecha
            json.dump(selecao, f, indent=4, ensure_ascii=False)

        print(f'Arquivo gerado com sucesso: {nome}') #print do arquivo gerado
    except json.JSONDecodeError:
        sys.exit('Erro: Erro na estrura do arquivo json.')
    except KeyError:
        sys.exit('Erro: Erro na resposta da API.')

def mostrar_selecao(selecao, ano, esquema): #função para printar a seleção

    ordem = ["Goleiro","Zagueiro","Lateral","Meia","Atacante","Técnico"] #a ordem das posições

    print('='*90)
    print(f'SELEÇÃO CARTOLA FC - ANO {ano}'.center(90)) #o título centralizado
    print(f'ESQUEMA {esquema}'.center(90)) #o esquema tático centralizado
    print('='*90)

    for posicao in ordem: #percorre cada posicao
        for jogador in selecao.values(): #percorre cada jogador só pelos valores
            if jogador["posicao"] == posicao: #se o jogador pertencer a posição atual
                print(f"{posicao.upper():10} | {jogador['nome_atleta']} ({jogador['apelido']}) | "
                      f"{jogador['nome_clube']} | {jogador['pontuacao']}") #printa os dados

def solicitar_esquema(): #função para solicitar o esquema tático corretamente
    try:
        print('Esquemas disponíveis:') 
        for esquema in ESQUEMAS: #printa os esquemas táticos disponíveis
            print(f"- {esquema}")

        while True: #enquanto o usuário não digitar um esquema tático disponível ele não avança
            esquema = input('Escolha esquema tático: ')

            if esquema in ESQUEMAS:
                return esquema
            else:
                print('Erro: Esquema inválido. Tente novamente.')
    
    except Exception as Erro: #exceção genérica
        sys.exit(f'Erro: {Erro}')

def main(): #função principal

    ano = solicitar_ano() #pede o ano ao usuário que já está válidado
    dados = origem_dos_dados(ano) #busca os dados com o ano e tudo já válidado

    if not dados: #se não tem dado, retorna vázio
        return

    atletas = tratar_atletas(dados) #pega os atletas com os dados já tratados

    esquema = solicitar_esquema() #chama a função que solicita o esquema tático

    selecao = selecionar_time(atletas, esquema) #monta a seleção

    salvar_json(selecao, ano, esquema) #salva a seleção no arquivo
    mostrar_selecao(selecao, ano, esquema) #printa a seleção


main() #chama a função principal


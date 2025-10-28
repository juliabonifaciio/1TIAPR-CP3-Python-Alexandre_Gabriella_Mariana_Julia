# persistencia.py
# Funções para salvar e carregar tarefas de arquivo

import json
import os


def salvar_tarefas(lista_tarefas, nome_arquivo='tarefas.json'):
    """
    Salva a lista de tarefas em um arquivo JSON
    """
    try:
        # Abre o arquivo em modo de escrita
        arquivo = open(nome_arquivo, 'w', encoding='utf-8')
        
        # Converte a lista de tarefas para JSON e salva
        json.dump(lista_tarefas, arquivo, ensure_ascii=False, indent=4)
        
        # Fecha o arquivo
        arquivo.close()
        
        return True
    except Exception as erro:
        print(f"Erro ao salvar tarefas: {erro}")
        return False


def carregar_tarefas(nome_arquivo='tarefas.json'):
    """
    Carrega a lista de tarefas de um arquivo JSON
    """
    # Verifica se o arquivo existe
    if not os.path.exists(nome_arquivo):
        # Se não existir, retorna uma lista vazia
        return []
    
    try:
        # Abre o arquivo em modo de leitura
        arquivo = open(nome_arquivo, 'r', encoding='utf-8')
        
        # Lê o conteúdo do arquivo e converte de JSON para lista
        lista_tarefas = json.load(arquivo)
        
        # Fecha o arquivo
        arquivo.close()
        
        return lista_tarefas
    except Exception as erro:
        print(f"Erro ao carregar tarefas: {erro}")
        return []


def arquivo_existe(nome_arquivo='tarefas.json'):
    """
    Verifica se o arquivo de tarefas existe
    """
    return os.path.exists(nome_arquivo)


def criar_backup(nome_arquivo='tarefas.json', nome_backup='tarefas_backup.json'):
    """
    Cria uma cópia de backup do arquivo de tarefas
    """
    if not arquivo_existe(nome_arquivo):
        return False
    
    try:
        # Lê o arquivo original
        arquivo_original = open(nome_arquivo, 'r', encoding='utf-8')
        conteudo = arquivo_original.read()
        arquivo_original.close()
        
        # Escreve no arquivo de backup
        arquivo_backup = open(nome_backup, 'w', encoding='utf-8')
        arquivo_backup.write(conteudo)
        arquivo_backup.close()
        
        return True
    except Exception as erro:
        print(f"Erro ao criar backup: {erro}")
        return False
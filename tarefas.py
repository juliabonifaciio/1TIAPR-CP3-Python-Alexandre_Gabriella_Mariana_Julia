# tarefas.py
# Funções para gerenciar as tarefas

def criar_tarefa(descricao, data_vencimento, status):
    """
    Cria uma nova tarefa
    """
    tarefa = {
        'id': None,  # Será definido ao adicionar na lista
        'descricao': descricao,
        'data_vencimento': data_vencimento,
        'status': status
    }
    return tarefa


def cadastrar_tarefa(lista_tarefas, descricao, data_vencimento, status):
    """
    Cadastra uma nova tarefa na lista
    """
    # Gera um ID único baseado no tamanho da lista
    if len(lista_tarefas) == 0:
        novo_id = 1
    else:
        # Pega o maior ID e adiciona 1
        maior_id = 0
        for tarefa in lista_tarefas:
            if tarefa['id'] > maior_id:
                maior_id = tarefa['id']
        novo_id = maior_id + 1
    
    tarefa = criar_tarefa(descricao, data_vencimento, status)
    tarefa['id'] = novo_id
    lista_tarefas.append(tarefa)
    return True


def listar_todas_tarefas(lista_tarefas):
    """
    Retorna todas as tarefas
    """
    return lista_tarefas


def filtrar_por_status(lista_tarefas, status):
    """
    Filtra tarefas por status
    """
    tarefas_filtradas = []
    for tarefa in lista_tarefas:
        if tarefa['status'] == status:
            tarefas_filtradas.append(tarefa)
    return tarefas_filtradas


def filtrar_por_data(lista_tarefas, data_vencimento):
    """
    Filtra tarefas por data de vencimento
    """
    tarefas_filtradas = []
    for tarefa in lista_tarefas:
        if tarefa['data_vencimento'] == data_vencimento:
            tarefas_filtradas.append(tarefa)
    return tarefas_filtradas


def buscar_tarefa_por_id(lista_tarefas, id_tarefa):
    """
    Busca uma tarefa pelo ID
    """
    for tarefa in lista_tarefas:
        if tarefa['id'] == id_tarefa:
            return tarefa
    return None


def atualizar_tarefa(lista_tarefas, id_tarefa, nova_descricao=None, nova_data=None, novo_status=None):
    """
    Atualiza informações de uma tarefa
    """
    tarefa = buscar_tarefa_por_id(lista_tarefas, id_tarefa)
    
    if tarefa is None:
        return False
    
    # Atualiza apenas os campos que foram fornecidos
    if nova_descricao is not None:
        tarefa['descricao'] = nova_descricao
    
    if nova_data is not None:
        tarefa['data_vencimento'] = nova_data
    
    if novo_status is not None:
        tarefa['status'] = novo_status
    
    return True


def remover_tarefa(lista_tarefas, id_tarefa):
    """
    Remove uma tarefa da lista
    """
    tarefa = buscar_tarefa_por_id(lista_tarefas, id_tarefa)
    
    if tarefa is None:
        return False
    
    lista_tarefas.remove(tarefa)
    return True


def contar_tarefas_por_status(lista_tarefas):
    """
    Conta quantas tarefas existem em cada status
    """
    contadores = {
        'pendente': 0,
        'em andamento': 0,
        'concluida': 0
    }
    
    for tarefa in lista_tarefas:
        status = tarefa['status']
        if status in contadores:
            contadores[status] = contadores[status] + 1
    
    return contadores
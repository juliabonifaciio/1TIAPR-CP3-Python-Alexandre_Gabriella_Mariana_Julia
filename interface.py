# interface.py
# Interface de linha de comando para o sistema de tarefas

import tarefas
import persistencia


def limpar_tela():
    """
    Limpa a tela do terminal
    """
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


def exibir_menu():
    """
    Exibe o menu principal
    """
    print("\n" + "="*50)
    print("        SISTEMA DE GERENCIAMENTO DE TAREFAS")
    print("="*50)
    print("\n1 - Cadastrar nova tarefa")
    print("2 - Listar todas as tarefas")
    print("3 - Filtrar tarefas por status")
    print("4 - Filtrar tarefas por data")
    print("5 - Atualizar tarefa")
    print("6 - Remover tarefa")
    print("7 - Estatísticas")
    print("0 - Sair")
    print("-"*50)


def exibir_tarefa(tarefa):
    """
    Exibe as informações de uma tarefa
    """
    print(f"\nID: {tarefa['id']}")
    print(f"Descrição: {tarefa['descricao']}")
    print(f"Data de Vencimento: {tarefa['data_vencimento']}")
    print(f"Status: {tarefa['status']}")
    print("-"*50)


def exibir_lista_tarefas(lista_tarefas):
    """
    Exibe uma lista de tarefas
    """
    if len(lista_tarefas) == 0:
        print("\nNenhuma tarefa encontrada!")
        return
    
    print(f"\nTotal de tarefas: {len(lista_tarefas)}")
    for tarefa in lista_tarefas:
        exibir_tarefa(tarefa)


def opcao_cadastrar(lista_tarefas):
    """
    Interface para cadastrar uma nova tarefa
    """
    print("\n--- CADASTRAR NOVA TAREFA ---")
    
    descricao = input("Descrição da tarefa: ")
    data_vencimento = input("Data de vencimento (DD/MM/AAAA): ")
    
    print("\nEscolha o status:")
    print("1 - Pendente")
    print("2 - Em andamento")
    print("3 - Concluída")
    opcao_status = input("Opção: ")
    
    if opcao_status == '1':
        status = 'pendente'
    elif opcao_status == '2':
        status = 'em andamento'
    elif opcao_status == '3':
        status = 'concluida'
    else:
        print("\nStatus inválido! Usando 'pendente' como padrão.")
        status = 'pendente'
    
    sucesso = tarefas.cadastrar_tarefa(lista_tarefas, descricao, data_vencimento, status)
    
    if sucesso:
        print("\nTarefa cadastrada com sucesso!")
        persistencia.salvar_tarefas(lista_tarefas)
    else:
        print("\nErro ao cadastrar tarefa!")


def opcao_listar(lista_tarefas):
    """
    Interface para listar todas as tarefas
    """
    print("\n--- LISTA DE TAREFAS ---")
    todas_tarefas = tarefas.listar_todas_tarefas(lista_tarefas)
    exibir_lista_tarefas(todas_tarefas)


def opcao_filtrar_status(lista_tarefas):
    """
    Interface para filtrar tarefas por status
    """
    print("\n--- FILTRAR POR STATUS ---")
    print("1 - Pendente")
    print("2 - Em andamento")
    print("3 - Concluída")
    opcao = input("Escolha o status: ")
    
    if opcao == '1':
        status = 'pendente'
    elif opcao == '2':
        status = 'em andamento'
    elif opcao == '3':
        status = 'concluida'
    else:
        print("\nOpção inválida!")
        return
    
    tarefas_filtradas = tarefas.filtrar_por_status(lista_tarefas, status)
    exibir_lista_tarefas(tarefas_filtradas)


def opcao_filtrar_data(lista_tarefas):
    """
    Interface para filtrar tarefas por data
    """
    print("\n--- FILTRAR POR DATA ---")
    data = input("Digite a data (DD/MM/AAAA): ")
    
    tarefas_filtradas = tarefas.filtrar_por_data(lista_tarefas, data)
    exibir_lista_tarefas(tarefas_filtradas)


def opcao_atualizar(lista_tarefas):
    """
    Interface para atualizar uma tarefa
    """
    print("\n--- ATUALIZAR TAREFA ---")
    
    try:
        id_tarefa = int(input("Digite o ID da tarefa: "))
    except ValueError:
        print("\nID inválido!")
        return
    
    tarefa = tarefas.buscar_tarefa_por_id(lista_tarefas, id_tarefa)
    
    if tarefa is None:
        print("\nTarefa não encontrada!")
        return
    
    print("\nTarefa atual:")
    exibir_tarefa(tarefa)
    
    print("\nO que deseja atualizar?")
    print("1 - Descrição")
    print("2 - Data de vencimento")
    print("3 - Status")
    print("4 - Tudo")
    opcao = input("Opção: ")
    
    nova_descricao = None
    nova_data = None
    novo_status = None
    
    if opcao == '1' or opcao == '4':
        nova_descricao = input("Nova descrição: ")
    
    if opcao == '2' or opcao == '4':
        nova_data = input("Nova data (DD/MM/AAAA): ")
    
    if opcao == '3' or opcao == '4':
        print("\nNovo status:")
        print("1 - Pendente")
        print("2 - Em andamento")
        print("3 - Concluída")
        opcao_status = input("Opção: ")
        
        if opcao_status == '1':
            novo_status = 'pendente'
        elif opcao_status == '2':
            novo_status = 'em andamento'
        elif opcao_status == '3':
            novo_status = 'concluida'
    
    sucesso = tarefas.atualizar_tarefa(lista_tarefas, id_tarefa, nova_descricao, nova_data, novo_status)
    
    if sucesso:
        print("\nTarefa atualizada com sucesso!")
        persistencia.salvar_tarefas(lista_tarefas)
    else:
        print("\nErro ao atualizar tarefa!")


def opcao_remover(lista_tarefas):
    """
    Interface para remover uma tarefa
    """
    print("\n--- REMOVER TAREFA ---")
    
    try:
        id_tarefa = int(input("Digite o ID da tarefa: "))
    except ValueError:
        print("\nID inválido!")
        return
    
    tarefa = tarefas.buscar_tarefa_por_id(lista_tarefas, id_tarefa)
    
    if tarefa is None:
        print("\nTarefa não encontrada!")
        return
    
    print("\nTarefa a ser removida:")
    exibir_tarefa(tarefa)
    
    confirmacao = input("\nTem certeza que deseja remover? (s/n): ")
    
    if confirmacao.lower() == 's':
        sucesso = tarefas.remover_tarefa(lista_tarefas, id_tarefa)
        
        if sucesso:
            print("\nTarefa removida com sucesso!")
            persistencia.salvar_tarefas(lista_tarefas)
        else:
            print("\nErro ao remover tarefa!")
    else:
        print("\nRemoção cancelada!")


def opcao_estatisticas(lista_tarefas):
    """
    Interface para exibir estatísticas
    """
    print("\n--- ESTATÍSTICAS ---")
    
    contadores = tarefas.contar_tarefas_por_status(lista_tarefas)
    total = len(lista_tarefas)
    
    print(f"\nTotal de tarefas: {total}")
    print(f"Pendentes: {contadores['pendente']}")
    print(f"Em andamento: {contadores['em andamento']}")
    print(f"Concluídas: {contadores['concluida']}")
    print("-"*50)


def executar():
    """
    Função principal que executa o sistema
    """
    # Carrega as tarefas do arquivo
    lista_tarefas = persistencia.carregar_tarefas()
    
    print("\nBem-vindo ao Sistema de Gerenciamento de Tarefas!")
    
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            opcao_cadastrar(lista_tarefas)
        elif opcao == '2':
            opcao_listar(lista_tarefas)
        elif opcao == '3':
            opcao_filtrar_status(lista_tarefas)
        elif opcao == '4':
            opcao_filtrar_data(lista_tarefas)
        elif opcao == '5':
            opcao_atualizar(lista_tarefas)
        elif opcao == '6':
            opcao_remover(lista_tarefas)
        elif opcao == '7':
            opcao_estatisticas(lista_tarefas)
        elif opcao == '0':
            print("\nSalvando tarefas...")
            persistencia.salvar_tarefas(lista_tarefas)
            print("Obrigado por usar o sistema!")
            break
        else:
            print("\nOpção inválida! Tente novamente.")
        
        input("\nPressione ENTER para continuar...")


# Executa o sistema se o arquivo for executado diretamente
if __name__ == "__main__":
    executar()
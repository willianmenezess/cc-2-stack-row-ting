from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    """Aqui irá sua implementação da fila de prioridade (PriorityQueue)"""
#   Testa uso relevante do método 'enqueue'
    mock_dict1 = {"qtd_linhas": 4, "nome_do_arquivo": "arquivo.txt"}
    mock_dict2 = {"qtd_linhas": 6, "nome_do_arquivo": "arquivo2.txt"}
    mock_dict3 = {"qtd_linhas": 3, "nome_do_arquivo": "arquivo3.txt"}
    mock_dict4 = {"qtd_linhas": 7, "nome_do_arquivo": "arquivo4.txt"}
    mock_dict5 = {"qtd_linhas": 1, "nome_do_arquivo": "arquivo5.txt"}
    fila = PriorityQueue()  # Fila de prioridade
    fila.enqueue(mock_dict1)
    fila.enqueue(mock_dict2)
    fila.enqueue(mock_dict3)
    fila.enqueue(mock_dict4)
    fila.enqueue(mock_dict5)
    assert len(fila.high_priority) == 3
    assert len(fila.regular_priority) == 2
    assert fila.__len__() == 5
    assert fila.high_priority.search(0) == mock_dict1
    assert fila.high_priority.search(1) == mock_dict3

# O teste levanta exceção ao acessar índices inválidos para Filas;
    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        fila.search(99)

# Testa uso relevante do método 'dequeue'
    fila.dequeue()  # tira o mock_dict1 da fila
    assert fila.__len__() == 4
    assert fila.high_priority.search(0) == mock_dict3

# Testa regra de prioridade
    assert fila.is_priority(mock_dict1) is True
    assert fila.is_priority(mock_dict2) is False

# Testa busca com comportamento invertido
    assert fila.search(0) == mock_dict3  # dict1 foi removido, dict3 é o 1º
    assert fila.search(1) == mock_dict5

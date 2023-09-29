from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    """Aqui irá sua implementação"""
#   Testar uso relevante do método 'enqueue'
    mock_dict1 = {"qtd_linhas": 4, "nome_do_arquivo": "arquivo.txt"}
    mock_dict2 = {"qtd_linhas": 6, "nome_do_arquivo": "arquivo2.txt"}
    mock_dict3 = {"qtd_linhas": 3, "nome_do_arquivo": "arquivo3.txt"}
    mock_dict4 = {"qtd_linhas": 7, "nome_do_arquivo": "arquivo4.txt"}
    mock_dict5 = {"qtd_linhas": 1, "nome_do_arquivo": "arquivo5.txt"}
    fila = PriorityQueue()
    fila.enqueue(mock_dict1)
    fila.enqueue(mock_dict2)
    fila.enqueue(mock_dict3)
    fila.enqueue(mock_dict4)
    fila.enqueue(mock_dict5)
    assert len(fila) == 5
    assert fila.high_priority.search(0) == mock_dict1
    assert fila.high_priority.search(1) == mock_dict3

# Testar uso relevante do método 'dequeue'
    fila.dequeue()  # tira o mock_dict1 da fila
    assert len(fila) == 2
    assert fila.high_priority.search(0) == mock_dict3

# Testar busca com comportamento invertido
    fila2 = PriorityQueue()
    fila2.enqueue(mock_dict1)
    fila2.enqueue(mock_dict2)
    fila2.enqueue(mock_dict3)
    assert fila2.high_priority.search(0) == mock_dict1
    assert fila2.high_priority.search(1) == mock_dict3
    assert fila2.high_priority.search(3) == mock_dict2

# Testar regra de prioridade inexistente (sempre True)
    fila3 = PriorityQueue()
    fila3.enqueue(mock_dict1)
    fila3.enqueue(mock_dict2)
    fila3.enqueue(mock_dict3)
    assert fila3.high_priority.search(0) == mock_dict1
    assert fila3.high_priority.search(1) == mock_dict2
    assert fila3.high_priority.search(2) == mock_dict3
    assert fila3.high_priority.search(3) is None

# Testar lançamento de erro com índice inválido na busca
    fila4 = PriorityQueue()
    fila4.enqueue(mock_dict1)
    fila4.enqueue(mock_dict2)
    fila4.enqueue(mock_dict3)
    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        fila4.high_priority.search(3)

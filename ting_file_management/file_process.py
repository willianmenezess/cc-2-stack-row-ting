from ting_file_management.file_management import txt_importer
from queue import Queue
import sys


def process(path_file, instance):
    """Transforma o retorno da função txt_importer em um
    dicionário que será armazenado dentro da Queue"""
    for q in instance._data:
        if q['nome_do_arquivo'] == path_file:
            return None

    list_lines_txt = txt_importer(path_file)
    new_enqueue = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(list_lines_txt),
        'linhas_do_arquivo': list_lines_txt,
    }
    instance.enqueue(new_enqueue)
    print(new_enqueue)


def remove(instance):
    """Remove o primeiro elemento da fila"""
    if instance.is_empty():
        return print('Não há elementos')
    else:
        fileDequeued = instance.dequeue()
        return print(
          f"Arquivo {fileDequeued['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance, position):
    """Retorna os metadados de um arquivo específico"""
    try:
        metadata = instance.search(position)
        sys.stdout.write(f'{metadata}')
    except IndexError:
        sys.stderr.write("Posição inválida\n")


if __name__ == "__main__":
    instance = Queue()
    path_file = "statics/arquivo_teste.txt"
    process(path_file, instance)
    # remove(instance)
    file_metadata(instance, 1)

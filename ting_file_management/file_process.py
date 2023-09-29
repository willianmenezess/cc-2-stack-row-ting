from ting_file_management.file_management import txt_importer
from queue import Queue
from sys import stdout


def process(path_file, instance):
    """Transforma o retorno da função txt_importer em um
    dicionário que será armazenado dentro da Queue"""
    list_lines_txt = txt_importer(path_file)
    qty_lines = len(list_lines_txt)
    new_enqueue = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': qty_lines,
        'linhas_do_arquivo': list_lines_txt
    }
    if instance.get_element(new_enqueue):
        return None

    # adicionando o dicionário na fila
    instance.enqueue(new_enqueue)
    stdout.write(f"{instance._data}\n")


def remove(instance):
    if instance.is_empty():
        return stdout.write('Não há elementos\n')
    else:
        fileDequeued = instance.dequeue()
        return stdout.write(
          f"Arquivo {fileDequeued['nome_do_arquivo']} removido com sucesso\n")


def file_metadata(instance, position):
    try:
        stdout.write(
            f"{instance.search(position)}\n"
        )
    except IndexError:
        stdout.write("Posição inválida ou inexistente\n")


if __name__ == "__main__":
    instance = Queue()
    path_file = "statics/arquivo_teste.txt"
    process(path_file, instance)
    # remove(instance)
    file_metadata(instance, 0)

from ting_file_management.file_management import txt_importer
from queue import Queue
from sys import stdout


def process(path_file, instance):
    """Transforma o retorno da função txt_importer em um
    dicionário que será armazenado dentro da Queue"""
    list_lines_txt = txt_importer(path_file)
    qty_lines = len(list_lines_txt)

    dict_txt = {
        "nome do arquivo": path_file,
        "qtd_linhas": qty_lines,
        "linhas _do_arquivo": list_lines_txt
    }

    if instance.get_element(dict_txt) is None:
        instance.enqueue(dict_txt)
        stdout.write(f"{dict_txt}\n")


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""


if __name__ == "__main__":
    path_file = "teste.txt"
    instance = Queue()
    # print(instance)  # antes de processar e colocar na fila
    process(path_file, instance)
    print(instance)  # depois de processar e colocar na fila

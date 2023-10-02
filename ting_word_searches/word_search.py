from queue import Queue
# from ting_file_management.file_management import txt_importer
from ting_file_management.file_process import process


def exists_word(word, instance):
    """A função deve retornar uma lista com as informações de cada
    arquivo e suas linhas em que a palavra foi encontrada"""
    list_search_occurrences = []
    for dict in instance._data:
        occurrences = []
        for index, line in enumerate(dict['linhas_do_arquivo']):
            if word.lower() in line.lower():
                occurrences.append({"linha": index + 1})
        if len(occurrences) > 0:
            new_dict = {
                "palavra": word.lower(),
                "arquivo": dict['nome_do_arquivo'],
                "ocorrencias": occurrences
            }
            list_search_occurrences.append(new_dict)
    return list_search_occurrences


def search_by_word(word, instance):
    """Aqui irá sua implementação"""


if __name__ == "main":
    word = "pedro"
    path_file = "statics/nome_pedro.txt"
    instance = Queue()
    process(path_file, instance)
    print(exists_word(word, instance))

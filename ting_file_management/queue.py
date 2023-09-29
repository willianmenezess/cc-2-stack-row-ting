from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    """Implementação da ED Fila usando list"""
    def __init__(self):
        self._data = list()

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        return self._data.pop(0)

    def search(self, index):
        if index not in range(len(self._data)):
            raise IndexError("Índice Inválido ou Inexistente")
        return self._data[index]

    def get_element(self, value):
        for index, element in enumerate(self._data):
            if element == value:
                return index
        return None

    def __str__(self):
        return str(self._data)

    def is_empty(self):
        return len(self._data) == 0

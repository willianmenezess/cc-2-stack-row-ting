from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    """Implementação da ED Fila usando list"""
    def __init__(self):
        self.__data = list()

    def __len__(self):
        return len(self.__data)

    def enqueue(self, value):
        self.__data.append(value)

    def dequeue(self):
        return self.__data.pop(0)

    def search(self, index):
        if index not in range(len(self.__data)):
            raise IndexError("Índice Inválido ou Inexistente")
        return self.__data[index]

    def get_element(self, value):
        for index, element in enumerate(self.__data):
            if element == value:
                return index
        return None

    def __str__(self):
        return str(self.__data)

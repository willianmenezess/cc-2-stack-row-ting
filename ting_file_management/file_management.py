import sys


def txt_importer(path_file):
    if path_file.split(".")[-1] != "txt":
        sys.stderr.write("Formato inválido")

    try:
        with open(path_file, "r") as file:
            txt_read = file.readlines()
            list_lines_txt = [line.strip() for line in txt_read]
            return list_lines_txt
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")


# if __name__ == "__main__":
#     path_file = "test.txt"
#     print(txt_importer(path_file))

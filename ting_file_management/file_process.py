from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    for i in range(len(instance)):
        if instance.search(i)["nome_do_arquivo"] == path_file:
            print("Arquivo já está na fila")
            return

    file = txt_importer(path_file)

    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file,
    }

    instance.enqueue(data)
    print(data)
    print("Arquivo adicionado com sucesso!")


def remove(instance):
    if len(instance) == 0:
        print("Não há elementos")
        return

    file = instance.dequeue()

    print(f"Arquivo {file['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance, position):
    if position >= len(instance):
        print("Posição inválida", file=sys.stderr)
        return

    file = instance.search(position)

    print(file)

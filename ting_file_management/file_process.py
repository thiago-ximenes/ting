from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    for file in instance.data:
        if file["nome_do_arquivo"] == path_file:
            return None

    file_lines = txt_importer(path_file)
    result = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file_lines),
        "linhas_do_arquivo": file_lines,
    }

    instance.enqueue(result)
    sys.stdout.write(str(result))


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""

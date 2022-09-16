from file_management import txt_importer


def process(path_file, instance):
    file_lines = txt_importer(path_file)
    result = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file_lines),
        "linhas_do_arquivo": file_lines,
    }
    if len(instance) == 0:
        return instance.enqueue(result)
    else:
        for file in instance.data:
            if file["nome_do_arquivo"] == path_file:
                pass

    return instance.enqueue(result)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""

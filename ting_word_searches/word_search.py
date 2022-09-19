def exists_word(word, instance):
    files_with_that_word = []

    for file in instance.data:
        for line in file["linhas_do_arquivo"]:
            if word in line:
                files_with_that_word.append(file)
                break

    result = []

    for file in files_with_that_word:
        result.append({
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            
        })


def search_by_word(word, instance):
    """Aqui irá sua implementação"""

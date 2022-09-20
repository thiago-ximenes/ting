def exists_word(word, instance):
    lower_word = word.lower()
    result = []

    for file in instance.data:
        occurrences = []
        for key, line in enumerate(file["linhas_do_arquivo"], 1):
            print(lower_word)
            if lower_word in line.lower():
                print(line.lower())
                occurrences.append({"linha": key})
                if key == len(file["linhas_do_arquivo"]):
                    result.append(
                        {
                            "palavra": word,
                            "arquivo": file["nome_do_arquivo"],
                            "ocorrencias": occurrences,
                        }
                    )

    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""

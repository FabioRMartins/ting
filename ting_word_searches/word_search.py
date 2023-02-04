def exists_word(word, instance):
    exist = []
    for i in range(len(instance)):
        file = instance.search(i)
        for line in file["linhas_do_arquivo"]:
            if word in line:
                exist.append(file["nome_do_arquivo"])
        if len(exist) > 0:
            return exist
    return exist


def search_by_word(word, instance):
    exist = exists_word(word, instance)
    if len(exist) > 0:
        print(f"Palavra {word} encontrada nos arquivos: {exist}")
    else:
        print(f"Palavra {word} não encontrada")
    return exist

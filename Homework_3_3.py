def thesaurus_adv(*args):
    result = dict()
    for i in args:
        name = i[0]
        if name in result:
            result[name].append(i)
        else:
            result[name] = [i]
    return result

print(thesaurus_adv("LeBron", "Kobe", "Kevin", "Vince"))
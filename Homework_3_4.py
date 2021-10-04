def thesaurus_adv(*args):
    main_dict = dict()
    for input in args:
        name = input.split(" ")[0][0]
        so_name = input.split(" ")[1][0]
        if name in main_dict:
            if so_name in main_dict[name]:
                if input not in main_dict[name][so_name]:
                    main_dict[name][so_name].append(input)
            else:
                main_dict[name][so_name] = [input]
        else:
            main_dict[name] = dict()
            main_dict[name][so_name] = [input]

    return main_dict

print(thesaurus_adv("LeBron James", "Kobe Bryant", "Kevin Garnett", "Vince Carter"))
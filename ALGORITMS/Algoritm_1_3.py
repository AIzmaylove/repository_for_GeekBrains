'''Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.'''

company_profits = {'Nestle': 10000, 'Gazprom': 1234, 'Apple': 3999999,
                   'EpicGames': 87654, 'ARM': 7888, 'Intel': 7887}

### O(N)
'''def find_tops(company_profits):
    top_three = {}
    max_values = max(company_profits, key=company_profits.get)  #O(1)
    for i in range(3):                                          #O(1)
        maximum = max(company_profits.items(), key=lambda key_value: key_value[1]) 
        del company_profits[maximum[0]]                         # O(N)
        top_three[maximum[0]] = maximum[1] 
    print(top_three)                                            # O(1)

find_tops(company_profits)'''

### O(n log n)
''' def find_tops2(company_profits):
    import operator                                                            # O(1)
    sort_dict_v1 = sorted(company_profits.items(), key=operator.itemgetter(1)) # O(n log n)
    print(sort_dict_v1[-3:])                                                   # O(1)

find_tops2(company_profits) '''
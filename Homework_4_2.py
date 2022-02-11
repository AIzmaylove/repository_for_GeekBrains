from requests import get, utils

def currency_rates(ticket):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    server_date = response.headers['Set-Cookie'].split(',')[1]
    print(f' Дата сервера: {server_date}')
    content = response.content.decode(encoding=encodings)

    key_words = ['Nominal', 'Name', 'Value']
    receive_srt = content[content.find(str(ticket).upper()):] # Поиск валюты в общем списке

    if len(receive_srt) > 2:
        receive_srt = receive_srt[:receive_srt.find('</Value>')] # Формирование строки с информацией о валюте

        currency_info = list(map(lambda x: str(receive_srt.split(x)[1])[1:-2], key_words))
        currency_info[0] = int(currency_info[0])
        currency_info[2] = float('.'.join(currency_info[2].split(',')))

        print(f'За {currency_info[0]} {currency_info[1]} дают {currency_info[2]} руб')
    else:
        print(None)

if __name__ == "__main__":
    currency_rates(input('Введите валюту :'))



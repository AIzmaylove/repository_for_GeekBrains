import hashlib
import uuid
salt = uuid.uuid4().hex
cache_obj = {}

def get_page(url):
    if cache_obj.get(url):
        print(f'Данный адрес:  {url} присутствует в кэше')
    else:
        result = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
        cache_obj[url] = result
        print(cache_obj)

get_page('https://geekbrains.re/')
get_page('https://geekbrains.re/')
get_page('https://geekbrains.re/')
import requests
def translate_it(filename, lang, res_filename):
    """
    YANDEX translation plugin

    docs: https://tech.yandex.ru/translate/doc/dg/reference/translate-docpage/

    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]

    :param text: <str> text for translation.
    :return: <str> translated text.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.readline()

    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'

    params = {
        'key': key,
        'lang': '',
        'text': text,
    }
    params.update({'lang': lang})
    response = requests.get(url, params=params).json()
    res_text = ' '.join(response.get('text', []))
    # return ' '.join(response.get('text', []))
    
    with open(res_filename, 'w') as res_f:
        res_f.write(res_text)


if __name__ == "__main__":
    filename = input('Введите название файла: ')
    lang = input('Введите оригинальный язык: ') + '-' + input('Введите язык перевода: ')
    res_filename = input('Введите название файла, в который хотите сохранить перевод: ')
    translate_it(filename, lang, res_filename)
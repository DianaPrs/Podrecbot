import requests
import json


def search_title(term): 
    parameters = {'term': term, 'country':'RU', 'media': 'podcast', 'entity': 'podcast', 'limit': 5}
    r = requests.get('https://itunes.apple.com/search', params=parameters)

    try:
        json = r.json()['results']
        result_count = r.json()['resultCount']
        print(f'Нашлось: {result_count}')

    except(requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False

    result_list = []
    if result_count == 0:
        return False 
    else:
        for result in json:
            url = result['collectionViewUrl']
            result_list.append(url)

    return result_list

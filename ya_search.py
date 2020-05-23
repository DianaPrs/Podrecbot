import requests
import json


def yandex_search(term):
    parameters = {'text': term, 'type': 'podcast', 'lang': 'ru'}
    r = requests.get('https://music.yandex.by/handlers/music-search.jsx', params=parameters)

    try:
        r.raise_for_status()
        info = json.loads(r.text)

    except(requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False

    id_list = []
    items = info['podcasts']['items']
    if not items:
        return False
    else:
        for item in items[:5]:
            track_id = item['id']
            id_list.append(track_id)

    return id_list

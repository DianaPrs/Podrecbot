from googleapiclient.discovery import build
import settings
import pprint


def google_search(search_term, api_key=settings.KEY, cse_id=settings.CSE, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()

    count = res['searchInformation']['totalResults']
    print(f'Нашлось: {count}')

    items = res['items']
    url_list = []
    for item in items[:5]:
        url = item['link']
        url_list.append(url)

    return url_list

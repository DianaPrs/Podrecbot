import requests
import json


def search_title(term): 
    parameters = {'term': term, 'country':'RU', 'media': 'podcast', 'entity': 'podcast', 'limit': 5}
    r = requests.get('https://itunes.apple.com/search', params=parameters)
    
    try:
        json = r.json()['results']
        result_count = r.json()['resultCount']
        print(f'Нашлось: {result_count}')
             
    except IndexError:
        print('No result')
        return None
    result_list = []
    for result in json:
        url = result['collectionViewUrl']
        result_list.append(url)
    
    return result_list
        
        
'''
attribute = titleTerm, languageTerm, authorTerm, genreIndex, 
artistTerm, ratingIndex, keywordsTerm, descriptionTerm
# The default is all attributes associated with the specified media type.

        print(result_list['trackCount'])
        print(result_list['collectionName'])
        print(result_list['artistName'])
        print(result_list['releaseDate'][:10])
    # должен отдавать несколько значений


{
 "resultCount":1,
 "results": [
{"wrapperType":"track", 
"kind":"podcast", 
"collectionId":1355504870, 
"trackId":1355504870, 
"artistName":"Kamhorka Production",
"collectionName":"Привет, Андрей!",
"trackName":"Привет, Андрей!",
"collectionCensoredName":"Привет, Андрей!", 
"trackCensoredName":"Привет, Андрей!",
 "collectionViewUrl":"https://podcasts.apple.com/ru/podcast/%D0%BF%D1%80%D0%B8%D0%B2%D0%B5%D1%82-%D0%B0%D0%BD%D0%B4%D1%80%D0%B5%D0%B9/id1355504870?uo=4", "feedUrl":"https://feeds.simplecast.com/gO3j9MGb", "trackViewUrl":"https://podcasts.apple.com/ru/podcast/%D0%BF%D1%80%D0%B8%D0%B2%D0%B5%D1%82-%D0%B0%D0%BD%D0%B4%D1%80%D0%B5%D0%B9/id1355504870?uo=4", "artworkUrl30":"https://is3-ssl.mzstatic.com/image/thumb/Podcasts113/v4/81/d1/10/81d1109b-8ee8-42ea-ae7f-261d1245362c/mza_6560076162077030473.jpg/30x30bb.jpg", "artworkUrl60":"https://is3-ssl.mzstatic.com/image/thumb/Podcasts113/v4/81/d1/10/81d1109b-8ee8-42ea-ae7f-261d1245362c/mza_6560076162077030473.jpg/60x60bb.jpg", "artworkUrl100":"https://is3-ssl.mzstatic.com/image/thumb/Podcasts113/v4/81/d1/10/81d1109b-8ee8-42ea-ae7f-261d1245362c/mza_6560076162077030473.jpg/100x100bb.jpg", "collectionPrice":0.00, "trackPrice":0.00, "trackRentalPrice":0, "collectionHdPrice":0, "trackHdPrice":0, "trackHdRentalPrice":0, "releaseDate":"2020-01-10T13:30:00Z", "collectionExplicitness":"cleaned", "trackExplicitness":"cleaned", "trackCount":49, "country":"RUS", "currency":"RUB", "primaryGenreName":"Технология", "contentAdvisoryRating":"Clean", "artworkUrl600":"https://is3-ssl.mzstatic.com/image/thumb/Podcasts113/v4/81/d1/10/81d1109b-8ee8-42ea-ae7f-261d1245362c/mza_6560076162077030473.jpg/600x600bb.jpg", "genreIds":["1318", "26", "1324"], "genres":["Технология", "Подкасты", "Общество и культура"]}]
}
entities = {'podcastAuthor': 'podcastAuthor',
'podcast': 'podcast'}

'''

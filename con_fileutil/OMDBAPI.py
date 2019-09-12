import urllib

# baseurl = "http://www.omdbapi.com/?t={}&apikey=3e6165e0"
# conner_api_key  = 3e6165e0
# http://www.omdbapi.com/?apikey=[api_key]&
# example usage
# http://www.omdbapi.com/?t=star+wars&apikey=3e6165e0

omdb_title_url = "http://www.omdbapi.com/?t={}&apikey=3e6165e0"

# film_list can be generated from scrapy top grossing movie list
film_list = {'star wars', 'good will hunting'}  # notice, is set
film_dictionary = {}

# requesting omdb data
for film in film_list:
    newurl = omdb_title_url.format("+".join(film.split()))
    # ^ title to url __+__+__ format
    json = requests.get(newurl).json()  # requests url, json back
    film_dictionary[json["Title"]] = json  # append film to dictionary
    # ^ may replace film dictionary title key with imdb code

    # ~~~~financial data scraping~~~~~
    # insert FINANCIAL DATA as dict keys ('Budget', 'Domestic', etc)
    # There is already a key called 'BoxOffice' with value 'N/A'

# print
for elems in film_dictionary:
    print(elems, film_dictionary[elems])

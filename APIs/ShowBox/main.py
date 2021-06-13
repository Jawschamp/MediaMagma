import requests

class ShowBoxAPIParams:
    genre_list = ["Action", "Comedy", "Family", "Kids", "Reality",
                  "Soap", "War", "Fantasy", "Music", "Romance",
                  "talk", "War & Politics", "Adventure", "Documentary",
                  "History", "Mystery", "Sci-Fi & Fantasy", "Thriller", "Western",
                  "Animation", "Drama", "Horror", "News", "Science Fiction", "Tv Movie"
                  ]
    # Fix names
    country_list = ["AR"]
    # Finish country list codes...
class ShowBoxDownloader():
    def download_stream():
        # maybe use the Selenium API select the element
        # and increase to specified said seg#
        #req = requests.get(host + "/" + playback, + "/", key, "/", quality, "/", segment + ".ts")
        return whole

    def validate_and_strip(url):
        req = requests.get(url)
        #if int(200) == req.status_code:
        #    ShowBoxDownloader.download_stream()

        # host:port:/playback:/key:quality:/seg.ts

        
        req = requests.get(url)

class ShowBoxAPI():
    class Endpoints:
        base = "https://www2.showbox-movies.net"
        movies = base + "/movie"

    def search(self):
        pass

    def sort_by_genre(genre: ShowBoxAPIParams.genre_list, genre_input):
        "Genre List is only available from ShowBoxAPIParams.genre_list"
        if genre == genre:
            req = requests.get(ShowBoxAPI.Endpoints.base + "/genre/{}".format(genre)).text
            return req

    def sort_by_country(country: ShowBoxAPIParams.country_list):
        "Only usable from Country Codes..."
        pass
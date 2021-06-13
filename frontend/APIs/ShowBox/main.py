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

        """
        starting_seg is defined by the streamer
        network and counts up from there..
        key is a parameter in the url aka strip.url..."""
    def validate_and_strip(url):
        req = requests.get(url)
        global host, playback, key, quality, segment
        host = req.host
        playback = "v2-hls-playback"
        key = url.strip(host + "/" + playback + "/")
        quality = url.strip(host + "/" + playback + "/" + key)
        print(key)

        if int(200) == req.status_code:
            ShowBoxDownloader.download_stream()

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
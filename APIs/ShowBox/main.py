import requests
import wget
import os


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
    def download_stream(url, num_of_segs):
        os.chdir(r"D:\Github\MediaMagmaV2\images\Moves")
        wget.download(url)
        #for i in range(1, num_of_segs):
            #pass

            # strip this part




        # TODO: Figure out place # of said value: aka ``chars_after_segs``.
    def create_folder(movie_name):
        os.chdir(r"D:\Github\MediaMagmaV2\images\Moves")
        os.mkdir(movie_name)
    def validate_and_strip(url):
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

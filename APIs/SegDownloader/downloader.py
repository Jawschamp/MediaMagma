import wget
import requests

class SegmentedDownloader:
    def seg_HTTP_status_checker():
        pass

    def seg_downloader(url, num_of_segs, fp):
        """
        :param url: url path of download location
        :param num_of_segs: the number of segments a video-segment stream has
        :param fp: where to store the new data (Make this a gui option ig)
        """
        HTTPStatus = requests.get(url).status_code
        if HTTPStatus != 200:
            new_segment = num_of_segs - 100
            if HTTPStatus != 200:
                new_segment = num_of_segs - 1000
            else:
                raise("You entered to many segments!")






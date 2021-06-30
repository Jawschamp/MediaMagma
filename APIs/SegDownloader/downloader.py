import wget
import requests

class SegmentedDownloader:
    def seg_HTTP_status_checker():
        for i in range(1, 16):
            urr = f"https://b-g-eu-4.betterstream.co:2222/v2-hls-playback/0bcacd5c7ee7bd141d2eab3c05b1b3232782fac230ba7836cefa36780bbc21df35733cd4888ce191ae19d4b19b346906fb08999a4191ec863decccb74be8ebd1aa0320aea76e565580da8fdfa285ff0db37a83c76f519bbeb807f86eeb518804878394da32ca628957d6c7668d18a95927b27af77ba15566ac4fba4b56891da27d326cd9f5bcb0ca19c65251221335384054dec412213aea9f7531b01dd8fdd3/720/seg-{i}-v1-a1.ts"
            print(urr.strip("[]"))
            SegmentedDownloader.seg_downloader(urr.strip("[]"), 16, None)
            HTTPStatus = requests.get(SegmentedDownloader.seg_downloader(urr.strip("[]"), 16, None).get("url")).status_code

    def seg_downloader(url, num_of_segs, fp):
        """
        :param url: url path of download location
        :param num_of_segs: the number of segments a video-segment stream has
        :param fp: where to store the new data (Make this a gui option ig)
        """
        pass
        """
        if HTTPStatus != 200:
            new_segment = num_of_segs - 100
            # If HTTPStatus does not return a 200 (success response) take away 100 segments
            if HTTPStatus == 200:
                for add_seg in range(new_segment, new_segment + 10000):
                    pass
                    # If Status is 200 again go up 50 more segments til you hit an error.

                print(new_segment)"""
        return url







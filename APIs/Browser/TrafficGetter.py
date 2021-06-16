from APIs.ShowBox.main import *

from seleniumwire import webdriver


#driver = webdriver.Firefox()



for number in range(326, 658):
    url = f"https://b-g-eu-3.betterstream.co:2222/v2-hls-playback/92a738f5541f848b154dcaa2ec9545b4a7741fa1e72ecc008f8b397b6f55034c0d52d620bc102eb98123f1806fdc1009fadf25c1b058655c55b41019bc60a42e7d9b50780ffbeaa47ec7e6602c21ace36f98a62c56b72c8ffa19fc9d7c1e10712cad5c62c66dbd0d02b9c5ed796640c0e075cface5ccab9f006fc7243cea171a75d9e8fa856d3d770021de440109a622b0b43161b6295c31d8a66db965c71149/720/seg-{number}-v1-a1.ts"
    print(url)
    ShowBoxDownloader.download_stream(url)

def report_back():
    for request in driver.requests:
        MP2T = request.response.headers["Content-Type"]
        if MP2T == "video/MP2T":
            print(request.url)
            ShowBoxDownloader.validate_and_strip(request.url)
            driver.close()

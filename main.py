from APIs.ShowBox.main import *
for i in range(99999, 999999):
    url = f"https://e1v-h.phncdn.com/hls/videos/202012/28/379233592/,1080P_4000K,720P_4000K,480P_2000K,240P_1000K,_379233592.mp4.urlset/seg-{i}-f1-v1-a1.ts?validfrom=1623873772&validto=1623880972&ip=107.181.177.130&ipa=107.181.177.130&hdl=-1&hash=REaUcTdsBJ5WHUoT94kF1R%2BKMAg%3D"
    print(url.strip("[]"))
    ShowBoxDownloader.download_stream(url.strip("[]"), 16)

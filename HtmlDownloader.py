__author__ = 'Administrator'
import requests


class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None
        headers = {"User-Agent" : "User-Agent:Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}
        r = requests.get(url=url,headers=headers)

        if r.status_code == 200:
            r.encoding = 'utf-8'
            return r.text
        return None
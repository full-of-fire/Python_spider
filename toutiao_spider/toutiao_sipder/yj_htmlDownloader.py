from urllib import request
class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None
        respose = request.urlopen(url)
        if respose.getcode() != 200:
            return None
        return respose.read()


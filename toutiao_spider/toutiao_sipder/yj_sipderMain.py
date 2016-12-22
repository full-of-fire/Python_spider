from toutiao_sipder import yj_urlManager
from toutiao_sipder import yj_htmlDownloader
from toutiao_sipder import yj_htmlParser
from toutiao_sipder import yj_htmlOutput

class SpiderMain(object):
    def __init__(self):
        self.urlManager = yj_urlManager.UrlManager()
        self.downloader = yj_htmlDownloader.HtmlDownloader()
        self.htmlParser = yj_htmlParser.HtmlParser()
        self.htmlOutput = yj_htmlOutput.HtmlOutper()


    def start_craw(self,main_url):
        count = 1

        self.urlManager.add_new_url(main_url)

        while self.urlManager.has_new_url():
            try:
                new_url = self.urlManager.get_new_url()
                print('craw %d:%s'%(count,new_url))
                html_string = self.downloader.download(new_url)

                new_urls = self.htmlParser.paser(new_url,html_string)

                for url in new_urls:

                    self.htmlOutput.append_data(url)
                    self.urlManager.add_new_url(url['href'])




                if count == 1000:
                    break
                count = count + 1
            except:
                print("抓取出错啦")

            self.htmlOutput.output_html()



if __name__ == '__main__':
    main_url = "http://www.toutiao.com/a6366528165116805378/"
    spider = SpiderMain()
    spider.start_craw(main_url)
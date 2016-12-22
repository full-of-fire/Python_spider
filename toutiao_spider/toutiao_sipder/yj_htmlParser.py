from bs4 import BeautifulSoup
import re
from urllib import  parse

class HtmlParser(object):
   def paser(self,main_url,html_string):
       if main_url is None or html_string is None:
           return None

       soup = BeautifulSoup(html_string,'html.parser',from_encoding='utf-8')


       news_urls = []



       links = soup.find_all('a',href = re.compile(r"http://toutiao.com/group/[0-9]{1,}/"))
       for link in links:
           new_url = link['href']
           title = link.get_text()

           dic = {}
           dic['href'] = new_url
           dic['title'] = title


           news_urls.append(dic)

       return news_urls

















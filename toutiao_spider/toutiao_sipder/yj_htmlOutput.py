import os

class HtmlOutper(object):
    def __init__(self):
        self.datas = []


    def append_data(self,data):
        if data is None:
            return
        self.datas.append(data)


    def output_html(self):

        with open('output.html','w') as f:

            f.write('<html>')
            f.write("<head><meta http-equiv=\"content-type\" content=\"text/html;charset=utf-8\"></head>")
            f.write("<body>")
            f.write('<table>')

            for data in self.datas:
                f.write('<tr>')
                f.write('<p><a target=\'_blank\' href=%s>%s</a></p>' % (data['href'],data['title']))
                f.write('</tr>')
            f.write('</table>')
            f.write('</body>')
            f.write('</html>')
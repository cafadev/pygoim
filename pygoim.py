from datetime import datetime
from bs4 import BeautifulSoup
from io import BytesIO
import pycurl
import json
import os


class Pygoim:

    def download_page(self, search, size=None, color=None, type_=None, cpr=None):
        # size, color, type_ y cpr
        # Son algunos de los filtros utilizados por Google
        search = search.replace(' ', '+')
        url = 'https://www.google.com/search?q=' + search + '&tbm=isch'

        if size is not None:
            if size == 'lg':
                url += '&tbs=isz:l'
            elif size == 'md':
                url += '&tbs=isz:m'
            elif size == 'sm':
                url += '&tbs=isz:i'
            elif 'x' in size:
                dimensions = size.split('x')
                width, heigth = dimensions[0], dimensions[1]
                url += '&tbs=isz:ex,iszw:%s,iszh:%s' % (width, heigth)

        if color is not None:
            if 'tbs' not in url:
                url += '&tbs='
            else:
                url += ','

            if color == 'all':
                url += 'ic:color'
            elif color == 'gs':
                url += 'ic:gray'
            elif color == 'png':
                url += 'ic:trans'
            else:
                url += 'ic:specific,isc:%s' % color

        if type_ is not None:
            if 'tbs' not in url:
                url += '&tbs='
            else:
                url += ','

            url += 'itp:%s' % type_

        if cpr is not None:
            if 'tbs' not in url:
                url += '&tbs='
            else:
                url += ','

            url += 'sur:%s' % cpr

        buffer = BytesIO()
        c = pycurl.Curl()
        c.setopt(c.URL, url)
        c.setopt(pycurl.HTTPHEADER, ['User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:56.0) Gecko/20100101 Firefox/56.0'])
        c.setopt(pycurl.HTTP_VERSION, pycurl.CURL_HTTP_VERSION_2_0)
        c.setopt(c.WRITEDATA, buffer)
        c.perform()
        c.close()

        body = buffer.getvalue()
        return body.decode('iso-8859-1')

    def image_tracker(self, html_doc):
        supported_formats = ['jpg', 'jpeg', 'png', 'gif']

        soup = BeautifulSoup(html_doc, 'html.parser')
        dirty_img_list = soup.find_all(class_='rg_meta')
        img_list = []

        for tag in dirty_img_list:
            tag_dic = json.loads(tag.get_text())
            if 'ou' in tag_dic and 'ity' in tag_dic:
                if tag_dic['ity'] in supported_formats:
                    img_list.append({
                        'img_url': tag_dic['ou'],
                        'img_type': tag_dic['ity']
                    })
        return img_list

    def download_image(self, img_dict, dest):
        if os.path.isdir(dest) is False:
            raise "Destination path no exist"

        name = str(datetime.time(datetime.now())).replace(':', '-')
        dest += ('/%s.%s' % (name, img_dict['img_type']))

        try:
            with open(dest, 'wb') as image:
                c = pycurl.Curl()
                c.setopt(c.URL, img_dict['img_url'])
                c.setopt(c.WRITEDATA, image)
                c.perform()
                c.close()
        except Exception as e:
            print(e)
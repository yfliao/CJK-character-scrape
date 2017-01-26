from bs4 import BeautifulSoup
import re
import sys
from urllib.parse import urlparse
import urllib.request

class HttpTextParse(object):

    """
    Instance designated towards requesting and parsing data from a HTTP
    GET request.
    """

    def __init__(self, uri):

        self.uri = uri
        self.chinese_text = None
        content = self.request_get_and_extract(self.uri_verify(self.uri))
        self.chinese_text = self.filter_chinese_characters(content)

    def set_input_file(self, uri):

        self.uri = uri

    def uri_verify(self, uri):

        if uri is not None and len(uri) > 1:
            # Use urllib.parse to verify that the passed argument is a url
            o = urlparse(uri)
            if (len(o.netloc) > 0 and len(o.scheme) < 1) or (len(o.path) < 1 and len(o.netloc) == 0) :

                msg = '''
                Provided URI is not valid, format should be: \n
                [protocol][host][path] | e.g. https://www.google.com
                '''

                raise ValueError(msg)

            elif len(o.path) > 0 and len(o.scheme) < 1:
                # add a default scheme
                uri = "http://"+uri
                return uri

            else:
                return uri
        else:
            raise ValueError("Provided URI is not a valid string")

    def request_get_and_extract(self, uri):

        soup = None
        req = urllib.request.Request(uri, data=None, method='GET')
        req.add_header('Cache-Control', 'no-cache')

        # Use BeautifulSoup4 to extract text from response.
        with urllib.request.urlopen(req) as data:
           soup = BeautifulSoup(data, 'html.parser')

        # Extract removes tags/strings from the parse tree

        [s.extract() for s in soup(['[document]', 'head', 'script', 'style', 'title'])]

        text = soup.get_text()
        return text

    def filter_chinese_characters(self, text):

        # Return all characters within the specified unicode range.
        chinese_characters = re.findall(r'([\u4e00-\u9fff]+)', text)
        text_data = ' '.join(chinese_characters)
        return text_data

    def get_chinese_text(self):
        if not self.chinese_text is None:
            return self.chinese_text

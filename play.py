# Let's see what it does with CLI args.

from bs4 import BeautifulSoup
import re
import sys
from urllib.parse import urlparse
import urllib.request

# Reformat this later, I don't know whether to make class or just instantiate a thign.

class HttpTextParse(object):

    """
    Instance designated towards requesting and parsing data from a HTTP
    GET request.
    """

    def __init__(self, uri):

        self.uri = uri

        if self.uri_verify():

            self.filter_chinese_characters(self.request_get_and_extract())

    def uri_verify(self):

        if len(self.uri) > 1:

            # Use urllib.parse to verify that the passed argument is a url
            o = urlparse(c_uri)

            if len(o.scheme) < 1 or len(o.netloc) < 1:

                msg = '''
                Provided URI is not valid, format should be: \n
                [protocol][host][path] | https://www.google.com
                '''

                raise ValueError(msg)

            else:
                return c_uri

        else:

            raise ValueError("Provided URI is not a valid string")

    def request_get_and_extract(self):

        soup = None
        req = urllib.request.Request(c_uri, data=None, method='GET')
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
        text_data = '\n'.join(chinese_characters)
        return text_data

c_uri = sys.argv[1] if len(sys.argv) > 1 else sys.exit('Please provide a second argument uri')
c_uri if isinstance(c_uri, str) else str(c_uri)

textOb = HttpTextParse(c_uri)

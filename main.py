# main.py -- effectively, you run the whole app from here.

from config import *
from lib import csv_read_write as csv_rw, http_text_parse as httptxt, dict_object as data_dict

# retrieve Text
# HTTPTextParse uses the content response and parses the data via the BeautifulSoup4 module.
HttpTextParse = httptxt.HttpTextParse(c_url)
text = HttpTextParse.chinese_text

# CsvReadWrite args are (self, inputFile, outputFile)
CsvReadWrite = csv_rw.CsvReadWrite(DATA_LOCATION, file_dest)

# get the read dictionary.
CeDict = CsvReadWrite.read_into_dictionary()

# This is a dictionary object created from the contents of the CeDict file.
dictionary = data_dict.DictObject(CeDict, text)

# Search the the dictionary for the corresponding pronunciation and translations.
char_trans = dictionary.word_search()

# Write the returned contents to a CSV
CsvReadWrite.write_csv(char_trans)

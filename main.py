# main.py -- effectively, you run the whole app from here.

from config import *
from lib import csv_read_write as csv_rw, http_text_parse as httptxt, dict_object as data_dict

# retieve Text
HttpTextParse = httptxt.HttpTextParse(c_url)
text = HttpTextParse.chinese_text
# CsvReadWrite args are (self, inputFile, outputFile)
CsvReadWrite = csv_rw.CsvReadWrite(DATA_LOCATION, file_dest)
# get the read dictionary.
CeDict = CsvReadWrite.read_into_dictionary()
dictionary = data_dict.DictObject(CeDict, text)
char_trans = dictionary.word_search()

# Write the returned contents to a CSV
CsvReadWrite.write_csv(char_trans)

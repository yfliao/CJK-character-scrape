# main.py -- effectively, you run the whole app from here.

from config import *
from lib import csv_read_write as csv_rw, http_text_parse as httptxt, dict_object as data_dict

# HttpTextParse = httptxt.HttpTextParse(c_url)
# CsvReadWrite args are (self, inputFile, outputFile)
CsvReadWrite = csv_rw.CsvReadWrite(data_location, file_dest)

CsvReadWrite.read_into_dictionary()

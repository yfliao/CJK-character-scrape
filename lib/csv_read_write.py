# csv_read_write.py
# Use the CSV module to read and write dictionary files.

import re
import os.path

class CsvReadWrite(object):

    '''
    Class with methods designed around reading from cc_cedict
    and a designated CSV output file.
    '''

    def __init__(self, inputFile, outputDir, fileName="ce_text_output.csv"):

        self.input_file = inputFile
        self.output_dir = outputDir
        self.file_name = fileName
        self.output_dest = self.get_output_location()

        print(self.output_dest)
        print(self.file_name)

    def get_output_location(self):

        if not isinstance(self.output_dir, str) or not isinstance(self.file_name, str):
            raise ValueError("Output destination/file must be a string.")

        if os.path.isabs(self.output_dir):

            # abspath normalizes the path similar to normpath
            return os.path.abspath(os.path.join(self.output_dir, self.file_name))

        else:

            # set an output path from the root directory
            return os.path.normpath(os.path.join(self.output_dir, self.file_name))

    def read_into_dictionary(self, input_file=None):

        input_file = self.input_file if input_file is None else input_file

        # Read in the datafile to use as a dictionary reference.

        with open(input_file, 'rb') as data:

            data_dict = dict()

            for line in data:
                line = line.decode('utf-8')
                if line.startswith('#') or line == '\n':
                     pass
                else:
                    splitLine = re.split(r'([\u4e00-\u9fff]+)?\s([\u4e00-\u9fff]+)?\s*\[*([^\]]+)?\]*\W+\/+(\[?\b[^\r\n\/(?<=\b)]*\]?)', line)
                    if len(splitLine) >= 4:
                        data_dict[splitLine[1]] = {"pron": splitLine[3], "def": splitLine[4]}
                        if(splitLine[1] != splitLine[2]):
                            data_dict[splitLine[2]] = {"pron": splitLine[3], "def": splitLine[4]}

            try:
                if len(data_dict) > 2:
                    return data_dict
                else:
                    raise AttributeError
            except Exception as e:
                raise AttributeError

    def write_csv(self, outputContent):

        if not isinstance(outputContent, dict):

            raise ValueError("The passed content needs to be in dict format.")

        lines_write = []
        strings_write = ''

        for key, value in outputContent.items():
            values = [key]

            for subkey in value:
                values.append(value[subkey])

                lines_write.append(values)

        for i in lines_write:

            strings_write += ", ".join(i)+"\n"

        try:

            with open(self.output_dest, "wb") as f:
                f.write(strings_write.encode("utf-8"))
                print("Successfully wrote to the file: {}".format(self.output_dest))
        except IOError as e:
            print("Couldn't write to the designated file. {}".format(e))

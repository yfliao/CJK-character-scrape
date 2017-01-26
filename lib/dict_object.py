# dict__object.py -- This file contains the DictObject class
# The main intent of this class is to translate the chinese characters via cc_cedict

class DictObject(object):

    def __init__(self, dictionary, text):

        self.dict = dictionary
        self.text = text

#    def find(self, data, word):

    # word_search() seeks a word using input from
    # the passed text file and cc_cedict based dictionary

    def word_search(self):

        if self.dict is None or self.text is None:

            raise ValueError("Provided arguments are invalid.")

        elif not isinstance(self.dict, dict):

            raise ValueError("Provided dictionary is not of type dict")

        max_chars = 8
        ix = 0
        current_text = ''
        match = None
        matches = {}
        matched = False

        while len(self.text) > 0:
            ix += 1
            current_text = self.text[:ix]

            try:

                match = self.dict[current_text]
                matched = True

            except KeyError:

                if matched:
                    # you should push the match into a python object here
                    self.text = self.text[ix:]
                    ix = 0
                    matches[current_text[:-1]] = match
                    continue
                else:
                    self.text = self.text[ix:]
                    continue


            try:

                if self.text[ix] == "\r" or self.text[ix] == "\n":

                    while self.text[ix] == "\r" or self.text[ix] == "\n":

                        if ix+1 < len(self.text):
                            ix+=1
                        else:
                            continue


                    if matched:

                        self.text = self.text[ix:]
                        ix = 0
                        matches[current_text[ix-1]] = match
                        continue
                    else:

                        self.text = self.text[ix:]
                        ix = 0
                        continue

            except IndexError:

                if matched:
                    matches[current_text[:-1]] = match
                    return matches
                else:
                    return matches

            if ix == max_chars:

                if not matched:

                    self.text = self.text[ix:]
                    ix = 0
                    continue

                else:
                    return match

class SubstitutionTable(dict):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def __init__(self, *args, **kwargs):
        super(SubstitutionTable, self).__init__(*args, **kwargs)
        self.__dict__ = self
        self.reset_table()

    def reset_table(self):
        for letter in self.alphabet:
            self.__dict__ [letter] = letter 
    
    def print_table(self):
        '''
        Prints out your table to the screen
        '''
        print ("Substitution Table")
        print ("---")
        for key in self.__dict__.keys():
            print("{} --> {}".format(key, self.__dict__[key]))

    def read_in_table(self, table_file):
        '''
        Reads in a table from a file in the format
        'BACD.....Z'
        '''
        with open(table_file, 'r') as fd:
            table_text = fd.read().replace('\n', '')
        
        if len(table_text) != len(self.alphabet):
            print("Bad table file")
            return
        
        for i in range(0, len(self.alphabet)):
            self.__dict__[self.alphabet[i]] = table_text[i]



def write_line_to_file(line):
    '''
    Writes out any line to scratchpad.txt
    '''
    with open('scratchpad.txt', 'a') as fd:
        # Add two newline characters for clarity
        fd.write(line + '\n' + '\n')


def print_puzzle_stats(puzzletext):
    '''
    Provides stats about the puzzle you may find useful!
    '''
    freq_dict = {}
    length = len(puzzletext)

    # Get frequency
    for c in puzzletext: 
        if c in freq_dict:
            freq_dict[c] += 1
        else:
            freq_dict[c] = 1
    
    # Normalise
    for key in freq_dict.keys():
        freq_dict[key] = freq_dict[key] / length

    # Print
    print("Length : {}".format(length))
    print("Frequency of Characters")
    print("---")

    for key in freq_dict.keys():
        print("{} : {}".format(key, freq_dict[key]))
    
    print ("\n")

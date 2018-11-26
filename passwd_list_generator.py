import re, itertools, sys

class passwd_list_generator():
    """Program used to test the strength of passwords"""
    def __init__(self,filepath, name_passwd_list="password_list.txt"):
        self.names_of_int = [n.strip() for n in open(filepath,'r')]
        ##common separators of words and symbols
        self.separators = ["@","-","?","_","*","%","!","#","/"]
        ##substitution dictionary: words for symbols/numbers
        self.substitution_dictionary = {"a":"@","e":"3","s":"5","i":"1","s":"$","s":"§","e":"&","o":"0"}
        ##main list for pentesting.
        self.passwd_list = open(name_passwd_list,"w",encoding='utf-8')

    def add_dates_numbers(self):
        x = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        for tup in itertools.product(x, repeat=8):
            aux_text = ''
            for n in tup:
                aux_text += n
            self.passwd_list.write(aux_text+'\n')
        self.passwd_list.close()

    def add_words(self):
        for name in self.names_of_int:
            for tup in itertools.product(x, repeat=8):
                aux_text = name
                number = ''
                for n in tup:
                    number += n
                self.passwd_list.write(aux_text+number+'\n')
                for sep in self.separators:
                    self.passwd_list.write(aux_text+sep+number+'\n')
                    self.passwd_list.write(number+sep+aux_text+'\n')

    def add_substitution_words(self):
        substitution_names = []
        for name in self.names_of_int:
            for k,v in self.substitution_dictionary.items():
                substitution_names.append(name.replace(k,v))
        self.names_of_int += substitution_names
        self.names_of_int = set(self.names_of_int)

    def generate_password_list(self):
        self.add_substitution_words()
        self.add_words()
        self.add_dates_numbers()

def main(filepath):
    psswrd = passwd_list_generator(filepath)
    psswrd.generate_password_list()

if __name__ == '__main__':
    main(sys.argv[1])
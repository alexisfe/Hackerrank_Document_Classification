__author__ = 'alexisfe'

from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

f = None
train_data_file = "trainingdata.txt"

def init_input():
    return open(train_data_file)

def read_input():
    return f.readline()
    # return raw_input()

f = init_input()

num_lines = int(read_input())

#Initialize english stopwords
sw = stopwords.words('english')
sbs = SnowballStemmer('english')
doc_dict = dict()

for i in range(0, num_lines):
    text = read_input()
    #All characters to lower case
    text = text.lower()
    #Create a list with all words split by spaces
    text_list = text.split(" ")
    #First word corresponds to the document number
    doc_num = int(text_list.pop(0))
    #Remove stopwords and non-alphanumeric words
    words_list = [j for j in text_list if j not in sw and j.isalnum()]
    #Stem words using a Snowball Stemmer
    words_list = [sbs.stem(j) for j in words_list]

    if doc_num not in doc_dict:
        doc_dict[doc_num] = dict()
    doc_words = doc_dict[doc_num]

    for word in words_list:
        if word in doc_words:
            doc_words[word] = doc_words[word]+1
        else:
            doc_words[word] = 1













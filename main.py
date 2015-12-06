__author__ = 'alexisfe'

import urllib2

from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer

def init_input(path):
    return open(path)

def init_remote_input(remote_path):
    return urllib2.urlopen(remote_path)

def read_input(file):
    return file.readline()

def read_raw_input():
    return raw_input()

def train_classifier(train_file, cv):
    num_lines = int(read_input(train_file))

    #Initialize english stopwords
    sw = stopwords.words('english')
    sbs = SnowballStemmer('english')

    doc_dict = dict()

    for i in range(0, num_lines):
        text = read_input(train_file)
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
            doc_dict[doc_num] = ' '
        doc_words = doc_dict[doc_num]

        doc_dict[doc_num] = doc_words+" "+ ' '.join(words_list)

    sorted_doc_num = sorted(doc_dict.keys())

    print [doc_dict[k] for k in sorted_doc_num]
    np.array(result.items(), dtype=dtype)
    X = cv.fit_transform([doc_dict[k] for k in sorted_doc_num])
    y = sorted_doc_num

    mnb = MultinomialNB()
    mnb.fit(X, y)

    return mnb

def predict(clf, cv, text):
    X = cv.transform(text)
    return clf.predict_proba(X)

train_data_local_path = "trainingdata.txt"
train_data_remote_path = 'https://s3.amazonaws.com/hr-testcases/597/assets/trainingdata.txt'

cv = CountVectorizer()
# train_file = init_remote_input(train_data_remote_path)
train_file = init_input(train_data_local_path)

clf = train_classifier(train_file, cv)
print predict(clf, cv, 'champion products ch approves stock split champion products inc said its board of directors')






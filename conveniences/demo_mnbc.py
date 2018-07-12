#
# demo_spam_classifier.py
#
# Multinomial Naive Bays Classifier.
#
# Based-on:
#
# https://www.udemy.com/data-science-and-machine-learning-with-python-hands-on/
# http://blog.datumbox.com/machine-learning-tutorial-the-naive-bayes-text-classifier/
#

import os
import io
import numpy
from pandas import DataFrame
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

'''
Convenience functions to read the emails and store their messages and
classes in a pandas dataframe.
'''

def readFiles(path):
    for root, dirnames, filenames in os.walk(path):
        for filename in filenames:
            path = os.path.join(root, filename)

            inBody = False
            lines = []
            f = io.open(path, 'r', encoding='latin1')
            for line in f:
                if inBody:
                    lines.append(line)
                elif line == '\n':
                    inBody = True
            f.close()
            message = '\n'.join(lines)
            yield path, message


def dataFrameFromDirectory(path, classification):
    rows = []
    index = []
    for filename, message in readFiles(path):
        rows.append({'message': message, 'class': classification})
        index.append(filename)
    return DataFrame(rows, index=index)

'''
Read the data and store it in a pandas dataframe.
'''

data = DataFrame({'message': [], 'class': []})

data = data.append(dataFrameFromDirectory('../datasets/emails/ham', 'ham'))
data = data.append(dataFrameFromDirectory('../datasets/emails/spam', 'spam'))

'''
We pass an array of messages to vectorizer.fit_transform(), it will convert
each word to a global token and count the occurences across all emails.
'''

vectorizer = CountVectorizer()
counts = vectorizer.fit_transform(data['message'].values)

'''
Now we train a Multinomial Naive Bayes Classifier using the frequencies
obtained from last step. We'll use this variant of the algorithm because
our premise is that spams tend to contain certain words that can easily
identify the nefarious purpose of them.
'''

classifier = MultinomialNB()
targets = data['class'].values
classifier.fit(counts, targets)

'''
Run some examples to test the classifier.
'''

examples = ['Free Viagra now!!!', "Hi Bob, how about a game of golf tomorrow?", "Luke... I'm your father."]

example_counts = vectorizer.transform(examples)
predictions = classifier.predict(example_counts)

print(predictions)

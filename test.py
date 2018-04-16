from nltk.corpus import names
import random
import nltk

def gender_features(word):
    feat = {}
    feat.update({'last_letter': word[-1]})
    sum = 0
    for c in word:
        sum = sum + ord(c)
    feat.update({'first_letter': word[0]})
    feat.update({'hash': sum})


    return feat


names = ([(name, 'male') for name in names.words('male.txt')] + [(name, 'female') for name in names.words('female.txt')])
import random
random.shuffle(names)
train_names = names[1500:]
devtest_names = names[500:1500]
test_names = names[:500]
featuresets = [(gender_features(n), g) for (n,g) in names]
train_set, test_set = featuresets[500:], featuresets[:500]
classifier = nltk.NaiveBayesClassifier.train(train_set)

train_set = [(gender_features(n), g) for (n,g) in train_names]
devtest_set = [(gender_features(n), g) for (n,g) in devtest_names]
test_set = [(gender_features(n), g) for (n,g) in test_names]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print nltk.classify.accuracy(classifier, devtest_set)
errors = []
for (name, tag) in devtest_names:
     guess = classifier.classify(gender_features(name))
     if guess != tag:
         errors.append( (tag, guess, name) )
for (tag, guess, name) in sorted(errors):
     print 'correct=%-8s guess=%-8s name=%-30s' % (tag, guess, name)

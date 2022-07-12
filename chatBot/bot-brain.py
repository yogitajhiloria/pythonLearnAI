from email import message
from pyexpat import model
import random
import json
import pickle
from unittest import result
import numpy as np


import nltk 
from nltk.stem import WordNetLemmatizer


from pkg_resources import to_filename

import tensorflow as tf
from tensorflow.python.keras.models import load_model

lemmatizer = WordNetLemmatizer()

intents = json.loads(open('chatBot/data/training-data.json').read())


words = pickle.load(open('chatBot/data/words.pk1','rb'))
classes = pickle.load(open('chatBot/data/classes.pk1','rb'))

model = load_model('chatbot_model.model')

def clean_up_sentence(sentenc):
    sentenc_word =  nltk.word_tokenize(sentenc)
    sentenc_word = [lemmatizer.lemmatize(word) for word in sentenc_word]
    return sentenc_word


def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)


def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

    results.sort(key = lambda x: x[1],reverse=True)
    retunr_list = []
    for r in results:
        retunr_list.append({'intent': classes[r[0]],'probability': str(r[1])})
    return retunr_list


def get_response(intents_list,intents_json):
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
    return result

print('GO! Bot is running!')

while True:
    message = input("")
    ints = predict_class(message)
    res = get_response(ints, intents)
    print(res)









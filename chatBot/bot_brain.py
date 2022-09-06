import datetime
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

# def clean_up_sentence(sentenc):
#     sentenc_word =  nltk.word_tokenize(sentenc)
#     sentenc_word = [lemmatizer.lemmatize(word) for word in sentenc_word]
#     return sentenc_word


# def bag_of_words(sentence):
#     sentence_words = clean_up_sentence(sentence)
#     bag = [0] * len(words)
#     for w in sentence_words:
#         for i, word in enumerate(words):
#             if word == w:
#                 bag[i] = 1
#     return np.array(bag)


# def predict_class(sentence):
#     bow = bag_of_words(sentence)
#     res = model.predict(np.array([bow]))[0]
#     ERROR_THRESHOLD = 0.25
#     results = [[i,r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

#     results.sort(key = lambda x: x[1],reverse=True)
#     retunr_list = []
#     for r in results:
#         retunr_list.append({'intent': classes[r[0]],'probability': str(r[1])})
#     return retunr_list


def get_response(intents_list,intents_json):
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
    return result

# print('GO! Bot is running!')

# while True:
#     message = input("")
#     ints = predict_class(message)
#     res = get_response(ints, intents)
#     print(res)


class BotAction:
    def clean_message(self,message):
        sentenc_word =  nltk.word_tokenize(message)
        sentenc_word = [lemmatizer.lemmatize(word) for word in sentenc_word]
        return sentenc_word

    def convert_to_array(self,sentence):
        sentence_words = self.clean_message(sentence)
        bag = [0] * len(words)
        for w in sentence_words:
            for i, word in enumerate(words):
                if word == w:
                    bag[i] = 1
        return np.array(bag)

    def predict_action(self,sentence):
        bow = self.convert_to_array(sentence)
        res = model.predict(np.array([bow]))[0]
        ERROR_THRESHOLD = 0.25
        results = [[i,r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
        results.sort(key = lambda x: x[1],reverse=True)
        retunr_list = []
        for r in results:
            retunr_list.append({'intent': classes[r[0]],'probability': str(r[1])})
        return retunr_list

    def get_response(self,actions_list):
        tag = actions_list[0]['intent']
        list_of_intents = intents['intents']
        for i in list_of_intents:
            if i['tag'] == tag:
                result = random.choice(i['responses'])
                break
        return result

    def process_asked_input(self,message):
        commandsPredicted =  self.predict_action(message)
        command = commandsPredicted[0]['intent']
        output_message = self.get_response(commandsPredicted)
        if command is None:
            return { "message": 'Got nothing', "actiontag": None } 

        if 'play' in command:
            song = command.replace('play', '')
            return  { "message": 'playing ' + song, "actiontag": 'play' } 
            # talk('playing ' + song)
            # pywhatkit.playonyt(song)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            return  { "message": output_message.format(time), "actiontag": 'time' } 
            # talk('Current time is ' + time)
        elif 'search' in command:
            person = message.replace('search', '')
            return  { "message": person, "actiontag": 'search'  } 
        elif 'date' in command:
            return  { "message": 'sorry, I have a headache', "actiontag": 'date' } 
            # talk('sorry, I have a headache')
        elif 'myself' in command:
            # talk('I am in a relationship with wifi')
            return  { "message": 'I am in a relationship with wifi', "actiontag": 'myself' } 
        elif command is not None:
            # talk(pyjokes.get_joke())
            return  { "message": output_message, "actiontag": command } 
        else:
            return  { "message": 'Please try again', "actiontag": None } 
            # talk('Please say the command again.')


class TextBot:
    def start(self,bot_config):
        print('starting text bot...')
        print('type now...')
        self.bot_setting = bot_config
    
    def get_user_input(self):
        message = input("")
        return message

    def process_output_message(self,message):
        print(message)
        









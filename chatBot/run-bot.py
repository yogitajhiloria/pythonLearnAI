from argparse import Action
from email import message
import sys
import time
import datetime
import pywhatkit
import wikipedia
import pyjokes


from click import command
from bot_brain import TextBot, BotAction
from audio_sys import AudioBot
from config import default_config, BotMode


bot_config = default_config

mode = 1

def run_bot():
    bot =  initlize()
    action = BotAction()
    while True:
        try:
            asked_input = bot.get_user_input()
            if asked_input is None:
                continue
            result = action.process_asked_input(asked_input)
            updated_result = do_extra_actions(result)
            if 'switch' in result['actiontag']:
                bot =  initlize()
            input = updated_result if updated_result is not None else result['message']
            bot.process_output_message(input)
            time.sleep(10)
        except KeyboardInterrupt:
            # quit
            sys.exit()

def initlize():
    if bot_config.mode is BotMode.TEXT:
        bot = TextBot()
    else:
        bot = AudioBot()
    bot.start(bot_config)    
    return bot    

def process_input(asked_input):
    pass

def do_extra_actions(action):
    print(action)
    command = action['actiontag']
    todo =  action['message'] 
    if 'play' in command:
        pywhatkit.playonyt(todo)
    elif 'search' in command:
        info = wikipedia.summary(todo, 1)
        return info
    elif 'joke' in command:
        return pyjokes.get_joke()
    elif 'name' in command:
        return todo.format(bot_config.name)
    elif 'switch' in command:
        bot_config.mode = 1 if bot_config.mode is BotMode.AUDIO else 2
        current_bot = 'text bot' if bot_config.mode is BotMode.TEXT else 'audio bot'
        return todo.format(current_bot)
    


run_bot()

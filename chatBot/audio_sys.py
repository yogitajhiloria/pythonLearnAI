import pprint
import traceback
from click import command
import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes
import time





pp = pprint.PrettyPrinter(indent=4)

def talk(text):
    engine.say(text)
    engine.runAndWait()


# talk('why are you not working in other mode')

# def take_command():
#     try:
#         with sr.Microphone() as source:
#             print('listening...')
#             voice = listener.listen(source)
#             command = listener.recognize_google(voice)
#             command = command.lower()
#             if 'yogita' in command:
#                 command = command.replace('yogita', '')
#                 return command
#             else:
#                 print('Can"t recongnise it...')
#                 print(command)
        
#     except BaseException as err:
#          print(f"Unexpected {err=}, {type(err)=}")
#          print(err)
#          pass
    

# def run_alexa():
#     command = take_command()
#     if command is None:
#         print('Got nothing')
#         return
#     print(command)
#     if 'play' in command:
#         song = command.replace('play', '')
#         talk('playing ' + song)
#         pywhatkit.playonyt(song)
#     elif 'time' in command:
#         time = datetime.datetime.now().strftime('%I:%M %p')
#         talk('Current time is ' + time)
#     elif 'who the heck is' in command:
#         person = command.replace('who the heck is', '')
#         info = wikipedia.summary(person, 1)
#         print(info)
#         talk(info)
#     elif 'date' in command:
#         talk('sorry, I have a headache')
#     elif 'are you single' in command:
#         talk('I am in a relationship with wifi')
#     elif 'joke' in command:
#         talk(pyjokes.get_joke())
#     else:
#         talk('Please say the command again.')


# while True:
#     try:
#     # DO THINGS
#         run_alexa()
#         time.sleep(10)
#     except KeyboardInterrupt:
#     # quit
#         sys.exit()
    
class AudioBot:
    
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 100)
    
    def start(self,bot_config):
        # self.listener = sr.Recognizer()
        # self.engine = pyttsx3.init()
        # self.voices = engine.getProperty('voices')
        # self.engine.setProperty('voice', voices[1].id)
        self.speak('Starting Bot Hello how can i help you')
        self.bot_setting = bot_config
    
    def get_user_input(self):
        # pp.pprint(sr.Microphone.list_microphone_names())
        # pprint(sr.Microphone.list_microphone_names())
        command_final = None
        try:
            # device_index=0
            listener = sr.Recognizer()
            with sr.Microphone(device_index=1) as source:
                # audio = source.pyaudio_module.PyAudio()
                # # for i in range(audio.get_device_count()):
                # #     device_info = audio.get_device_info_by_index(i)
                # #     print(device_info)
                # devicedetails = audio.get_device_info_by_index(0)
                # defaultdevicedetails = audio.get_default_input_device_info()
                # print(devicedetails)
                # print(defaultdevicedetails)
                # print(source.device_index)

                listener.adjust_for_ambient_noise(source, duration = 1)
                print('listening...')
                voice = listener.listen(source)
                print(voice)
                print(type(voice))
                # print('got the voice')
                command = listener.recognize_google(voice)
                # print(f'got the comand {command}')
                command = command.lower()
                if self.bot_setting.name in command:
                    command_final = command.replace(self.bot_setting.name, '')
                    
                else:
                    print(f'Can"t recongnise it... Say the name {self.bot_setting.name} got this message instead: {command}')  
        except KeyboardInterrupt:
            # quit
            raise KeyboardInterrupt("Date provided can't be in the past")
        except BaseException as err:
            print(f"Unexpected {err=}, {type(err)=}")
            print(traceback.format_exc())
        finally:
            pass
        return command_final
    
    def process_output_message(self,message):
        self.speak(message)
    
    def speak(self,message):
        self.engine.say(message)
        self.engine.runAndWait()



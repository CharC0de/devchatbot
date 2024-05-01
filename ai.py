
# for speech-to-text
import speech_recognition as sr
# for text-to-speech
from gtts import gTTS
# for language model
import transformers
import os
import time
# for data
import os
import datetime
import numpy as np
# Building the AI


class ChatBot():
    def __init__(self, name):
        print("----- Starting up", name, "-----")
        self.name = name
        self.text = ''

    @staticmethod
    def reply(text):
        return text

    @staticmethod
    def action_time():
        return datetime.datetime.now().time().strftime('%H:%M')

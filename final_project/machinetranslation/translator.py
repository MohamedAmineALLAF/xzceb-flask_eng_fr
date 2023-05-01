"""
This module provides functions for translating text between English and French using the IBM Watson.
"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
lt = LanguageTranslatorV3(
    version='2022-05-01',
    authenticator=authenticator
)

lt.set_service_url(url)

def english_to_french(english_text):
        
    lt.set_service_url(url)
    translation = lt.translate(
        text=english_text,
        source='en',
        target='fr'
    ).get_result()
    french_text = translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
        
    translation = lt.translate(
        text=french_text,
        source='fr',
        target='en'
    ).get_result()
    english_text = translation['translations'][0]['translation']
    return english_text

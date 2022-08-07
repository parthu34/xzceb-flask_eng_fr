'''Import Modules'''
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(url)

def english_to_french(english_text):
    '''Method to translate English text to French'''
    translation = language_translator.translate(
    english_text,
    model_id='en-fr').get_result()
    french_text = translation.get('translations')
    return french_text[0]['translation']

def french_to_english(french_text):
    '''Method to translate French text to English'''
    translation = language_translator.translate(
    french_text,
    model_id='fr-en').get_result()
    english_text = translation.get('translations')
    return english_text[0]['translation']

from deep_translator import MyMemoryTranslator as dt 

def english_to_french (english_text):
    #write the code here
    frenchText = dt (source='en-GB' target='fr-FR').translate(english_text)
    return french_text

def french_to_english (french_text):
    #write the code here
    englishText = dt(source='fr-FR', target='en-GB').translate(french_text)
    return english_text
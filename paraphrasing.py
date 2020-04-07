from googletrans import Translator
import json

translator=Translator()



from googletrans import Translator
from grammarbot import GrammarBotClient
import json

translator=Translator()

in_text=input("Please enter text")

def Paraphrasing(in_text):
    phrased = []
    for i in ['ko', 'ja', 'el', 'fr', 'tl', 'ar', 'ht','af', 'sq', 'am']:
        par_text = translator.translate(in_text, dest=i).text
        phrased.append(translator.translate(par_text, dest='en').text.capitalize())
    t = [i for i in phrased if i.lower() != in_text.lower()]
    if not list(set(t)):
        dictionary={'paraphrased':['No possible phrases']}
        return json.dumps(dictionary)
    else:
        dictionary={'paraphrased':list(set(t))}
        return json.dumps(dictionary)    



x=Paraphrasing(in_text)

print(x)
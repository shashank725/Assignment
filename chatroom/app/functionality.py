import json
import nltk
from nltk import pos_tag, word_tokenize

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

async def analyze_message(message):
    tokens = word_tokenize(message)
    pos_tags = pos_tag(tokens)

    figures_of_speech = {
        'Adjective': [],
        'Adverb': [],
        'Conjunction': [],
        'Determiner': [],
        'Noun': [],
        'Number': [],
        'Preposition': [],
        'Pronoun': [],
        'Verb': [],
    }

    for word, pos in pos_tags:
        if pos.startswith('JJ'):
            print()
            figures_of_speech['Adjective'].append(word)
        elif pos.startswith('RB'):
            figures_of_speech['Adverb'].append(word)
        elif pos.startswith('CC'):
            figures_of_speech['Conjunction'].append(word)
        elif pos.startswith('DT'):
            figures_of_speech['Determiner'].append(word)
        elif pos.startswith('NN'):
            figures_of_speech['Noun'].append(word)
        elif pos.startswith('CD'):
            figures_of_speech['Number'].append(word)
        elif pos.startswith('IN'):
            figures_of_speech['Preposition'].append(word)
        elif pos.startswith('PRP'):
            figures_of_speech['Pronoun'].append(word)
        elif pos.startswith('VB'):
            figures_of_speech['Verb'].append(word)

    return figures_of_speech
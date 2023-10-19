import requests
from bs4 import BeautifulSoup
import sys


# creating user-defined exception in order user input wrong language


class WrongWordError(Exception):
    def __init__(self, word):
        self.word = word

    def __str__(self):
        message = 'Sorry, unable to find {}'.format(self.word)
        return message


class WrongLanguageError(Exception):
    def __init__(self, language):
        self.language = language

    def __str__(self):
        message = "Sorry, the program doesn't support {}".format(self.language)
        return message

# creating variables from user's input

args = sys.argv  # we get the list of arguments
first_lang = args[1]  # convert arguments to float
second_lang = args[2]
target_word = args[3]

# creating dictionary with supported languages
lang = ['Arabic', 'German', 'English', 'Spanish', 'French', 'Hebrew', 'Japanese', 'Dutch', 'Polish', 'Portuguese',
        'Romanian', 'Russian', 'Turkish']


def translate_all_lang(first_l, word):
    file = open('{}.txt'.format(word), 'w', encoding='utf-8')
    for language in lang:
        if language.lower() != first_l:
            headers = {'User-Agent': 'Mozilla/5.0'}
            translations = []
            sentences = []
            url = 'https://context.reverso.net/translation/{}-{}/{}'.format(first_l, language.lower(), word)
            request = requests.get(url, headers=headers)
            if 400 <= request.status_code <= 499:
                raise WrongWordError(target_word)
            soup = BeautifulSoup(request.content, 'html.parser')
            data_words = soup.find('span', {'class': 'display-term'})
            for data in data_words:
                translations.append(data.string)
            data_sentence = soup.find_all('div', {'class': 'example'})
            for sentence in data_sentence:
                sentences.append(sentence.text)
            file.write('{} Translations:'.format(language).title() + '\n')
            file.write(translations[0] + '\n')
            file.write('{} Examples:'.format(language).title() + '\n')
            file.write(sentences[0].replace('          ', '') + '\n')

    file.close()
    file = open('{}.txt'.format(word), 'r', encoding='utf-8')
    print(file.read())
    file.close()


def translate_exact_lang(first_l, second_l, word):
    file = open('{}.txt'.format(word), 'w', encoding='utf-8')
    headers = {'User-Agent': 'Mozilla/5.0'}
    translations = []
    sentences = []
    url = 'https://context.reverso.net/translation/{}-{}/{}'.format(first_l, second_l, word)
    request = requests.get(url, headers=headers)

    if 400 <= request.status_code <= 499:
        raise WrongWordError(target_word)
    soup = BeautifulSoup(request.content, 'html.parser')
    data_words = soup.find_all('span', {'class': 'display-term'})
    for data in data_words:
        translations.append(data.string)
    data_sentence = soup.find_all('div', {'class': 'example'})

    for sentence in data_sentence:
        sentences.append(sentence.text)

    file.write('{} Translations:'.format(second_lang).title() + '\n')
    file.write(translations[0] + '\n')
    file.write('{} Examples:'.format(second_lang).title() + '\n')
    file.write(sentences[0].replace('          ', '') + '\n')
    file.close()

    file = open('{}.txt'.format(word), 'r', encoding='utf-8')
    print(file.read())
    file.close()


try:
    if first_lang.capitalize() not in lang:
        raise WrongLanguageError(first_lang)
    if second_lang.capitalize() not in lang and second_lang != 'all':
        raise WrongLanguageError(second_lang)
    if second_lang == 'all':
        translate_all_lang(first_lang, target_word)
    else:
        translate_exact_lang(first_lang, second_lang, target_word)

except WrongLanguageError as error:
    print(error)
except WrongWordError as err:
    print(err)

import re
from bs4 import BeautifulSoup
import contractions
import underthesea

def separate_text(text):
    text = re.split(r'(?<=[.!?]) +', text)
    return text

def separate_word(text):
    word = re.findall(r'\b\w+\b', text)
    return word

def contraction(text):
    text = BeautifulSoup(text, "html.parser").get_text()
    text = contractions.fix(text)
    text.replace(" '", "'")
    return text

def normalize_punctuation_spacing(text):
    text = re.sub(r'\n', ' ', text)
    text = re.sub(r'([.,!?;(){}\[\]])', r' \1 ', text)
    text = re.sub(r'\s{2,}', ' ', text)
    text = text.strip()
    return text

def word_tokenize_vn(text):
    return underthesea.word_tokenize(text, format="text")

__all__ = [
    'separate_text',
    'separate_word',
    'contraction',
    'normalize_punctuation_spacing',
    'word_tokenize_vn'
]
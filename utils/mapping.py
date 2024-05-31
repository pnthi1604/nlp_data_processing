import re
from bs4 import BeautifulSoup
import contractions
import underthesea
import numpy as np
import pandas as pd

def separate_text(text):
    text = re.split(r'(?<=[.!?]) +', text)
    return text

def separate_text_with_min_max_len(text, min_len, max_len):
    text = re.split(r'(?<=[.!?]) +', text)
    text = [t for t in text if len(t.split()) <= max_len]

    sentences = []
    i = 0
    while i < len(text):
        sent = text[i]
        for j in range(i + 1, len(text)):
            if len(sent.split()) + len(text[j].split()) <= max_len:
                sent = sent.strip() + ' ' + text[j].strip() + ' . '
            else:
                i = j - 1
                break
        i += 1
        if len(sent.split()) >= min_len:
            sentences.append(sent.strip())
    return sentences

def separate_word(text):
    word = re.findall(r'\b\w+\b', text)
    return word

def contraction(text, lang="vi"):
    text = BeautifulSoup(text, "html.parser").get_text()
    if lang == "en":
        text = contractions.fix(text)
        text.replace(" '", "'")
    return text

def normalize_punctuation_spacing(text):
    text = re.sub(r'\n', ' ', text)
    text = re.sub(r'([.,!?;(){}\[\]])', r' \1 ', text)
    text = re.sub(r'\s{2,}', ' ', text)
    text = text.strip()
    return str(text)

def word_tokenize_vn(text):
    return underthesea.word_tokenize(text, format="text")

__all__ = [
    'separate_text',
    'separate_word',
    'contraction',
    'normalize_punctuation_spacing',
    'word_tokenize_vn',
    'separate_text_with_min_max_len',
]
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
        sents = [text[i]]
        sum_len = len(text[i].split())
        j = i + 1
        i = j
        while j < len(text):
            if sum_len + len(text[j].split()) <= max_len:
                sents.append(text[j])
                sum_len += len(text[j].split())
                j += 1
                i = j
            else:
                i = j
                break
        if sum_len >= min_len:
            sentences.append(' '.join(sents))
    return sentences

def separate_word(text):
    word = re.findall(r'\b\w+\b', text)
    return word

def contraction(text, lang="vi"):
    text = BeautifulSoup(text, "html.parser").get_text()
    text.replace(" '", "'")
    text = contractions.fix(text)
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
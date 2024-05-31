import pandas as pd

def condition_length_with_tokenizer(
    tokenizer,
    text,
    min_len_token,
    max_len_token,
):
    if type(text) != str:
        return False
    text = tokenizer.encode(text).ids
    return len(text) >= min_len_token and len(text) <= max_len_token

def condition_non_number_character(text):
    if type(text) != str:
        return False
    if any(char.isdigit() for char in text):
        return False
    return True

def condition_min_max_length(text, min_len, max_len):
    if type(text) != str:
        return False
    return len(text.split()) >= min_len and len(text.split()) <= max_len

__all__ = [
    "condition_length_with_tokenizer",
    "condition_non_number_character",
    "condition_min_max_length",
]
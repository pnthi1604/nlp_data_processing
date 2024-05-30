import pandas as pd

def condition_length_with_tokenizer(
    tokenizer,
    text,
    min_len_token=6,
    max_len_token=100,
):
    text = tokenizer.encode(text)
    if len(text.ids) < min_len_token:
        return False
    if len(text.ids) > max_len_token:
        return False
    return True

def condition_non_number_character(text):
    if any(char.isdigit() for char in text):
        return False
    return True

__all__ = [
    "condition_length_with_tokenizer",
    "condition_non_number_character",
]
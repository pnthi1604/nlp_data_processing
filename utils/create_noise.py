import random
import numpy as np

# const variable
TOKEN_MASKING = 'token_masking'
TOKEN_DELETION = 'token_deletion'
DOCUMENT_ROTATION = 'document_rotation'
TEXT_INFILLING = 'text_infilling'

def random_pos(length, ratio=0.15):
    length_pos = int(length * ratio)
    pos = random.sample(range(length), length_pos)
    return pos

def token_masking(text, ratio=0.15):
    words = text.split()
    length = len(words)

    mask_positions = random_pos(
        length=length,
        ratio=ratio
    )

    masked_words = words.copy()
    for pos in mask_positions:
        masked_words[pos] = '<mask>'

    masked_text = ' '.join(masked_words)
    return masked_text.strip()

def token_deletion(text, ratio=0.15):
    words = text.split()
    length = len(words)

    mask_positions = random_pos(
        length=length,
        ratio=ratio
    )

    masked_words = words.copy()
    for pos in mask_positions:
        masked_words = masked_words[:pos] + masked_words[pos+1:]

    masked_text = ' '.join(masked_words)
    return masked_text.strip()

def document_rotation(text, ratio=None):
    words = text.split()
    length = len(words)
    pos = random.randint(0, length-1)

    rotated_words = words[pos:] + words[:pos]
    rotated_text = ' '.join(rotated_words)
    return rotated_text.strip()

def text_infilling(text, lambd=3, ratio=0.15):
    words = text.split()
    length = len(words)
    num_masks = max(1, int(length * ratio))

    mask_positions = []
    current_length = 0

    while current_length < length - 1 and len(mask_positions) < num_masks:
        mask_length = min(length - current_length, max(1, int(np.random.poisson(lambd))))
        if length - current_length - mask_length < 1:
            break
        start = random.randint(current_length + 1, length - mask_length)
        end = start + mask_length
        mask_positions.append((start, end))
        current_length = end

    masked_words = words.copy()
    for start, end in mask_positions:
        if start >= end:
            masked_words = masked_words[:start] + ['<mask>'] + masked_words[start:]
            continue
        masked_words[start:end] = ['<mask>']

    masked_text = ' '.join(masked_words)
    return masked_text

__all__ = [
    "token_masking",
    "token_deletion",
    "document_rotation",
    "text_infilling",
    "TOKEN_MASKING",
    "TOKEN_DELETION",
    "DOCUMENT_ROTATION",
    "TEXT_INFILLING",
]
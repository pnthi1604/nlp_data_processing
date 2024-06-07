import random
import numpy as np

# const variable
TOKEN_MASKING = 'token_masking'
TOKEN_DELETION = 'token_deletion'
DOCUMENT_ROTATION = 'document_rotation'
TEXT_INFILLING = 'text_infilling'
SENTENCE_PERMUTATION = 'sentence_permutation'

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

def sentence_permutation(text, ratio=None):
    sentences = text.split('.')
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    random.shuffle(sentences)
    permuted_text = '. '.join(sentences)
    return permuted_text.strip()

def multi_random_choice_min(left, right, num=10):
    min_choice = right
    while num > 0:
        choice = random.randint(left, right)
        min_choice = min(min_choice, choice)
        num -= 1
    return min_choice

def text_infilling(text, lambd=3, ratio=0.15):
    words = text.split()
    length = len(words)
    num_masks = max(1, int(length * ratio))

    mask_positions = []
    cur_pos = 0
    sum_length = 0

    queue_positions = []
    while length - (num_masks - sum_length) > 0 and sum_length <= num_masks and length - cur_pos > 0:
        mask_length = min(length - cur_pos, max(1, int(np.random.poisson(lambd))))
        if mask_length == 0:
            queue_positions.append(cur_pos + len(queue_positions))
            cur_pos += 2
            continue
        if  length - (num_masks - sum_length + mask_length) < cur_pos + 1:
            break
        start = multi_random_choice_min(
            left=cur_pos + 1,
            right=length - (num_masks - sum_length + mask_length), 
            num=10
        )
        end = start + mask_length
        if end > length:
            break
        mask_positions.append((start, end))
        sum_length += mask_length
        cur_pos = end + 1

    masked_words = words.copy()
    for start, end in mask_positions:
        if start >= end:
            continue
        masked_words[start:end] = ['<mask>']

    for start in queue_positions:
        masked_words = masked_words[:start] + ['<mask>'] + masked_words[start:]

    masked_text = ' '.join(masked_words)
    return masked_text

__all__ = [
    "token_masking",
    "token_deletion",
    "document_rotation",
    "text_infilling",
    "sentence_permutation",
    "TOKEN_MASKING",
    "TOKEN_DELETION",
    "DOCUMENT_ROTATION",
    "TEXT_INFILLING",
    "SENTENCE_PERMUTATION",
]
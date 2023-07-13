"""
Shared functions, especially for building regular expressions.
"""
from pathlib import Path


def _clean_word(orig_word):
    """Clean tokens of word, and regexify"""
    word = orig_word.replace('5', r'\d+')  # placeholder for any digit
    word = word.replace('her', r'(?:her|hi[sm]|the(?:ir|m))')
    word = word.replace('she', r'(?:s?he|they)')
    word = word.replace('.', r'\W?')  # period
    if len(word) != len(orig_word):
        pass  # already made needed changes
    if len(word) > 4 and word.endswith('ing'):
        word = rf'{word[:-3]}\w*'
    elif len(word) > 4 and (word.endswith('ed') or word.endswith('al')):
        word = rf'{word[:-2]}\w*'
    elif word.endswith('s'):
        word = rf'{word}?'
    elif word.endswith("n't"):  # expand n't
        word = rf'{word[:-3]}(?:n\Wt|\W?not)'
    elif len(word) > 3:
        word = rf'{word}\w*'
    word = word.replace("'", r'\W')  # apostrophe
    return word


def clean_phrase(phrase):
    """Clean multiple, space-separated words and input into a regex."""
    phrase = phrase.replace('-', ' ')
    return r'\W*'.join(_clean_word(word) for word in phrase.split())


def load_vocab_from_file(filename: str):
    """Load vocab from filename as a set"""
    with open(Path(__file__).parent / 'data' / f'{filename}.txt', encoding='utf8') as fh:
        return {line.strip() for line in fh}


def make_spacy_pattern(phrase, clean=False):
    if clean:
        ...
    else:
        return []


def create_pattern_from_set(data: set, clean=False):
    func = clean_phrase if clean else lambda x: x
    pattern = '|'.join(func(datum) for datum in data)
    return rf'\b(?:{pattern})\b'

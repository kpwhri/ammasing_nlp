"""
Regular expressions patterns for locating side effects.
"""
import re
from pathlib import Path

_SIDE_EFFECTS = set()
_SIDE_EFFECTS_RX = None


def get_ses():
    if not _SIDE_EFFECTS:
        with open(Path(__file__).parent / 'data' / 'sideeffects.txt', encoding='utf8') as fh:
            for line in fh:
                _SIDE_EFFECTS.add(line.strip())
                print(line)
    return _SIDE_EFFECTS


def _clean_word(orig_word):
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


def _clean_se(se):
    se = se.replace('-', ' ')
    return r'\W*'.join(_clean_word(word) for word in se.split())


def get_se_rx():
    global _SIDE_EFFECTS_RX
    if not _SIDE_EFFECTS_RX:
        ses = '|'.join(_clean_se(se) for se in get_ses())
        _SIDE_EFFECTS_RX = rf'\b(?:{ses})\b'
    return _SIDE_EFFECTS_RX


SE_PAT = re.compile(
    rf'(?:'
    rf'{get_se_rx()}'
    rf')',
    re.I
)

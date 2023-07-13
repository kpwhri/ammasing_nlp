"""
Regular expressions patterns for locating status (i.e., negation) terms.
"""
import re

from ammasing_nlp.categories.utils import load_vocab_from_file, create_pattern_from_set

_STATUS_TERMS = None
_STATUS_TERMS_RX = None


def get_status():
    """Get side effects"""
    global _STATUS_TERMS
    return _STATUS_TERMS or (_STATUS_TERMS := load_vocab_from_file('statusterms'))


def get_status_rx():
    """Get pattern with loaded side effects"""
    global _STATUS_TERMS_RX
    return _STATUS_TERMS_RX or (_STATUS_TERMS_RX := create_pattern_from_set(get_status(), clean=True))


def get_status_spacy():
    pass


STATUS_PAT = re.compile(
    rf'(?:'
    rf'{get_status_rx()}'
    rf')',
    re.I
)

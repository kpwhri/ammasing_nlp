"""
Regular expressions patterns for locating side effects.
"""
import re

from ammasing_nlp.categories.utils import load_vocab_from_file, create_pattern_from_set

_SIDE_EFFECTS = None
_SIDE_EFFECTS_RX = None


def get_ses():
    """Get side effects"""
    global _SIDE_EFFECTS
    return _SIDE_EFFECTS or (_SIDE_EFFECTS := load_vocab_from_file('sideeffects'))


def get_se_rx():
    """Get pattern with loaded side effects"""
    global _SIDE_EFFECTS_RX
    return _SIDE_EFFECTS_RX or (_SIDE_EFFECTS_RX := create_pattern_from_set(get_ses(), clean=True))


SE_PAT = re.compile(
    rf'(?:'
    rf'{get_se_rx()}'
    rf')',
    re.I
)

import re

from ammasing_nlp.categories.utils import load_vocab_from_file, create_pattern_from_set

_MEDICATIONS = set()
_MEDS_RX = None


def get_meds():
    """Retrieve medication names"""
    global _MEDICATIONS
    return _MEDICATIONS or (_MEDICATIONS := load_vocab_from_file('medications'))


def get_meds_rx():
    """Get pattern for medications"""
    global _MEDS_RX
    return _MEDS_RX or (_MEDS_RX := create_pattern_from_set(get_meds()))


MEDICATION_PAT = re.compile(
    rf'\b(?:'
    rf'{get_meds_rx()}'
    rf')\b',
    re.I
)

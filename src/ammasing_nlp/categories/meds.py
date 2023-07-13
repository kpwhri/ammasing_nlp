import re

from ammasing_nlp.categories.utils import load_vocab_from_file, create_pattern_from_set

_MEDICATIONS = set()
_MEDS_RX = None

# generic names like 'meds' and 'medications'
_GEN_MEDICATIONS = set()
_GEN_MEDS_RX = None

_ALL_MEDS_RX = None


def get_meds():
    """Retrieve medication names"""
    global _MEDICATIONS
    return _MEDICATIONS or (_MEDICATIONS := load_vocab_from_file('medications'))


def get_meds_rx():
    """Get pattern for medications"""
    global _MEDS_RX
    return _MEDS_RX or (_MEDS_RX := create_pattern_from_set(get_meds()))


def get_generic_meds():
    global _GEN_MEDICATIONS
    return _GEN_MEDICATIONS or (_GEN_MEDICATIONS := load_vocab_from_file('genericmed'))


def get_generic_meds_rx():
    global _GEN_MEDS_RX
    return _GEN_MEDS_RX or (_GEN_MEDS_RX := create_pattern_from_set(get_generic_meds()))


def get_all_med_mentions():
    global _ALL_MEDS_RX
    return _ALL_MEDS_RX or (_ALL_MEDS_RX := create_pattern_from_set(get_meds() | get_generic_meds()))


MEDICATION_PAT = re.compile(
    rf'\b(?:'
    rf'{get_meds_rx()}'
    rf')\b',
    re.I
)

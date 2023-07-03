import re
from pathlib import Path

_MEDICATIONS = set()
_MEDS_RX = None


def get_meds():
    """Retrieve medication names"""
    if not _MEDICATIONS:
        with open(Path(__file__).parent / 'data' / 'medications.txt', encoding='utf8') as fh:
            for line in fh:
                _MEDICATIONS.add(line.strip())
    return _MEDICATIONS


def get_meds_rx():
    global _MEDS_RX
    if not _MEDS_RX:
        meds = '|'.join(get_meds())
        _MEDS_RX = rf'\b(?:{meds})\b'
    return _MEDS_RX


MEDICATION_PAT = re.compile(
    rf'\b(?:'
    rf'{get_meds_rx()}'
    rf')\b',
    re.I
)

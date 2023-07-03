import re

from ammasing_nlp.categories.utils import load_vocab_from_file, create_pattern_from_set

_SIDER = set()
_SIDER_RX = None


def get_sider():
    """Retrieve medication names"""
    global _SIDER
    return _SIDER or (_SIDER := load_vocab_from_file('sider'))


def get_sider_rx():
    """Get pattern for medications"""
    global _SIDER_RX
    return _SIDER_RX or (_SIDER_RX := create_pattern_from_set(get_sider(), clean=True))


SIDER_PAT = re.compile(
    rf'\b(?:'
    rf'{get_sider_rx()}'
    rf')\b',
    re.I
)

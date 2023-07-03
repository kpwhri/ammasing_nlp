"""
Patterns for detecting problem free use.
"""
import re

from ammasing_nlp.categories.meds import get_meds_rx
from ammasing_nlp.categories.shared import really, med_pre_filler

not_had = r'(?:ha[sd] not|not ha[sd])'
side_effects = r'(?:(?:side-)?effects?|s\.?e\.?s?|problems?|difficult\w*)'

doing_well = (
    rf'(?:(?:doing|done|did|does|tolerat\w*|work\w*|feel\w*)'
    rf'\s*(?:(?:{really}|it|the|{get_meds_rx()}) )*(?:well|good|fine))'
)
tolerates = rf'(?:tolerat\w+ (?:{med_pre_filler} )*{get_meds_rx()}|it|well\Wtolerated)'
no_ses = (
    rf'\b(?:{not_had}|den[yi]\w*|not?|w/o|without)'
    rf'\s*(?:(?:any|negative|adverse|observed|significant|side|med\w*|drug|apparent|experienc\w*)\s*)*{side_effects}'
)
agreeable = r'\b(agreeable to (?:remain|stay)\w*)\b'
magic = r'(?:magic)'

PFU_PAT = re.compile(
    rf'\b(?:'
    rf'{doing_well}'
    rf'|{no_ses}'
    rf'|{agreeable}'
    rf'|{tolerates}'
    rf'|{magic}'
    rf')\b',
    re.I
)

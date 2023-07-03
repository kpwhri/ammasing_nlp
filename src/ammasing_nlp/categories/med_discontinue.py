"""
Detecting medication discontinuation
"""
import re

from ammasing_nlp.categories.meds import get_meds_rx
from ammasing_nlp.categories.shared import doesnt, cant, med_pre_filler, med_post_filler, wont

discontinue = r'\b(?:d/?c(e?d)?|discontinu\w+|stop\w*|prohibit\w*' \
              rf'|(?:unable to|not|no sense in|{wont}|{wont} be) continu\w*' \
              r'|(?:went|go|get|hold) off|no longer tak\w*|off|quit\w*)\b'
taper = r'\b(?:taper\w*|wean\w*|decreas\w+|reduc\w+)\b'
refuse = r'\b(?:(?:refus\w+|will not|not been)\s*(?:to take|tak\w+))\b'
discomfort = rf'\b(?:uncomfortable|{doesnt} like|dislikes?)\b'
tolerate = rf'\b(?:{doesnt}|{cant}|trouble|difficulty|not) tolerat\w*'
allergic = r'add\w* to allergy list'

# derived
discontinue_med = rf'\bd\b (?:{med_pre_filler} )*{get_meds_rx()}'
med_discontinue = rf'(?:'

discontinue_pat = (
    rf'(?:'
    rf'{discontinue}'
    rf'|{taper}'
    rf'|{refuse}'
    rf'|{discomfort}'
    rf'|{tolerate}'
    rf'|{allergic}'
    rf')'
)
DISCONTINUE_PAT = re.compile(
    rf'(?:'
    rf'{discontinue_pat}'
    rf'|{discontinue_med}'
    rf')',
    re.I
)

MED_DISCONTINUE_PAT = re.compile(
    rf'{discontinue_pat} (?:{med_pre_filler} )*{get_meds_rx()}'
    rf'|{get_meds_rx()} (?:{med_post_filler} )*{discontinue_pat}'
    rf'|{discontinue_med}'
)

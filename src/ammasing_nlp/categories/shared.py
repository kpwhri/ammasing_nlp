"""
Shared regular expressions tidbits.
"""

doesnt = r'(?:did not|does not|doesn\'t|didn\'t)'
cant = r'(?:could not|can ?not|can\'t|couldn\'t)'
wont = r'(?:will not|would not|won\'t|wouldn\'t)'
not_taking = r'(?:no longer|not) (?:tak\w*|us\w*)\b'
med_pre_filler = r'\b(?:use of|using|her|his|their|the|usage|eventually|them|from' \
                 r'|this|\d+mg|mg|\d+|of|side|effects?|any|more|tak\w*|further)\b'
med_post_filler = r'(?:was)'

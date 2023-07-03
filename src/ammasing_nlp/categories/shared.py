"""
Shared regular expressions tidbits.
"""

doesnt = r'(?:did not|does not|doesn\'t|didn\'t)'
cant = r'(?:could not|can ?not|can\'t|couldn\'t)'
wont = r'(?:will not|would not|won\'t|wouldn\'t)'
not_taking = r'(?:no longer|not) (?:tak\w*|us\w*)\b'
really = r'(?:very|really|quite)'

# filler terms appearing around medications
med_pre_filler = r'\b(?:use|on|using|her|his|the(?:ir|m)|the|usage|eventually|from' \
                 r'|this|\d+mg|mg|\d+|of|side|effects?|any|more|tak\w*|further|with)\b'
med_post_filler = r'(?:was)'

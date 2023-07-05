import re

from nlpakki.feat.ctxt import FeatureFunction

SECTION_SPLITTER = re.compile(
    r'(?:(?P<plan>P[LANlan]*)|'
    r'(?P<subj>S[UBJECTIVubjectiv]*)|'
    r'(?P<obj>O[BJECTIVbjectiv]*)|'
    r'(?P<asm>A[SEMNTsemnt]*)):'
)

FEATURE_FUNCTIONS = [
    (
        'med_in_sentence',
        FeatureFunction().has_token_in_sentence,
        {
            'kind': 'Medication'
        }
    ),
    (
        'nearby_se',
        FeatureFunction().has_token_in_sentence,
        {
            'kind': 'Side_Effect',
        }
    ),
    (
        'nearby_dense_se',
        FeatureFunction().has_token_in_sentence,
        {
            'kind': 'Side_Effect',
            'gt': 2,
        }
    ),
    (
        'nearby_very_dense_se',
        FeatureFunction().has_token_in_sentence,
        {
            'kind': 'Side_Effect',
            'gt': 4,
        }
    ),
    (
        'any_problem_free_use',
        FeatureFunction().has_token,
        {
            'kind': 'Problem_Free_Use'
        }
    ),
    (
        'contains_common_se',
        FeatureFunction(
            '+r!(pain|anxiety|appetite|cough|dizz[yines]+|depress[edion]+)'
        ).has_text_in_sentence,
        {
        }
    ),
    ('in_plan',
     FeatureFunction().in_section,
     {
         'match_title': 'plan'
     }
     ),
    ('in_subj',
     FeatureFunction().in_section,
     {
         'match_title': 'subj'
     }
     ),
    ('in_assess',
     FeatureFunction().in_section,
     {
         'match_title': 'asm'
     }
     ),
    ('in_obj',
     FeatureFunction().in_section,
     {
         'match_title': 'obj'
     }
     ),
    ('status_term',
     FeatureFunction().has_token_in_sentence,
     {
         'kind': 'Status_Term',
     }
     ),
    ('nearest_is_med',
     FeatureFunction().has_previous_token,
     {
         'kind': 'Medication',
         'nearest_token_index': 0
     }
     ),
    ('nearest_is_pfu',
     FeatureFunction().has_previous_token,
     {
         'kind': 'Problem_Free_Use',
         'nearest_token_index': 0
     }
     ),
    ('nearest_is_se',
     FeatureFunction().has_previous_token,
     {
         'kind': 'Side_Effect',
         'nearest_token_index': 0
     }
     ),
    ('nearest_is_st',
     FeatureFunction().has_previous_token,
     {
         'kind': 'Status_Term',
         'nearest_token_index': 0
     }
     ),
    ('nearest_in_sent_is_med',
     FeatureFunction().has_previous_token_in_sentence,
     {
         'kind': 'Medication',
         'nearest_token_index': 0
     }
     ),
    ('nearest_in_sent_is_pfu',
     FeatureFunction().has_previous_token_in_sentence,
     {
         'kind': 'Problem_Free_Use',
         'nearest_token_index': 0
     }
     ),
    ('nearest_in_sent_is_se',
     FeatureFunction().has_previous_token_in_sentence,
     {
         'kind': 'Side_Effect',
         'nearest_token_index': 0
     }
     ),
    ('nearest_in_sent_is_st',
     FeatureFunction().has_previous_token_in_sentence,
     {
         'kind': 'Status_Term',
         'nearest_token_index': 0
     }
     ),
    ('nearest_in_sect_is_med',
     FeatureFunction().has_previous_token_in_section,
     {
         'kind': 'Medication',
         'nearest_token_index': 0
     }
     ),
    ('nearest_in_sect_is_pfu',
     FeatureFunction().has_previous_token_in_section,
     {
         'kind': 'Problem_Free_Use',
         'nearest_token_index': 0
     }
     ),
    ('nearest_in_sect_is_se',
     FeatureFunction().has_previous_token_in_section,
     {
         'kind': 'Side_Effect',
         'nearest_token_index': 0
     }
     ),
    ('nearest_in_sect_is_st',
     FeatureFunction().has_previous_token_in_section,
     {
         'kind': 'Status_Term',
         'nearest_token_index': 0
     }
     ),
    ('nearest_is_med_next',
     FeatureFunction().has_next_token,
     {
         'kind': 'Medication',
         'nearest_token_index': 0
     }
     ),
    ('nearest_is_pfu_next',
     FeatureFunction().has_next_token,
     {
         'kind': 'Problem_Free_Use',
         'nearest_token_index': 0
     }
     ),
    ('nearest_is_se_next',
     FeatureFunction().has_next_token,
     {
         'kind': 'Side_Effect',
         'nearest_token_index': 0
     }
     ),
    ('nearest_is_st_next',
     FeatureFunction().has_next_token,
     {
         'kind': 'Status_Term',
         'nearest_token_index': 0
     }
     ),
    ('discontinue',
     FeatureFunction().has_token_in_sentence,
     {
        'kind': 'Discontinue',
     }),
    ('discontinue_med',
     FeatureFunction().has_token_in_sentence,
     {
        'kind': 'Discontinue_Med',
     }),
    ('pw',
     FeatureFunction().previous_word,
     {
         'word_index': 0
     }
     ),
    ('ppw',
     FeatureFunction().previous_word,
     {
         'word_index': 1
     }
     ),
    ('pppw',
     FeatureFunction().previous_word,
     {
         'word_index': 2
     }
     ),
    ('ppppw',
     FeatureFunction().previous_word,
     {
         'word_index': 3
     }
     ),
    ('pppppw',
     FeatureFunction().previous_word,
     {
         'word_index': 4
     }
     ),
    ('nw',
     FeatureFunction().next_word,
     {
         'word_index': 0
     }
     ),
    ('nnw',
     FeatureFunction().next_word,
     {
         'word_index': 1
     }
     ),
    ('nnnw',
     FeatureFunction().next_word,
     {
         'word_index': 2
     }
     ),
    ('nnnnw',
     FeatureFunction().next_word,
     {
         'word_index': 3
     }
     ),
    ('nnnnnw',
     FeatureFunction().next_word,
     {
         'word_index': 4
     }
     ),
]

FEATURE_LABELS = [x[0] for x in FEATURE_FUNCTIONS]

from nlpakki.feat.ctxt import ContextBuilder
from nlpakki.sspl import brat_ssplit

from ammasing_nlp.categories.med_discontinue import DISCONTINUE_PAT, MED_DISCONTINUE_PAT
from ammasing_nlp.categories.meds import MEDICATION_PAT
from ammasing_nlp.categories.prob_free_use import PFU_PAT
from ammasing_nlp.categories.sideeffects import SE_PAT
from ammasing_nlp.categories.sider import SIDER_PAT
from ammasing_nlp.features import FEATURE_FUNCTIONS


def build_features_for_notes(note_iter):
    features = []
    keys = []
    for i, (note_id, note_text) in enumerate(note_iter):
        build_feature_for_note(note_id, note_text, keys, features)
    return features, keys


def build_feature_for_note(note_id, note_text, keys, features):
    cb = ContextBuilder(note_text)
    cb.ssplit(brat_ssplit)
    cb.match('Side_Effect', SE_PAT, SIDER_PAT)
    cb.match('Medication', MEDICATION_PAT)
    cb.match('Problem_Free_Use', PFU_PAT)
    cb.match('Discontinue', DISCONTINUE_PAT)
    cb.match('Discontinue_Med', MED_DISCONTINUE_PAT)
    # cb.match('Status_Term', STATUS_PAT)  # TODO
    cb.featurize(['Side_Effect'], FEATURE_FUNCTIONS, prefix=f'{note_id}')
    features += cb.get_features(oformat='binary')
    keys += cb.get_keys()

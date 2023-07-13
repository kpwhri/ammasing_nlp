import spacy
from prodigy.components.preprocess import add_tokens
from spacy.matcher import PhraseMatcher
from spacy.util import filter_spans

from ammasing_nlp.categories.med_discontinue import DISCONTINUE_PAT, MED_DISCONTINUE_PAT
from ammasing_nlp.categories.meds import get_meds
from ammasing_nlp.categories.prob_free_use import PFU_PAT
from ammasing_nlp.categories.sideeffects import get_ses
from ammasing_nlp.categories.sider import get_sider
from ammasing_nlp.categories.statusterms import STATUS_PAT
from ammasing_nlp.regex_matcher import RegexMatcher

nlp = spacy.blank('en')
strings = nlp.vocab.strings
matcher = PhraseMatcher(nlp.vocab, attr='LOWER')
matcher.add('SIDE_EFFECT', [nlp.make_doc(s) for s in get_ses() | get_sider()])
# matcher.add('MEDICATION', [nlp.make_doc(s) for s in get_meds()])


def clean_text(text):
    return text.replace('Â¶', '\n')


def sort_spans(*spans, key='start'):
    return list(sorted(spans, key=lambda x: x[key]))


def make_textcat_se_stream(stream):
    for doc, id_ in nlp.pipe(((clean_text(d['text']), d['id']) for d in stream), as_tuples=True):
        matches = matcher(doc, as_spans=True)
        if not matches:
            continue
        matched_labels = {strings[span.label] for span in matches}
        if 'SIDE_EFFECT' in matched_labels and 'MEDICATION' in matched_labels:
            spans = filter_spans(matches)  # filter overlaps
            se_spans = [{'start': span.start_char, 'end': span.end_char,
                         'label': 'SIDE_EFFECT'}
                        for span in spans if strings[span.label] == 'SIDE_EFFECT']
            med_spans = [{'start': span.start_char, 'end': span.end_char,
                          'label': 'MEDICATION'}
                         for span in spans if strings[span.label] == 'MEDICATION']
            for se_span in se_spans:
                yield {'id': f'{id_}_{se_span["start"]}',
                       "text": doc.text,
                       "spans": sort_spans(*med_spans, se_span),
                       "label": 'HAS_SIDE_EFFECT'}


def add_tokens_to_stream(f):
    def _add_tokens_to_stream(*args, **kwargs):
        stream = f(*args, **kwargs)
        yield from add_tokens(nlp, stream, use_chars=False)

    return _add_tokens_to_stream


@add_tokens_to_stream
def make_spans_se_stream(stream, require=True, ban=False):
    rx_matcher = RegexMatcher(nlp.vocab)
    rx_matcher.add('PFU', PFU_PAT)
    rx_matcher.add('DISCONTINUE', DISCONTINUE_PAT)
    rx_matcher.add('MED_DISCONTINUE', MED_DISCONTINUE_PAT)
    rx_matcher.add('STATUS', STATUS_PAT)
    for doc, id_ in nlp.pipe(((clean_text(d['text']), d['id']) for d in stream), as_tuples=True):
        matches = matcher(doc, as_spans=True)
        if not ban and require and not matches:
            continue
        if ban and matches:
            continue
        spans = rx_matcher(doc, as_spans=True)
        spans = [
            {'start': span.start_char,
             'end': span.end_char,
             'label': strings[span.label],
             } for span in spans + matches
        ]
        yield {
            'id': id_,
            'text': doc.text,
            'spans': sort_spans(*spans),
        }

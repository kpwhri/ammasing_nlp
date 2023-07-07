import spacy
from spacy.matcher import PhraseMatcher
from spacy.util import filter_spans

from ammasing_nlp.categories.meds import get_meds
from ammasing_nlp.categories.sideeffects import get_ses
from ammasing_nlp.categories.sider import get_sider

nlp = spacy.blank('en')
matcher = PhraseMatcher(nlp.vocab, attr='LOWER')
matcher.add('SIDE_EFFECT', [nlp.make_doc(s) for s in get_ses() | get_sider()])
matcher.add('MEDICATION', [nlp.make_doc(s) for s in get_meds()])


def clean_text(text):
    return text.replace('Â¶', '\n')


def make_stream(stream):
    for doc, id_ in nlp.pipe(((clean_text(d['text']), d['id']) for d in stream), as_tuples=True):
        matches = matcher(doc, as_spans=True)
        if not matches:
            continue
        matched_labels = {nlp.vocab.strings[span.label] for span in matches}
        if 'SIDE_EFFECT' in matched_labels and 'MEDICATION' in matched_labels:
            spans = filter_spans(matches)  # filter overlaps
            se_spans = [{'start': span.start_char, 'end': span.end_char,
                         'label': 'SIDE_EFFECT'}
                        for span in spans if nlp.vocab.strings[span.label] == 'SIDE_EFFECT']
            med_spans = [{'start': span.start_char, 'end': span.end_char,
                          'label': 'MEDICATION'}
                         for span in spans if nlp.vocab.strings[span.label] == 'MEDICATION']
            for se_span in se_spans:
                yield {'id': f'{id_}_{se_span["start"]}',
                       "text": doc.text,
                       "spans": list(sorted(med_spans + [se_span], key=lambda x: x['start'])),
                       "label": 'HAS_SIDE_EFFECT'}

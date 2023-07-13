import prodigy
from prodigy import log
from prodigy.components.loaders import JSONL
from prodigy.util import split_string

from ammasing_nlp.recipes.label_for_prodigy import make_spans_se_stream


@prodigy.recipe(
    'spans.sideeffect',
    dataset=("Dataset to save annotations to", "positional", None, str),
    source=("Data to annotate (file path or '-' to read from standard input)", "positional", None, str),
    required=('List of keyword groups that must be found in note to be reviewed.', 'option', None, split_string),
    banned=('List of keyword groups that must NOT be found in note to be reviewed.', 'option', None, split_string),
    skiptasks=('Skip all reviewed ids from these datasets', 'option', None, split_string),
    skipterms=('Skip specified matched terms', 'option', None, split_string),
)
def spans_sideeffect(dataset, source, required=None, banned=None, skiptasks=None, skipterms=None):
    log("RECIPE: Starting recipe spans.sideeffect", locals())
    stream = JSONL(source)
    stream = make_spans_se_stream(stream, required=required, banned=banned, skiptasks=skiptasks, skipterms=skipterms)
    return {
        'dataset': dataset,
        'view_id': 'spans_manual',
        'stream': stream,
        'config': {
            'labels': ['RELEVANT_SE', 'BOILERPLATE', 'MEDICATION', 'SIDE_EFFECT',
                       'STATUS', 'PFU', 'DISCONTINUE', 'MED_DISCONTINUE'],
        }
    }


@prodigy.recipe(
    'spans.sideeffect.ban',
    dataset=("Dataset to save annotations to", "positional", None, str),
    source=("Data to annotate (file path or '-' to read from standard input)", "positional", None, str),
)
def spans_sideeffect_ban(dataset, source):
    log("RECIPE: Starting recipe spans.sideeffect", locals())
    stream = JSONL(source)
    stream = make_spans_se_stream(stream, banned=True)
    return {
        'dataset': dataset,
        'view_id': 'spans_manual',
        'stream': stream,
        'config': {
            'labels': ['RELEVANT_SE', 'BOILERPLATE', 'MEDICATION', 'SIDE_EFFECT',
                       'STATUS', 'PFU', 'DISCONTINUE', 'MED_DISCONTINUE'],
        }
    }

import prodigy
from prodigy.components.loaders import JSONL

from ammasing_nlp.recipes.label_for_prodigy import make_textcat_se_stream


@prodigy.recipe('textcat.sideeffect')
def textcat_sideeffect(dataset, source):
    stream = JSONL(source)
    stream = make_textcat_se_stream(stream)
    return {
        'dataset': dataset,
        'view_id': 'classification',
        'stream': stream,
    }
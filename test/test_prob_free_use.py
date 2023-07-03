import pytest

from ammasing_nlp.categories.prob_free_use import PFU_PAT


@pytest.mark.parametrize('text', [
    'agreeable to remaining on the medication',
    'without any negative side effects',
    'denies any side effects',
    'did quite well',
    'does tolerate the medication',
    'doing quite well on it',
    'doing very well on it',
    'done well',
    'feeling well',
    'has not had any significant side effects from the medication',
    'is tolerating it well',
    'magic medication',
    'medication is well-tolerated',
    'medication is working well',
    'no adverse effect',
    'no adverse side effects',
    'no apparent adverse drug effects',
    'no medication side effects',
    'no observed side-effects',
    'no problems with rx',
    'no problems with the pill',
    'no s.e. from med',
    'no ses from this',
    'no side effects',
    'not experienced any side effects',
    'without difficulty',
    'without any negative side effects',
    'tolerating it fine',
    'tolerated it without any side effects',
    'tolerated well',
    'tolerates it well',
    'tolerating it fine',
    'tolerating it well',
    'tolerating venlafaxine well',
    'tolerating w/o side effects',
])
def test_pfu_pat(text):
    assert PFU_PAT.search(text)

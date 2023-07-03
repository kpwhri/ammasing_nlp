"""
Test side effect patterns.
"""
import pytest

from ammasing_nlp.categories.sideeffects import get_ses, SE_PAT


@pytest.mark.parametrize('text', get_ses())
def test_se_pat_on_source(text):
    assert SE_PAT.search(text)

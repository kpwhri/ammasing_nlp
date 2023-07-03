"""
Test side effect patterns.
"""
import pytest

from ammasing_nlp.categories.statusterms import get_status, STATUS_PAT


@pytest.mark.parametrize('text', get_status())
def test_status_pat_on_source(text):
    assert STATUS_PAT.search(text)

"""
Test medications.
"""
import pytest

from ammasing_nlp.categories.meds import get_meds, MEDICATION_PAT


@pytest.mark.parametrize('text', get_meds())
def test_med_patterns_on_source(text):
    assert MEDICATION_PAT.search(text)

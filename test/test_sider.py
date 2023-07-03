"""
Test sider side effect patterns.
"""
import pytest

from ammasing_nlp.categories.sider import SIDER_PAT, get_sider


@pytest.mark.parametrize('text', get_sider())
def test_se_pat_on_source(text):
    assert SIDER_PAT.search(text)

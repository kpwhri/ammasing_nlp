from ammasing_nlp.build_features import build_features_for_notes


def test_build_features_on_text():
    notes = [
        (0, 'No side effects on prozac. Asthma.'),
        (1, 'quitting prozac due to abdominal pain')]
    features, keys = build_features_for_notes(notes)
    assert len(features) == len(keys) == 3
    assert keys == ['0_side effects_3', '0_asthma_27', '1_abdominal pain_23']

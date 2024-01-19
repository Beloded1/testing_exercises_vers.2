from functions.level_1.one_gender import genderalize


def test_genderalize_if_male():
    assert genderalize('говорил', 'говорила', 'male') == 'говорил'

def test_genderalize_if_female():
    assert genderalize('говорил', 'говорила', 'female') == 'говорила'

def test_genderalize_if_not_gender():
    assert genderalize('говорил', 'говорила', 'transgender') == 'говорила'

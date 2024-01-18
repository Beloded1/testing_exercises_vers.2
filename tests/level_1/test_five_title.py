from functions.level_1.five_title import change_copy_item


def test_change_copy_item_behavior_for_long_title():
    assert change_copy_item('It is a very very long title', 20) == 'It is a very very long title'


def test_change_copy_item_add_copy():
    assert change_copy_item('Short title', 20) == 'Copy of Short title'


def test_change_copy_item_increase_copy():
    assert change_copy_item('Copy of my item (2)') == 'Copy of my item (3)'


def test_change_copy_for_basic_text():
    assert change_copy_item('Copy of my item') == 'Copy of my item (2)'

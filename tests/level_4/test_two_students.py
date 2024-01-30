import pytest
from functions.level_4.two_students import get_student_by_tg_nickname, Student
from conftest import students



def test__get_student_by_tg_nickname__if_get_empty_student_list():
    assert get_student_by_tg_nickname('olegivanov', []) == None


@pytest.mark.parametrize(
        'nickname,result',
        [
            ('janedoe', Student('Jane', 'Doe', '@janedoe')),
            ('charliebrown', Student('Charlie', 'Brown', '@charliebrown')),
            ('charlie111brown', None),
        ]
)
def test__get_student_by_tg_nickname__if_valid_input(students, nickname, result):
    assert get_student_by_tg_nickname(nickname, students) == result


def test__get_student_by_tg_nickname__if_get_invalid_tg_username():
    with pytest.raises(TypeError):
        get_student_by_tg_nickname(123, students) == None

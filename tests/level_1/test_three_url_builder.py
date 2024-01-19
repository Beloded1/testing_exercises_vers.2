from functions.level_1.three_url_builder import build_url


def test_build_url_without_get_params():
    assert build_url('xxx.com', 'path') == 'xxx.com/path'


def test_build_url_with_get_params():
    assert build_url('xxx.com', 'path', {"param1": "value1", "param2": "value2"}) == 'xxx.com/path?param1=value1&param2=value2'

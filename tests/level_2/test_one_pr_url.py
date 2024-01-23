from functions.level_2.one_pr_url import is_github_pull_request_url
import pytest

def test__is_github_pull_request_url__if_valid_url():
    assert is_github_pull_request_url('https://github.com/Beloded1/testing_exercises_vers.2.git/pull/1') == True


def test__is_github_pull_request_url__if_not_valid_too_long_url():
    assert is_github_pull_request_url('https://github.com/Beloded1/testing_exercises_vers.2.git/pull/1/2') == False


def test__is_github_pull_request_url__if_not_valid_too_short_url():
    assert is_github_pull_request_url('https://github.com/Beloded1/testing_exercises_vers.2.git/pull') == False


def test__is_github_pull_request_url__if_not_valid_url_without_pull():
    assert is_github_pull_request_url('https://github.com/Beloded1/testing_exercises_vers.2.git/null/1') == False


def test__is_github_pull_request_url__if_not_valid_url_without_github():
    assert is_github_pull_request_url('https://mithub.com/Beloded1/testing_exercises_vers.2.git/pull/1') == False





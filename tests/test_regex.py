from tiny_python_utils.regex import search_by_regex


def test_it_returns_matching_string():
    assert search_by_regex(r"en", "string-en") == "en"
    assert search_by_regex(r"ita|en", "string-en") == "en"
    assert search_by_regex(r"ita", "string-ita") == "ita"


def test_it_returns_none_when_no_match():
    assert search_by_regex(r"en", "string") == None

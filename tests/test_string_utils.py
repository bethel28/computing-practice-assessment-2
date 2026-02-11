import string_utils


def test_reverse():
    assert string_utils.reverse("abc") == "cba"


def test_shout():
    assert string_utils.shout("hello") == "HELLO!"

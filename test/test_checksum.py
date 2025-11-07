from src.checksum import modulo11_checksum


def test_good():
    assert modulo11_checksum("2-266-11156-6")

def test_only_digits():
    assert modulo11_checksum("2266111566")

def test_wrong_length():
    assert not modulo11_checksum("12323")
    assert not modulo11_checksum("1234123215678901234")

def test_bad():
    assert not modulo11_checksum("2-266-11156-3")


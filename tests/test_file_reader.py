import file_reader


def test_read_numbers():
    assert file_reader.read_numbers() == [10, 20, 30]

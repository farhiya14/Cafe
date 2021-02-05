import app2

# unit tests


def test_load_file_couriers():
    actual = app2.load_file_couriers().contents

    print(actual)
    expected = "Jack Johnson"

    assert actual == expected

test_load_file_couriers()

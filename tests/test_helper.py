from modules.helper import chech_locate_null_foo, get_location_data_foo, get_coord


def test_chech_locate_null_foo() -> None:
    assert chech_locate_null_foo(123) == True


def test_get_location_data_foo() -> None:
    assert get_location_data_foo(123) == True


def test_get_coord() -> None:
    assert get_coord(123) == True

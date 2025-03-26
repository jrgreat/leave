import pytest


# Arrange
@pytest.fixture
def first_entry():
    return "a"


# Arrange
@pytest.fixture
def order():
    return []


# Act
@pytest.fixture
def append_first(order, first_entry):
    return order.append(first_entry)


def test_string_only(append_first, order, first_entry):
    # Assert
    order.append(first_entry)
    assert order == [first_entry]
    order.append(first_entry)
    order.append(first_entry)
    assert order == [first_entry]

from src.package import Package
import pytest


def test_00__set_measurement_validation():
    with pytest.raises(ValueError) as e:
        Package(mass='Eric is a really Thoughtful applicant :)', width=1337, height=1337, length=1337)
    assert "must be either a floating point or integer" in str(e.value)

def test_01__is_bulky():
    test_package = Package(mass=20, width=1337, height=1337, length=1337)
    assert test_package.bulky is True

def test_02__is_heavy():
    test_package = Package(mass=25, width=1337, height=1337, length=1337)
    assert test_package.heavy is True

def test_03__get_volume():
    test_package = Package(mass=25, width=100, height=100, length=100)
    assert test_package._get_volume() == 1_000_000

def test_04__set_measurement_validation():
    with pytest.raises(ValueError) as e:
        Package(mass=20, width=-1337, height=1337, length=1337)
    assert "cannot be a negative value." in str(e.value)

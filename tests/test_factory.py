from src.factory import Factory

def test_00_sort_package_standard():
    factory = Factory(name='Test Factory Object')
    stack_type = factory.sort_package(width=10, height=10, length=10, mass=15)
    assert stack_type == 'standard'

def test_01_sort_package_special():
    factory = Factory(name='Test Factory Object')
    stack_type = factory.sort_package(width=10, height=10, length=10, mass=25)
    assert stack_type == 'special'

def test_02_sort_package_rejected():
    factory = Factory(name='Test Factory Object')
    stack_type = factory.sort_package(width=120, height=120, length=120, mass=25)
    assert stack_type == 'rejected'

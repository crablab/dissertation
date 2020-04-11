import pytest, cuid

@pytest.fixture(scope='session')
def allocations_class():
    from ..libraries import allocations
    return allocations.allocations()

def test_allocations_load(allocations_class):
    """
    Test that the allocations class is correctly loaded.
    """
    assert allocations_class.load_allocations() == True

def test_allocations_returns(allocations_class):
    """
    Test that allocations are correctly returned in a non-zero list.
    """
    assert allocations_class.load_allocations() == True
    list = allocations_class.allocations

    assert list != False
    assert len(list) > 0
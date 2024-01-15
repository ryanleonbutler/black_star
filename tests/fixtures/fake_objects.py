from black_star.world.items import Item, ItemTypes
import pytest


@pytest.fixture
def fake_sword():
    yield Item("fake sword", ItemTypes.weapon, 0, 5, "fake sword for testing")

import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.lifesupport_facade import LifeSupportSystemFacade

@pytest.fixture
def facade():
    return LifeSupportSystemFacade()

def test_initial_level(facade):
    assert facade.level == 100, "Initial level should be 100%"

def test_set_and_get_stable_level(facade):
    facade.level = 75
    assert facade.level == 75, "Level should be set to 75% and remain stable"

def test_set_warning_level(facade):
    facade.level = 30
    assert facade.level == 30, "Level should be set to 30% and return as warning"

def test_set_critical_level_replenishes(facade):
    facade.level = 10
    assert facade.level == 80, "Level should be replenished to 80% when set below 20%"

def test_multiple_sets(facade):
    facade.level = 60
    assert facade.level == 60, "First set to 60% failed"
    facade.level = 25
    assert facade.level == 25, "Second set to 25% failed"
    facade.level = 15
    assert facade.level == 80, "Third set below 20% should replenish to 80%"

def test_edge_case_zero(facade):
    """Test setting the level to 0 triggers replenishment."""
    facade.level = 0
    assert facade.level == 80, "Level should replenish to 80% when set to 0"
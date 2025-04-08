import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.lifesupport import LifeSupportSystem

def test_oxygen_level_drops_below_threshold_and_is_replenished():
    # Given the life support system is active
    lss = LifeSupportSystem(isActive=True)

    # And the oxygen tank pressure is at 15%
    lss.set_oxygen_level(15)

    # When the system checks the oxygen level
    result = lss.check_oxygen_level()

    # Then the system should automatically replenish oxygen to 80% pressure
    assert 80 == lss.oxygen_level

    # And report "Oxygen replenished to 80%"

    assert "Oxygen replenished to 80%" == result

    # raise NotImplementedError("Don't know correct yet")

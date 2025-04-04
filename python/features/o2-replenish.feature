Feature: Automatic Oxygen Replenishment
  As a Mars colonist,
  I want the life support system to automatically replenish oxygen when levels are low,
  So that I can survive without manual intervention.

  Scenario: Oxygen level drops below threshold and is replenished
    Given the life support system is active
    And the oxygen tank pressure is at 15%
    When the system checks the oxygen level
    Then the system should automatically replenish oxygen to 80% pressure
    And report "Oxygen replenished to 80%"
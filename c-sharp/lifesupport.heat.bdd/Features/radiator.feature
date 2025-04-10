Feature: Radiator

Engage the radiator when heat rises above a critical level

@lifesupport
Scenario: Engage the radiator when internal temperature rises above thirty degrees C
	Given the temperature is 31
	When the temperature is checked
	Then the radiator state should be Engaged
namespace tdd_agile.lifesupport
{
    using System;

    public class WaterLevelMonitor
    {
        private double _waterLevel;

        public WaterLevelMonitor(double initialWaterLevel)
        {
            if (initialWaterLevel < 0)
                throw new ArgumentException("Water level cannot be negative.");
            _waterLevel = initialWaterLevel;
        }

        public double GetWaterLevel() => _waterLevel;

        public void AddWater(double amount)
        {
            if (amount < 0)
                throw new ArgumentException("Cannot add negative water.");
            _waterLevel += amount;
        }

        public void UseWater(double amount)
        {
            if (amount < 0)
                throw new ArgumentException("Cannot use negative water.");
            if (amount > _waterLevel)
                throw new InvalidOperationException("Insufficient water.");
            _waterLevel -= amount;
        }
    }
}

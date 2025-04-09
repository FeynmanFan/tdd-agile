namespace tdd_agile.lifesupport.tests
{
    using System;
    using NUnit.Framework;

    public class Tests
    {
        public class WaterLevelMonitorTests
        {
            [Test]
            public void Constructor_ValidInput_SetsInitialLevel()
            {
                var monitor = new WaterLevelMonitor(100);
                Assert.That(monitor.GetWaterLevel(), Is.EqualTo(100));
            }

            [Test]
            public void AddWater_PositiveAmount_IncreasesLevel()
            {
                var monitor = new WaterLevelMonitor(50);
                monitor.AddWater(20);
                Assert.That(monitor.GetWaterLevel(), Is.EqualTo(70));
            }

            [Test]
            public void UseWater_ValidAmount_DecreasesLevel()
            {
                var monitor = new WaterLevelMonitor(50);
                monitor.UseWater(20);
                Assert.That(monitor.GetWaterLevel(), Is.EqualTo(30));
            }

            [Test]
            public void Constructor_NegativeInitial_ThrowsArgumentException()
            {
                Assert.Throws<ArgumentException>(() => new WaterLevelMonitor(-10));
            }

            [Test]
            public void AddWater_NegativeAmount_ThrowsArgumentException()
            {
                var monitor = new WaterLevelMonitor(50);
                Assert.Throws<ArgumentException>(() => monitor.AddWater(-5));
            }

            [Test]
            public void UseWater_NegativeAmount_ThrowsArgumentException()
            {
                var monitor = new WaterLevelMonitor(50);
                Assert.Throws<ArgumentException>(() => monitor.UseWater(-10));
            }

            [Test]
            public void UseWater_ExceedsCurrentAmount_ThrowsInvalidOperationException()
            {
                var monitor = new WaterLevelMonitor(50);
                Assert.Throws<InvalidOperationException>(() => monitor.UseWater(60));
            }
        }
    }
}

namespace lifesupport.heat
{
    public class Radiator
    {
        public Radiator(decimal initialTemp) 
        {
            this.Temperature = initialTemp;
        }

        public decimal Temperature { get; set; }

        public Boolean CheckTemperature()
        {
            return this.Temperature > 30;
        }
    }
}

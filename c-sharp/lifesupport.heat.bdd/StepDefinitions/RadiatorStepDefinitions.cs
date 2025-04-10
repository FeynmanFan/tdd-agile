using System;
using Reqnroll;

namespace lifesupport.heat.bdd.StepDefinitions
{
    [Binding]
    public class RadiatorStepDefinitions
    {
        Radiator rad = new Radiator(20);

        [Given("the temperature is {int}")]
        public void GivenTheTemperatureIs(int newTemp)
        {
            rad.Temperature = newTemp;
        }

        [When("the temperature is checked")]
        public void WhenTheTemperatureIsChecked()
        {
            var result = rad.CheckTemperature();
            ScenarioContext.Current.Add("checktempresult", result);
        }

        [Then("the radiator state should be Engaged")]
        public void ThenTheRadiatorStateShouldBeEngaged()
        {
            Assert.AreEqual(true, ScenarioContext.Current["checktempresult"]);
        }
    }
}

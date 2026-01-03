package com.example;

import junit.framework.Test;
import junit.framework.TestCase;
import junit.framework.TestSuite;
import com.example.App;

import java.util.Scanner;

/**
 * Unit test for simple App.
 */
public class AppTest 
    extends TestCase
{
    /**
     * Create the test case
     *
     * @param testName name of the test case
     */
    public AppTest( String testName )
    {
        super( testName );
    }

    /**
     * @return the suite of tests being tested
     */
    public static Test suite()
    {
        return new TestSuite( AppTest.class );
    }


    public void testTemperatureConversion()
    {
        assertEquals(32.0F, TemperatureConversion.convertCelsiusToFahrenheit(0));
        assertEquals(273.15F, TemperatureConversion.convertCelsiusToKelvin(0));
        assertEquals(255.37222F, TemperatureConversion.convertFahrenheitKelvin(0));
        assertEquals(-17.777779F, TemperatureConversion.convertFahrenheitToCelsius(0));
        assertEquals(-273.15F, TemperatureConversion.convertKelvinToCelsius(0));
        assertEquals(-459.67F, TemperatureConversion.convertKelvinToFahrenheit(0));
    }

    public void testValidateUnitName() {
        assertEquals("Celsius",TemperatureConversion.validateUnitName("C"));
        assertEquals("Celsius",TemperatureConversion.validateUnitName("c"));

        assertEquals("Fahrenheit",TemperatureConversion.validateUnitName("F"));
        assertEquals("Fahrenheit",TemperatureConversion.validateUnitName("f"));

        assertEquals("Kelvin",TemperatureConversion.validateUnitName("K"));
        assertEquals("Kelvin",TemperatureConversion.validateUnitName("k"));
    }
}

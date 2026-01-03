package com.example;

public class TemperatureConversion {
    private String temperature;
    private String initialUnit;
    private String outputUnit;
    private float resultTemperature;
    public TemperatureConversion(String temperature, String initialUnit, String outputUnit){
        String originalTemperatureUnitName = validateUnitName(initialUnit);
        String outputTemperatureUnitName = validateUnitName(outputUnit);
        if((!originalTemperatureUnitName.equals("invalid")) && (!outputTemperatureUnitName.equals("invalid"))){
            this.initialUnit = originalTemperatureUnitName;
            this.outputUnit = outputTemperatureUnitName;
        }else{
            System.out.println("Invalid Temperature Units");
        }
        float result = convertTemperatureToFloat(temperature);
        if(result != Float.MIN_VALUE){
            this.temperature = temperature;
            this.resultTemperature = temperatureConverter(result,initialUnit.charAt(0),outputUnit.charAt(0));
        }else{
            System.out.println("Invalid Temperature");
        }
    }
    public static float convertCelsiusToFahrenheit(float temperature) {return (temperature*((float) 9 /5)) + 32;}
    public static float convertKelvinToFahrenheit(float temperature) {return (float) ((temperature - 273.15)* ((double) 9 /5) + 32);}
    public static float convertFahrenheitToCelsius(float temperature) {return (temperature - 32 ) *((float) 5 /9);}
    public static float convertKelvinToCelsius(float temperature) {return (float) (temperature - 273.15);}
    public static float convertCelsiusToKelvin(float temperature) {return (float) (temperature + 273.15);}
    public static float convertFahrenheitKelvin(float temperature) {return (float) (((temperature - 32)* ((double) 5 /9) + 273.15));}

    public static String validateUnitName(String tempUnit ){
        switch (tempUnit.toUpperCase()){
            case "C": return "Celsius";
            case "K": return "Kelvin";
            case "F": return  "Fahrenheit";
        }
        return "invalid";
    }

    public static Float temperatureConverter(float temperature, char originalUnit, char outputUnit){
        if(originalUnit =='C' && outputUnit == 'F'){return convertCelsiusToFahrenheit(temperature);}
        if(originalUnit == 'K' && outputUnit == 'F'){return convertKelvinToFahrenheit(temperature);}

        if(originalUnit == 'F' && outputUnit == 'C'){return convertFahrenheitToCelsius(temperature);}
        if(originalUnit == 'K' && outputUnit == 'C'){return convertKelvinToCelsius(temperature);}

        if(originalUnit == 'C' && outputUnit == 'K'){return convertCelsiusToKelvin(temperature);}
        if(originalUnit == 'F' && outputUnit == 'K'){return convertFahrenheitKelvin(temperature);}
        if(originalUnit == outputUnit){return temperature; }
        return Float.MIN_VALUE;
    }

    public static Float convertTemperatureToFloat(String temperature){
        try{
            return Float.parseFloat(temperature);
        }
        catch (NumberFormatException e ){
            System.out.println("Error Trying to convert String to Float: " + e);
            return Float.MIN_VALUE;
        }
    }

    //Getters
    public float getTemperature(){return this.resultTemperature; }
    public String getInitialUnit(){return this.initialUnit; }
    public String getOutputUnit(){return this.outputUnit; }

    public void printResult(){
        System.out.println(this.temperature + " degrees " + getInitialUnit() + " is equivalent to " +  getTemperature() + " degrees " + getOutputUnit());
    }
}

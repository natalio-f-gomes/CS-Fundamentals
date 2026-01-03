package com.example;

import java.util.Scanner;

public class App 
{
    public static void main( String[] args )
    {
        Scanner scanner = new Scanner(System.in);
        String username = getUserInput("Please enter your name: ",scanner);
        welcomeMessage(username);

        String temperature = getUserInput("Enter the Temperature: ", scanner);
        String tempUnit = getUserInput("Enter the Temperature Unit: \nC - Celsius\nF - Fahrenheit\nK - Kelvin\nA: ", scanner);
        String outputUnit =  getUserInput("Enter the Temperature Unit: \nC - Celsius\nF - Fahrenheit\nK - Kelvin\nA: ", scanner);
        TemperatureConversion temperatureConversion = new TemperatureConversion(temperature, tempUnit, outputUnit);
        temperatureConversion.printResult();
    }

    public static void welcomeMessage(String name){
        System.out.println("Hello " + name);
        System.out.println("Welcome to Temperature Converter Application");
    }

    public static String getUserInput(String input,Scanner scanner){
        System.out.print(input);
        return scanner.nextLine();
    }

}

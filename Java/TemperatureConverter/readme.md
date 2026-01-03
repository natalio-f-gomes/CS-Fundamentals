Author: Natalio Gomes
Date: 12/22/2025
Project Name: Temperature Conversion
Project Description: Converts temperatures from all 3 units.

# Temperature Converter Application

A simple Java console application that converts temperature values between Celsius (°C), Fahrenheit (°F), and Kelvin (K).

## Overview

This project consists of a basic command-line temperature conversion tool. It allows users to:
- Input a temperature value as a string
- Specify the initial unit (C, F, or K)
- Specify the desired output unit (C, F, or K)
- Receive the converted temperature with proper formatting

The application includes input validation for both the temperature value and units, and it provides clear error messages for invalid inputs.

## Project Structure

```
com.example/
├── TemperatureConversion.java  # Core conversion logic and object model
├── App.java                    # Main entry point with console interaction
└── AppTest.java                # JUnit 3 unit tests for conversion methods
```

## Features

- Supports conversions between **Celsius ↔ Fahrenheit ↔ Kelvin** (all 6 directions + same-unit case)
- Case-insensitive unit input (e.g., "c", "C", "k", etc.)
- Validates temperature input (must be a valid float number)
- Validates unit input (only C, F, K accepted)
- Friendly console greeting with user's name
- Prints results in a readable format

## How to Run

### Prerequisites
- Java JDK 8 or higher
- Maven or any Java build tool (optional – can be run directly)

### Steps

1. Compile the source files:
   ```bash
   javac com/example/*.java
   ```

2. Run the application:
   ```bash
   java com.example.App
   ```

3. Follow the prompts:
    - Enter your name
    - Enter the temperature value (e.g., `25`)
    - Enter the initial unit (C, F, or K)
    - Enter the desired output unit (C, F, or K)

### Example Run

```
Please enter your name: Alice
Hello Alice
Welcome to Temperature Converter Application
Enter the Temperature: 100
Enter the Temperature Unit: 
C - Celsius
F - Fahrenheit
K - Kelvin
A: C
Enter the Temperature Unit: 
C - Celsius
F - Fahrenheit
K - Kelvin
A: F
100 degrees Celsius is equivalent to 212.0 degrees Fahrenheit
```

### Invalid Input Handling

- Invalid unit → "Invalid Temperature Units"
- Invalid temperature string → "Invalid Temperature"

## Testing

The project includes basic unit tests using **JUnit 3** (legacy style).

### Running Tests

If you have JUnit 3 on your classpath:

```bash
java -cp .:/path/to/junit.jar org.junit.runner.JUnitCore com.example.AppTest
```

Or use an IDE (IntelliJ, Eclipse) to run `AppTest`.

### Tests Included

- Conversion accuracy for all supported directions
- Unit name validation (case insensitivity)


## License

This is a simple educational/example project. Feel free to use, modify, and distribute it freely.

---

**Enjoy converting temperatures!** 🌡️
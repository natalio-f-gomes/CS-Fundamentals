import java.util.NoSuchElementException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        printWelcomeMessage();
        String arraySizePromptText = "How many elements would you like the array to have?\n  Enter an integer from zero (0) to 20 (0-20, inclusive)";
        int arraySize = runSafeNonNegIntegerPrompt(arraySizePromptText, 20);
        runArrayBuilder(arraySize);

}
    private static void printWelcomeMessage() {
        System.out.println("=================================================");
        System.out.println("**** INPUT ERROR PROOF INT[] ARRAY BUILDER ****");
        System.out.println("Let's build an int[] array (safely).");
        System.out.println("=================================================");

    }


    private static int runSafeNonNegIntegerPrompt(String userPromptText, int upperBound) {
        boolean valid;
        String inputString;
        Scanner kbScanner = new Scanner(System.in);
        do {
            System.out.println(userPromptText);
            System.out.print(">> ");
            inputString = kbScanner.nextLine();
            valid = nonNegIntSafePromptHelper(inputString, upperBound);
        }while (valid == false);
        int validArraySizeInt = Integer.parseInt(inputString);

        return validArraySizeInt;
    }




    private static boolean nonNegIntSafePromptHelper(String inputString, int upperBound) {
        if(stringIsNonNegInt(inputString)==false){
            System.out.println("ERROR: You entered an invalid input!");
            return false;
        }else{
            int testInt = Integer.parseInt(inputString);
            if(testInt>upperBound){
                System.out.println( "ERROR: You entered a value that is out of range!!");
                return false;
            }

            return true;
    }
    }

    private static boolean stringIsNonNegInt(String inputString) {

    boolean status = false;
      if(inputString.length()==0){
          return false;

      }

      for(int i = 0;i<inputString.length();i++) {
          char ch = inputString.charAt(i);
          int ascii = ch;
          // You can also cast char to int
          int castAscii = (int) ch;
          if (47 >= castAscii || castAscii >= 58) {
              status = false;
          } else {
              status = true;
          }

      }
      return status;
    }
    private static void runArrayBuilder(int arrayLength) {
        int[] newIntArray;
        newIntArray = new int[arrayLength];
        System.out.println("""
                =================================================
                Let's start filling the array with values from zero to 50 (0-
                50, inclusive)...
                """);
        System.out.println(" **** The array will have " + arrayLength + " elements. ****");
        buildArray(newIntArray);
        System.out.println("""
                =================================================
                Here is a visual display of the array values you entered:
                """);
        visualizeArrayContent(newIntArray);
        System.out.println("=================================================\n");
}
    private static void buildArray(int[] intArray) {
        String elementPromptText = ("Enter an integer between zero and 50 (0-50, inclusive) to fill element at index ");
        for(int i =0;i<intArray.length;i++){
            intArray[i]=  runSafeNonNegIntegerPrompt(elementPromptText + intArray[i], 50);
            System.out.println("Element " + i + " set to " +
                    intArray[i]);
            printArrayElements(intArray);


        }
    }
    private static void printArrayElements(int[] arrayToBePrinted) {
        System.out.print("Current Array Values: ");
        for(int i : arrayToBePrinted){
            System.out.print(i+" ");
        }
        System.out.println();
    }
    private static void visualizeArrayContent(int[] arrayToBeDisplayed) {
        for(int i=0;i<arrayToBeDisplayed.length;i++){
            System.out.print("Value at index " + i + " (" +
                    arrayToBeDisplayed[i] + ")\t-> ");
            for(int j = 0;j<arrayToBeDisplayed[i];j++){
               int value =  arrayToBeDisplayed[i];
                System.out.print('*');

            }
        }
        System.out.println();

    }



    }

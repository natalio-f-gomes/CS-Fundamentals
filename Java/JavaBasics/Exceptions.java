/*
*   In this class, there is the Exception lecture, where you can customize your own exceptions
*   Throw new exceptions
*
* */

class CustomException extends Exception{
    public CustomException(String message){
        System.out.println(message);
    }
}

class Person{
    int age;
    String name;

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Person(String name, int age){
        this.name =name;
        this.age = age;
    }
}

public class Exceptions {
    public static void main(String[] args) {
        String str = null;
        int[] lst = new int[5];
        int i = 20;
        int j = 2;
        int result = 0;

        try {
            Person person1 = new Person("Natalio", 31);
            if(person1.getAge()<21) throw new CustomException("Must be older to be able to drink");

        }
        catch (CustomException error){
            System.out.println(error);
        }




        try{
            //System.out.println(str.length());
            //ystem.out.println(lst[-1]);

            result = i/j;

            if(j==0){
                //Calls the ArithmeticException catch it
                throw  new ArithmeticException("Cannot divide by zero");}

        }
        catch (NullPointerException error){
            System.out.println("The str is null, therefore it does not have a length");
        }
        catch (ArrayIndexOutOfBoundsException error){
            System.out.println("The array cannot access the number specified");
        }
        catch (ArithmeticException error){
            System.out.println(STR."There was an error: \{error}");
        }
        catch (Exception error){
            //should always handle the Exception at the bottom
            System.out.println("Something went wrong: " + error);
        }
        finally {
            //This block here is used to close the recourse. Meaning after handling all the exceptions,
            // we should execute certain parts of our code regardless.
            System.out.println(result);

        }


    }
}

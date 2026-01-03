public class Abstraction {
    public static void main(String[] args) {

    }
}
//Only abstract classes can have abstract methods.
// Abstract classes does not need to have abstract methods
//When a class inherits it, the class must Override and provide the body to the abstract method.
// You can create a abstract class that inherits another abstract class. In this case the subclass
// does not need to define the abstract method.

abstract class Phone{
    public abstract void OS();

    public void playingMusic(){
        System.out.println("Playing music");
    }
}

class Iphone extends Phone{
    @Override
    public void OS(){
        System.out.println("iOS");
    };
}
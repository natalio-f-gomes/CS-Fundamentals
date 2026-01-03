class Mobile{
    String name;
    int price;

    //Static maena sall objects using this instance shares the same value
    static String type;
    public Mobile(String name, int price, String type){
        this.name = name;
        this.price = price;
        Mobile.type = type;
    }
    public void getInfo(){
        System.out.println(name + " 0 " + price + " - " + type );
    }
}

class Computer{
    String name;
    int price;

    //Static means all objects using this instance shares the same value
    static String type;
    public Computer(String name, int price, String type){
        this.name = name;
        this.price = price;
        Computer.type = type;
    }
    public static void getInfo(Computer obj){
        // can only have the static variables inside of it, unless we specify what object we want to use
        System.out.println(obj.name + " 0 " + obj.price + " - " + type );
    }
}

class Gym{
    String name;
    static int num;
    public Gym(String name){
        this.name =name;
    }
    static {
        num = 19;
        System.out.println(num);
    }
}

public class Static {


    public static void main(String[] args) throws ClassNotFoundException {
        Mobile phone1 = new Mobile("iPhone13", 1200,"SmartPhone");
        Mobile phone2 = new Mobile("Samsung 4plus", 1300,"Phone");

        //phone1.getInfo(); // iPhone13 0 1200 - Phone
        //phone2.getInfo();

        Computer computer1 = new Computer("MacBookPro", 1500,"laptop");
        Computer computer2 = new Computer("MacStudios", 800,"pc");

        Computer.getInfo(computer1);

        Computer.getInfo(computer2);

        Class.forName("Gym"); // instance it, loas the class

        //Gym gym = new Gym("WOW"); //if i do not initialize this object it will not call the static block
        //it calls the static block first
        //when a java program starts running it loads the class first due to the JVM ClassLoader
        // and this class calls the static block first, and then it run the rest of the program
        //System.out.println(gym.name);


    }
}

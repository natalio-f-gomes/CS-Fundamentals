

interface Animal{
    //in interfaces, all variables are final and static.
    //Meaning they cannot change
    String getName(String name);
    int getAge(int age);

}

interface Vet extends  Animal{
    void getVet();
}

class Dog implements Animal, Vet{
    //a class can implement multiple interfaces
    @Override
    public String getName(String name){
        return name;

    }
    @Override
    public int getAge(int age){
        return age;
    }

    @Override
    public void getVet(){
        System.out.println("Veteran");
    }

}


interface Apple {
    void code();
        }
class MacBookPro implements Apple{
    @Override
    public void code(){
        System.out.println("code, compile, run");
    };
}
class iPad implements Apple{
    @Override
    public void code(){
        System.out.println("code, compile, run");
    }
}



public class Interfaces {
    public static void main(String[] args) {
        Animal puppy1 = new Dog();
        Vet vet1 = new Dog();

        int age = puppy1.getAge(10);
        System.out.println(age);

        Apple ipad = new iPad();
        Apple laptop = new MacBookPro();


        laptop.code();

    }
}

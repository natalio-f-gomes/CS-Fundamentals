class Cooking extends Thread{
    public void run(){
        for(int i =0;i<100;i++){
            System.out.println("Cooking");
        }
    }
}
class Cleaning extends Thread{
    public void run(){
        for(int i =0;i<100;i++){
            System.out.println("Cleaning");
        }
    }
}


public class Threads {
    public static void main(String[] args) {
        Cooking cooking = new Cooking();
        Cleaning cleaning = new Cleaning();

        cooking.start();
        cleaning.start();
    }
}

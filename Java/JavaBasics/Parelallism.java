

public class Parelallism {
    public static void main(String[] args) {

        Runnable en = () -> {
            for(int i = 0; i<10;i++){
                System.out.println("Hello");
            }
        };
        Runnable rd = () -> {
            for (int i=10;i>0;i--) {
                System.out.println("Hi");
            }
        };

        Thread t1 = new Thread(en);
        Thread t2 = new Thread(rd);

        t1.start();t2.start();

    }
}

class Counter{
    public int count = 0;
    public synchronized void  increment(){
        this.count++;
    }
}

public class RaceCondition {
    public static void main(String[] args) throws InterruptedException {
        Counter c1 = new Counter();
        Runnable run1 = () -> {
            for(int i= 0; i<1000;i++){
                c1.increment();
            }
        };
        Runnable run2 = () -> {
            for (int i=0; i<1000;i++){
                c1.increment();
            }
        };


        Thread t1 = new Thread(run1);
        Thread t2 = new Thread(run2);



        t1.start();
        t2.start();

        t1.join();
        t2.join();

        System.out.println(t1.threadId());

        System.out.println(c1.count);
    }

}

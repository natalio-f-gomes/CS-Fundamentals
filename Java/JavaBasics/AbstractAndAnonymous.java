abstract class A1 {
    public abstract void greeting();

}
class B1 extends A1{
    @Override
    public void greeting() {
        System.out.println("Hello from B1");
    }
}
public class AbstractAndAnonymous {

    public static void main(String[] args) {
        A1 a1 = new A1() {
            @Override
            public void greeting() {
                System.out.println("Hello");
            }
        };
    }
}


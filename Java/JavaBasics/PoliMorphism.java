public class PoliMorphism {
    public static void main(String[] args) {

    }
}
class A{
    public void method1(int a){

    }
    public void method1(int a, int b){

    }
}

class  B extends  A{
    @Override
    public void method1(int a) {
        super.method1(a);
    }
}

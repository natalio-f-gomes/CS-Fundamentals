@FunctionalInterface
interface C1{

    //the annotation FunctionInterface annotation tells the compiler that this interface should only have 1 method.

    public int myMethod(int x, int y);
}




public class InterfaceTypes {
    public static void main(String[] args) {
        //lambda expression. It syntactically reduces the code, however the compiler performs the same job
        //lambda expression only works with Functional Interfaces
        C1 c1 =  (x,y) -> {return x+y;};


        ;

        System.out.println(c1.myMethod(11,7));

    }
}

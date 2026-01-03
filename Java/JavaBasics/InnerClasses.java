
class OuterClass{
    int age;
    public void show(){
        System.out.println("In show");
    };
    class InnerClass{
        public void config(){
            System.out.println("In config");
        }
    }

}

public class InnerClasses {
    public static void main(String[] args) {
        OuterClass oc = new OuterClass();
        oc.show();

        OuterClass.InnerClass in = oc.new InnerClass();
        // when complied, it should appear => OuterClass$InnerClass, meaning OuterClass have Inner class inside of it
        // The inner class can be static, however the Outer cannot
        in.config();

        //anonymous class
        OuterClass anonymous = new OuterClass(){
            public void show(){
                System.out.println("Anonymous method")
;            }
        };
        //when compiled it will create a java.clas file named OuterClass$1.java
        //the more anonymous class we create the number increases,
        // however it does not have a name
        anonymous.show();

    }
}

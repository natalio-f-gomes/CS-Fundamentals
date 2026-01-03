public class Strings {
    public static void main(String[] args) {
        //Immutable strings
        String name = new String("Natalio"); //original address = 821270929
        name = name + "Gomes"; // new address =  1160460865
        int numAddress = System.identityHashCode(name);
        //System.out.println(numAddress);


        //Mutable Strings  - StringBuffer
        StringBuffer Name = new StringBuffer("Nato");// 1160460865

        int sbAddress2 = System.identityHashCode(name);
        System.out.println(sbAddress2);
        Name.insert(4, " Fernandes");

        System.out.println(sbAddress2); // 1160460865
        System.out.println(Name);
    }
}

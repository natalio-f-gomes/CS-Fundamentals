class Student{
    String name;
    int age;
}


public class ArrayObjects {
    public static void main(String[] args) {

        Student s1 = new Student();
        s1.name = "Natalio";
        s1.age = 20;

        Student s2 = new Student();
        s2.name = "Alexa";
        s2.age = 25;

        Student s3 = new Student();
        s3.name = "Joana";
        s3.age = 89;

        Student s4 = new Student();
        s4.name = "Camila";
        s4.age = 15;

        Student[] students = new Student[4];
        students[0] = s1;
        students[1] = s2;
        students[2] = s3;
        students[3] = s4;

        for (Student student : students) {
            System.out.println(student.name);
        }
    }

}

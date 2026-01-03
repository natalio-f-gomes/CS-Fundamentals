import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner user_input = new Scanner(System.in);
        System.out.println("How many student records? ");
        int student_runner = user_input.nextInt();
        user_input.nextLine();

        Student[] StudentArray = new Student[student_runner];
        for(int i = 1;i<student_runner+1;i++){
            String student_name = "";
            System.out.println("Enter the first and last name of the student "+i);
            student_name += user_input.nextLine();
            System.out.print("Enter "+ student_name +"'s Major: ");
            String student_major = user_input.nextLine();
            System.out.print("Enter "+ student_name +"s'ID: ");
            int student_id = user_input.nextInt();

            user_input.nextLine();
            System.out.print("Enter "+student_name+"'s GPA: ");
            double student_gpa = user_input.nextDouble();
            Student student = new Student(student_name,student_major,student_id,student_gpa);
            StudentArray[i-1] = student;

        }
        for(Student i: StudentArray){
            i.displayInfo();
        }

    }
}

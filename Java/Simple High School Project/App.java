import java.util.ArrayList;

public class App {
    public static void main(String[] args) throws Exception {
        ArrayList<String> courses_name = new ArrayList<String>();
        courses_name.add("Math");
        courses_name.add("English");
        courses_name.add("CS");
        courses_name.add("Chemistry");
        courses_name.add("Portuguese");

        float[] grades = {100,100,100,0};

        Student student1 = new Student("Natalio", "Fernandes", "Cape Verdean", 'M', 19, "BSU", courses_name, grades);
        student1.Get_Courses_list();
        System.out.println(student1.Get_Age());
        System.out.println(student1.Get_Full_Name());
        System.out.println(student1.Get_GPA());
        System.out.println(student1.Get_Nationality());
        System.out.println(student1.Get_Gender());

        System.out.println("Teachers info ");

        Teacher Teacher1 = new Teacher("Anna", "Antunes", "French", 'F', 39, "BSU", 80000,student1);
        System.out.println(Teacher1.GetStudents());
       
        
    

    
    }
}

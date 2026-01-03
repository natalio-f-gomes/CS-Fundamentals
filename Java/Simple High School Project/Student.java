import java.util.ArrayList;


public class Student extends School {
    
    public Student(String f_name,String l_name, String nationality, char gender, int age, String School_Name, ArrayList<String> courses,float[] grades){
        this.f_name = f_name;
        this.l_name = l_name;
        this.nationality = nationality;
        this.gender = gender;
        this.age = age;
        this.School_Name = School_Name;
        this.courses = courses;
        this.grades = grades;
        this.type = "Student";

    }
    @Override
    public String Get_Full_Name(){
        return this.f_name + " " + this.l_name;
    }
    @Override
    public String Get_Nationality(){
        return this.nationality;
    }
    @Override
    public char Get_Gender(){
        return this.gender;
    }
    @Override
    public int Get_Age(){
        return this.age;
    }
    @Override
    public String Get_email(){
        return  this.l_name.charAt(0)+"." + this.f_name + "@"+this.School_Name+"."+this.type+".edu";
    }

    public void Get_Courses_list(){
        System.out.println("Courses List: ");
        for (int i=0;i<courses.size();i++){
            System.out.println(courses.get(i));
        }
        
    }

    public double Get_GPA(){
        
        double total = 0;
        for (int i =0 ; i<this.grades.length;i++){
            total += grades[i];
        }
        double gpa = (total * 4) / grades.length/100;

        return +gpa;
    }
    
    
}


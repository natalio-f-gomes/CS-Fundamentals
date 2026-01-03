import java.util.ArrayList;

public abstract class School {
    public School(){}
    protected String f_name;
    protected String l_name;
    protected String nationality;
    protected char gender;
    protected int age;
    protected String School_Name;
    protected String type;
    //Speciffically for Teachers
    protected double raise_amount = 1.05;
    protected float Salary;
    //Speciffically for Students
    protected ArrayList<String> courses;
    protected String Course1;
    protected String Course2;
    protected String Course3;
    protected String Course4;
    protected String Course5;
    protected float[] grades;
    protected double GPA;

    public abstract String Get_Full_Name();
    public abstract String Get_Nationality();
    public abstract char Get_Gender();
    public abstract int Get_Age();
    public abstract String Get_email();
   
    

   
}



public class Teacher extends School {

    private Student students;
    public Teacher(String f_name,String l_name, String nationality, char gender, int age, String School_Name, float Salary, Student students){
        this.f_name = f_name;
        this.l_name = l_name;
        this.nationality = nationality;
        this.gender = gender;
        this.age = age;
        this.School_Name = School_Name;
        this.Salary = Salary;
        this.type = "Teachers";
        this.students =students;
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
        return this.l_name.charAt(0)+"." + this.f_name + "@"+this.School_Name+"."+this.type+".edu";
    }
    public void Set_Salary(float amount){
        this.Salary += amount;
    }
    public double Get_Salary(){
        return this.Salary;
    }
    public double ApplyRaise(){
        return this.Salary *= raise_amount;
    }
    public String GetStudents(){
       return students.Get_Full_Name();
        }
    }


    
        //get full name
        //get nationality
        //get age
        //get gender
        //get email
    
    


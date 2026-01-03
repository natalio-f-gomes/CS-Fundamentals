public class Student {
    private String name;
    private String major;
    private int id;
    private double gpa;
    public Student(String name, String major, int id, double gpa){
        this.name = name;
        this.id = id;
        this.gpa = gpa;
        this.major = major;
    }
    public String getName(){
        return this.name;
    }
    public String getMajor(){
        return this.major;
    }
    public int getID(){
        return this.id;
    }
    public double getGPA(){
        return this.gpa;
    }
    public void setName(String name){
        this.name = name;
    }
    public void setMajor(String major){
        this.major = major;
    }
    public void setID(int id){
        this.id = id;
    }

    public void setGPA(double gpa){
        this.gpa = gpa;
    }
    public void displayInfo(){
        System.out.println("Student info for: "+ this.name);
        System.out.println("ID "+ this.id);
        System.out.println("Major "+ this.major);
        System.out.println("GPA "+ this.gpa);
    }

}

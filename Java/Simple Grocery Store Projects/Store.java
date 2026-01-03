public abstract class Store {
    protected static int total_members= 0;
    protected static int employees= 0;
    protected static int managers= 0;
    protected String First_Name;
    protected String Last_Name;
    protected int Age;
    protected String department;
    protected double salary;
    protected String type;
    protected String ethnicity;
    protected String race;
    protected String store_name;
    protected String commercialtype;


    public abstract String GetName();
    public abstract int GetAge();
    public abstract String GetDepartment();
    public abstract String GetEmail();
    public abstract String GetType();
    public abstract Double GetSalary();
    public abstract String GetEtchnicity();
    public abstract String GetRace();
    public abstract String GetStoreName();
    public abstract String GetCommercialType();
    public abstract Double SetRaise(double amount);
    public abstract Double ApplyRaise();


    
}

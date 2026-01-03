

public class Employees extends Store{
    //first name
    //last anme
    //age
    //department
    //email
    //salary
    //Type
    //ethnicity
    Double raise = 1.3;
    public Employees(String First_Name,String Last_Name, int Age, String department, double salary, String ethnicity, String race, String commercialtype, String store_name){
        this.First_Name = First_Name;
        this.Last_Name = Last_Name;
        this.Age = Age;
        this. department = department;
        this.salary = salary;
        this.type = "Employee";
        this.ethnicity = ethnicity;
        this.race = race;
        this.commercialtype = commercialtype;
        this.store_name = store_name;
        Store.total_members +=1;
        Store.employees+=1;
    }

    @Override
    public String GetName() {
        return this.First_Name+ " "+ this.Last_Name;
    }

    @Override
    public int GetAge() {

        return this.Age;
    }

    @Override
    public String GetDepartment() {
        return this.department;
    }

    @Override
    public String GetEmail() {
        return this.Last_Name +this.Last_Name+this.type+"@"+this.store_name+"."+this.commercialtype.strip();
    }

    @Override
    public String GetType() {
        // TODO Auto-generated method stub
        return this.type;
    }

    @Override
    public Double GetSalary() {
        return this.salary;
    }

    @Override
    public String GetEtchnicity() {
        
        return this.ethnicity;
    }

    @Override
    public String GetRace() {
        return this.race.toUpperCase();
    }

    @Override
    public String GetStoreName() {
        
        return this.store_name;
    }

    @Override
    public String GetCommercialType() {
        return this.commercialtype.strip();
    }

    @Override
    public Double SetRaise(double amount) {
        return this.raise = amount;
    }

    @Override
    public Double ApplyRaise() {
        return this.salary*=raise;
    }
}

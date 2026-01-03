public class LeapYear {
    private int year;
    public LeapYear(int year){
        this.year = year;
    }
    public void CheckIfLeapYear(){
        if(this.year%400==0){
            if(this.year%100==0){
                if(this.year%4==0){
                    System.out.println("Leap");
                }
            
            System.out.println("Not Leap");
            }
        
            System.out.println("Leap");
        }
    
        System.out.println("Not Leap");
    }
}

public class Goomba extends GSU{
 
    public Goomba(String name,int donation) {
        //name, donation and type must be typed in all classes manually, or use super keyword
            this.name = name;
            this.donation = donation; 
            this.type = "Goomba";
        }

    @Override
    public String GetName(){  
    return this.name;
    }
    @Override 
    public int GetDonation(){
     return this.donation; 
    }
    @Override 
    public String GetType(){
        return this.type;
    }
}
    

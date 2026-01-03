public class ParaGoomba extends GSU{

    public ParaGoomba(String name,int donation) {
        //name, donation and type must be typed in all classes manually, or use super keyword
            this.name = name;
            this.donation = donation; 
            this.type = "ParaGoomba";
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
       

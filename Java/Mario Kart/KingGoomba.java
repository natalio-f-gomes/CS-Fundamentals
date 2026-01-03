public class KingGoomba extends GSU{
    
    public KingGoomba(String name,int donation) {
        //name, donation and type must be typed in all classes manually, or use super keyword
            this.name = name;
            this.donation = donation; 
            this.type = "KingGoomba";
        }

 
    //the follwing methods get the names, donation and type
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
       

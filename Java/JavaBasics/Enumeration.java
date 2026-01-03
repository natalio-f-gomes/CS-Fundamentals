enum Status{
    PENDING, FINISHED, STOPPED, STARTED
    //these are statics and finals
}

enum Laptop{
    MABBOOKPRO(1500), XPS(1500), ALIEN(3000), LENOVO;

    private int price;

    private Laptop(int price){
        this.price = price;
        System.out.println("Laptop: " + this.name() );;
    }
    private Laptop(){
        this.price = 500;
    }
    public int getPrice(){
        return this.price;
    }
    
    public void setPrice(int price){
        this.price = price;
    }
}


public class Enumeration {
    public static void main(String[] args) {
        Status[] status = Status.values();

        Laptop[] laptop1 = Laptop.values();
        for (Laptop lap: laptop1){
            System.out.println(lap + " : $" + lap.getPrice());
        }

    }
}


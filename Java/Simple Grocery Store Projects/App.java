import java.io.FileReader;

import com.opencsv.CSVReader;

public class App {
    public static void main(String[] args) throws Exception {
        Manager manager1 = new Manager("Natalio", "Gomes", 32, "Meat", 9000, "CapeVerdean", "Black","Meat","Vicentes");
        Manager manager2 = new Manager("Livy", "Fournier", 38, "Kitchen", 10000, "Canadian", "White","Grocery","Market basket");

        Employees employee1 = new Employees("Kevin", "Pina", 32, "Meat", 8000, "CapeVerdean", "Spanic", "Supermaket","Beto");
        Employees employee2 = new Employees("Leandro", "Push", 38, "Kitchen", 5000, "Canadian", "White","MiniMarket","Shaws");
        
    }
}

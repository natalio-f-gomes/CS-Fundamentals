import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.io.FileReader;
import java.util.ArrayList;
import javax.swing.JFileChooser;

import com.opencsv.CSVReader;


public class Actionhandler {
    private TextPart tp;
    private ButtonPart bp;
    
   
    public Actionhandler(TextPart tp, ButtonPart bp){
        this.tp = tp;
        this.bp = bp;
        
        
        //alleader contains all added buttons. for now
        //AddListenerstoButtons();
    }

    public void AddListenerstoButtons(){
        Listener listener = new Listener();
        for (JButton eachB:bp.GetButtonArrList()){
            eachB.addActionListener(listener);
        }
}

    private class Listener implements ActionListener{
        int Goombadonation = 0;
        int ParaGoombadonation = 0;
        int KingGoombadonation = 0;
        
        @Override
        public void actionPerformed(ActionEvent e){
        JButton but = (JButton) e.getSource();
        String butText = but.getText();
        
        
        if (butText.equals("Open CSV")){
            //code for c
            JFileChooser jfc = new JFileChooser();
            int returnVal = jfc.showOpenDialog(null);
            String csvfilename = "";
            if (returnVal == javax.swing.JFileChooser.APPROVE_OPTION){
                csvfilename = jfc.getSelectedFile().toString();
                System.out.println(csvfilename);
            }
            try{
                FileReader filereader = new FileReader(csvfilename); //Get the path of CSV file
                CSVReader csvreader = new CSVReader(filereader); // Reads the file
                String[] nextLine = csvreader.readNext(); // Saves evertyhing into a list of string

               
                ArrayList<GSU> GsuArray = new ArrayList<GSU>();//create an GSU arraylist that saves all the data of all goombas
                nextLine = csvreader.readNext(); //Start reading the next line, because the first line is the name, type and donation
        
                //Iterate through the list Nextline and separates the names, types and donation
                while(nextLine != null){
                    String name = nextLine[0];
                    String type = nextLine[1];
                    int donation = Integer.parseInt(nextLine[2]);
        
                    //If type of the goombas in Nextline euals Goomba, save the info into the goomba object, and add it into the GSU array
                    if (type.equals("Goomba")){
                        Goomba goomba = new Goomba(name,donation);
                        GsuArray.add(goomba);
                    }
                    //If type of the goombas in Nextline euals ParaGoomba, save the info into the goomba object, and add it into the GSU array
                    if (type.equals("ParaGoomba")){
                    ParaGoomba paragoomba = new ParaGoomba(name,donation);
                    GsuArray.add(paragoomba);
                    }
                    //If type of the goombas in Nextline euals KingGoomba, save the info into the goomba object, and add it into the GSU array
                    if (type.equals("KingGoomba")){
                    KingGoomba kinggoomba = new KingGoomba(name,donation);
                    GsuArray.add(kinggoomba);
                    }
                    nextLine = csvreader.readNext();
                    
        
                
            }
           
        
            //Loop through the arraylist and accodring to their type adds their values into the donations    
            for(int i = 0; i<GsuArray.size();i++){
                if ( GsuArray.get(i).GetType().equals("Goomba")){
                Goombadonation += GsuArray.get(i).GetDonation();
                System.out.println(Goombadonation);}
        
                if ( GsuArray.get(i).GetType().equals("KingGoomba")){
                    KingGoombadonation += GsuArray.get(i).GetDonation();}
                
                if ( GsuArray.get(i).GetType().equals("ParaGoomba")){
                    ParaGoombadonation += GsuArray.get(i).GetDonation();}   
               
            }
            // print out everything
            System.out.println("Goomba donated $"+Goombadonation + "dollars");
            System.out.println("ParaGoomba donated $"+ParaGoombadonation + "dollars");
            System.out.println("KingGoomba donated $"+KingGoombadonation + "dollars");
            csvreader.close();//close the csv reader to avoid errors
            
         }
        
    
            catch(Exception ee){
                System.out.println(ee.getMessage());
            }

        }
        if(butText.equals("Goomba")){
            
            tp.SetText("Type Goomba donated : $"+String.valueOf(Goombadonation+" dollars."));
            
        }
        else if(butText.equals("ParaGoomba")){
            tp.SetText("Type ParaGoomba donated : $"+String.valueOf(ParaGoombadonation+" dollars."));
            
        }
        else if(butText.equals("KingGoomba")){
            tp.SetText(String.valueOf("Type KingGoomba donated : $"+KingGoombadonation+" dollars."));
        }
    }}}

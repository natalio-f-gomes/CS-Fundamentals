import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.util.ArrayList;
import java.awt.event.ActionEvent;

public class ActionHandler {
    private TextPart tp;
    private ButtonPart bp;
    private ArrayList<String> equation;
    private String numbText;
    public ActionHandler(TextPart tp, ButtonPart bp){
        this.tp = tp;
        this.bp = bp;//alleader contains all added buttons. for now
        //AddListenerstoButtons();
        this.equation = new ArrayList<String>();
        this.numbText = "";
    }
    public void AddListenerstoButtons(){
        Listener listener = new Listener();
        for (JButton eachB:bp.GetButtonArrList()){
            eachB.addActionListener(listener);
        }
    }
    private class Listener implements ActionListener{
        @Override
        public void actionPerformed(ActionEvent e){
        JButton but = (JButton) e.getSource();
        String butText = but.getText();
        if (butText.equals("C")){
            //code for c
            equation.clear();
            tp.clearTextfield();
            numbText = "";
        }
        else if(butText.equals("=")){
            equation.add(numbText);
            //tp.setTextField("=");//empty field
            Double firstNumb = Double.parseDouble(equation.get(0));
            Double secondNumb = Double.parseDouble(equation.get(2));
            String op = equation.get(1);
            String result = "";
            
            
            if (op.equals("+")){
                result = String.valueOf(firstNumb+secondNumb);
            }
            else if (op.equals("-")){
                result = String.valueOf(firstNumb-secondNumb);
            }
            else if (op.equals("/")){
                result = String.valueOf(firstNumb/secondNumb);
            }
            else if (op.equals("*")){
                result = String.valueOf(firstNumb*secondNumb);
            }
            tp.GetTextField().setText(result);
            equation.clear();
            numbText = "";

            //Get whatever is in the textbox and save it
            String sec_equation = tp.GetTextField().getText();
            numbText += sec_equation;
        }
               
        else if(butText.equals("-")||(butText.equals("+"))||(butText.equals("/"))||(butText.equals("*"))){
            //operators
            equation.add(numbText);
            equation.add(butText);
            String eqSoFar = tp.GetTextField().getText();
            tp.GetTextField().setText(eqSoFar+butText);
            numbText = "";  
        }
        else{
            //numbers
            if(equation.size()==0 && numbText.isEmpty()){
                //will start new equation
                tp.clearTextfield();
                
                if (tp.GetTextField().getText().isEmpty()==false){
                    String new_equation = tp.GetTextField().getText();
                    numbText += new_equation;
                }
            }
            numbText += butText;
            String equationsoFar = tp.GetTextField().getText();
            tp.GetTextField().setText(equationsoFar+butText);
        }
        }
    }  
}

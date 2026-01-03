import javax.swing.JButton;
import javax.swing.JPanel;
import java.awt.GridLayout;
import java.util.ArrayList;
import java.awt.Color;

public class ButtonPart {
    private JPanel buttonpart;
    private GridLayout gl;
    private ArrayList<JButton> buttonlist;
    public ButtonPart(){
        this.buttonpart = new JPanel();
        this.gl = new GridLayout(0,4);
        this.buttonpart.setLayout(gl);
        this.buttonlist = new ArrayList<JButton>();
        this.buttonpart.setBounds(8,90,270,235);
        this.buttonpart.setBackground(Color.red);

        AddButtons();
        
    }
    public ArrayList<JButton> GetButtonArrList(){
        return this.buttonlist;
    }

    public JPanel GetButtonPart(){
        return this.buttonpart;
    }
    private void AddButtons(){
        JButton C = new JButton("C");
        this.buttonpart.add(C);
        this.buttonlist.add(C);

        JButton Devide = new JButton("/");
        this.buttonpart.add(Devide);
        this.buttonlist.add(Devide);

        JButton Time = new JButton("*");
        this.buttonpart.add(Time);
        this.buttonlist.add(Time);

        JButton equals = new JButton("=");
        this.buttonpart.add(equals);
        this.buttonlist.add(equals);

        JButton seven = new JButton("7");
        this.buttonpart.add(seven);
        this.buttonlist.add(seven);

        JButton eight = new JButton("8");
        this.buttonpart.add(eight);
        this.buttonlist.add(eight);

        JButton nine = new JButton("9");
        this.buttonpart.add(nine);
        this.buttonlist.add(nine);

        JButton plus = new JButton("+");
        this.buttonpart.add(plus);
        this.buttonlist.add(plus);

        JButton four = new JButton("4");
        this.buttonpart.add(four);
        this.buttonlist.add(four);

        JButton five = new JButton("5");
        this.buttonpart.add(five);
        this.buttonlist.add(five);

        JButton six = new JButton("6");
        this.buttonpart.add(six);
        this.buttonlist.add(six);

        JButton minus = new JButton("-");
        this.buttonpart.add(minus);
        this.buttonlist.add(minus);

        JButton one = new JButton("1");
        this.buttonpart.add(one);
        this.buttonlist.add(one);

        JButton two = new JButton("2");
        buttonpart.add(two);
        this.buttonlist.add(two);

        JButton three = new JButton("3");
        this.buttonpart.add(three);
        this.buttonlist.add(three);

        JButton zero = new JButton("0");
        this.buttonpart.add(zero);
        this.buttonlist.add(zero);
    }
}
    



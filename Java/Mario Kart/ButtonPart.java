
import javax.swing.JButton;
import javax.swing.JPanel;
import java.awt.GridLayout;
import java.util.ArrayList;

public class ButtonPart {
    private JPanel buttonpart;
    private GridLayout gl;
    private ArrayList<JButton> buttonlist;
    public ButtonPart(){
        this.buttonlist = new ArrayList<JButton>();
        this.buttonpart = new JPanel();
        this.gl = new GridLayout(0,2);
        this.buttonpart.setLayout(gl);
        this.buttonpart.setBounds(8,270,350,100);
        
        AddButtons();
        
    }
    public ArrayList<JButton> GetButtonArrList(){
        return this.buttonlist;
    }
    public JPanel GetButtonPart(){
        return this.buttonpart;
    }
    private void AddButtons(){
        JButton OpenCSV = new JButton("Open CSV");
        this.buttonpart.add(OpenCSV);
        this.buttonlist.add(OpenCSV);

        JButton GoombaButton = new JButton("Goomba");
        this.buttonpart.add(GoombaButton);
        this.buttonlist.add(GoombaButton);

        JButton PGButton = new JButton("ParaGoomba");
        this.buttonpart.add(PGButton);
        this.buttonlist.add(PGButton);

        JButton KGButton = new JButton("KingGoomba");
        this.buttonpart.add(KGButton);
        this.buttonlist.add(KGButton);

}}

import javax.swing.JTextArea;
import java.awt.Font;
import java.awt.Color;

public class TextPart {
    private JTextArea textfield;
    private int x,y,w,h;
    
    public TextPart(){
        this.textfield = new JTextArea();
        this.x = 8;
        this.y = 10;
        this.w = 350;
        this.h = 250;
        this.textfield.setBounds(x,y,w,h);
        this.textfield.setBackground(Color.white);
        this.textfield.setFont(new Font("Arial", Font.BOLD, 25));
        this.textfield.setText("This part is JTextArea\nyou will print info of CSV\nin multiple lines here.");

        this.textfield.setLineWrap(true);
        
    }
    public JTextArea GetTextField(){
        return this.textfield;
    }
    public void SetText(String donation){
        this.textfield.setText(donation);;
    }
    
}

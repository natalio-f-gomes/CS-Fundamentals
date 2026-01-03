import java.awt.*;
import javax.swing.*;

public class TextPart {
    private JTextField textfield;
    private int x,y,w,h;
    public TextPart(){
        this.textfield = new JTextField();
        this.x = 8;
        this.y = 10;
        this.w = 270;
        this.h = 70;
        this.textfield.setBounds(x,y,w,h);
        this.textfield.setBackground(Color.white);
        this.textfield.setFont(new Font("Arial", Font.BOLD, 50));
        this.textfield.setHorizontalAlignment(JTextField.RIGHT);
    }
    public JTextField GetTextField(){
        return this.textfield;
    }
    public void setTextField(String x){
        this.textfield.setText(x);;
}
    public void clearTextfield(){
        this.textfield.setText("");
    }
}

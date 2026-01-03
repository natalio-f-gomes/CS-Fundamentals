
import javax.swing.JFrame;

public class App {
    public static void main(String[] args) throws Exception {

        JFrame mainwindow = new JFrame();
        mainwindow.setLayout(null);

        TextPart tp =  new TextPart();
        ButtonPart bp = new ButtonPart();
        mainwindow.add(tp.GetTextField());
        mainwindow.add(bp.GetButtonPart());

        ActionHandler ah = new ActionHandler(tp, bp);
        ah.AddListenerstoButtons();
        
        mainwindow.setTitle("Calculator");
        mainwindow.setSize(300,370);
        mainwindow.setLocationRelativeTo(null);//pop up on center of screen
        mainwindow.setResizable(false);//not resisable 
        mainwindow.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);//terminate java program
        mainwindow.setVisible(true);//visible to the users
    }
}

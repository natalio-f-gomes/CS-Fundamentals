import javax.swing.JFrame;
public class App {
    public static void main(String[] args) {

        JFrame window = new JFrame();

        ButtonPart bp = new ButtonPart();
        TextPart tp = new TextPart();
        window.add(tp.GetTextField());
        window.add(bp.GetButtonPart());
        Actionhandler ah = new Actionhandler(tp, bp);
        ah.AddListenerstoButtons();

        window.setSize(365,400);
        window.setLayout(null);
        window.setResizable(false);
        window.setTitle("Mario Kart");
        window.setVisible(true);
        window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

    }
}

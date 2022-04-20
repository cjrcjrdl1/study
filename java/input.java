import javax.swing.*;

public class input {

    public static void main(String[] args) {

        String id = JOptionPane.showInputDialog("Enter a ID");
        String age = JOptionPane.showInputDialog("Enter your age");

        System.out.println(id);
        System.out.println(age);
    }
}

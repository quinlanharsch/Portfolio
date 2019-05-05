import java.util.Scanner;
import java.util.Stack;

public class Project8 {
    public static void main(String[] Args){
        Scanner scan = new Scanner(System.in);
        Stack<Integer> stk = new Stack<>();
        System.out.println("Enter postfix equation: ");
        String uIn = scan.nextLine();
        char atI;
        String[] uLs = uIn.split(" ");
        boolean valid = true;
        for (String uL : uLs) {
            System.out.println(stk);
            switch (uL) {
                case "+":
                    if (stk.size() >= 2) {
                        stk.push(stk.pop() + stk.pop());
                    } else {
                        System.out.print("Error, cannot add. Invalid sequence.");
                        System.out.println(stk);
                        valid = false;
                    }
                    break;
                case "-":
                    if (stk.size() >= 2) {
                        stk.push(stk.pop() - stk.pop());
                    } else {
                        System.out.print("Error, cannot subtract. Invalid sequence.");
                        System.out.println(stk);
                        valid = false;
                    }
                    break;
                case "*":
                    if (stk.size() >= 2) {
                        stk.push(stk.pop() * stk.pop());
                    } else {
                        System.out.print("Error, cannot multiply. Invalid sequence.");
                        System.out.println(stk);
                        valid = false;
                    }
                    break;
                case "/":
                    if (stk.size() >= 2) {
                        stk.push(stk.pop() / stk.pop());
                    } else {
                        System.out.print("Error, cannot divide. Invalid sequence.");
                        System.out.println(stk);
                        valid = false;
                    }
                    break;
                default:
                    stk.push(Integer.parseInt(uL));
            }
        }
        if(valid){
            if(stk.size()==1){
                System.out.println(stk.pop());
            } else {
                System.out.println("Can't compute. Too few operands.");
                System.out.println(stk);
            }
        }
    }
}

import java.util.Scanner;

public class Checkpoint2 {
    public static void main(String args[]){
        Scanner s = new Scanner(System.in);
        System.out.print("Enter cat's age: ");
        int age = s.nextInt();
        if (age == 1) {
            System.out.println("Your cat is 15 in human years");
        } else if (age == 2) {
            System.out.println("Your cat is 24 in human years");
        } else {
            System.out.println("Your cat is "+(24+(age-2)*4)+" in human years");
        }
    }
}

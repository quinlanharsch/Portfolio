import java.util.Scanner;

public class Project1 {
    public static void main(String args[]) {
        Scanner s = new Scanner(System.in);
        System.out.print("Enter the student's name: ");
        String name = s.next();
        int n = 5;
        int max = 0;
        int min = 0;
        double avgTotal = 0.0;
        for(int i = 1; i <= n; i++) {
            System.out.print("Enter the Test " + i + " score: ");
            double current = s.nextInt();
            if (i == 1) {
                min = (int) current;
                max = (int) current;
            } else if (current < min) {
                min = (int) current;
            } else if (current > max) {
                max = (int) current;
            }
            avgTotal += current;
        }
        double avg = avgTotal / n;
        System.out.println("\n" + name + "'s Grade Report\n");
        System.out.println("Minimum Score: " + min);
        System.out.println("Maximum Score: " + max);
        System.out.println("Average Score: " + avg);
        if (avg>=90){
            System.out.println("Final Grade: A");
        } else if (avg>=80){
            System.out.println("Final Grade: B");
        } else if (avg>=70){
            System.out.println("Final Grade: C");
        } else if (avg>=60){
            System.out.println("Final Grade: D");
        } else {
            System.out.println("Final Grade: F");
        }

    }
}

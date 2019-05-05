import java.util.*;

public class Checkpoint7 {
    public static void main (String [] args) {
        PriorityQueue <Patient>p_ls = new PriorityQueue<Patient>();

        Scanner scan = new Scanner(System.in);
        boolean active = true;
        while(active){
            System.out.println("1. Add Patient, 2. See Patient, 3. Exit");
            int choice = scan.nextInt();

            switch (choice) {
                case 1:
                    System.out.println("Name:");
                    String n = scan.next();
                    System.out.println("Urgency:");
                    int u = scan.nextInt();
                    p_ls.add(new Patient(n, u));
                    break;
                case 2:
                    if(p_ls.isEmpty()){
                        System.out.println("There are no patients waiting to be seen.");
                    }else{
                        System.out.println("Patient " + p_ls.poll().name + " has been seen.");
                    }
                    break;
                case 3:
                    active = false;
                    break;
                default:
                    System.out.println("Invalid input");
                    break;
            }
        }
    }
}

class Patient implements Comparable<Patient> {
    String name;
    int urgency;

    public Patient (String name, int urgency) {
        this.name = name;
        this.urgency = urgency;
    }

    public int compareTo(Patient p) {
        String name1 = this.name;
        String name2 = p.name;
        int urgency1 = this.urgency;
        int urgency2 = p.urgency;
        if(urgency1 != urgency2){
            return urgency2 - urgency1;
        }else{
            return name1.compareTo(name2);
        }
    }

    public String toString() {
        return "Patient Name: " + this.name + ", Urgency: " + this.urgency;
    }
}

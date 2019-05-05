import java.util.*;

public class Checkpoint6 {
    public static void main(String[] args){
        ArrayList<String> aList = new ArrayList<>();
        Scanner scan = new Scanner(System.in);

        System.out.println("Type\n'list'\t to print the roster\n'add'\t to add a student\n'quit'\t to end it all");
        boolean active = true;
        while(active){
            String uIn = scan.next();
            switch(uIn){
                case "list":
                    Iterator<String> aIt = aList.iterator();
                    System.out.println("Current roster:");
                    if(aList.isEmpty())System.out.println("[empty]");
                    else while (aIt.hasNext()) System.out.println(aIt.next());
                    break;
                case "add":
                    System.out.println("Enter student name:");
                    uIn = scan.next();
                    aList.add(uIn);
                    System.out.println(uIn+" added.");
                    break;
                case "quit":
                    System.out.println("K thx bye.");
                    active = false;
                    break;
                default:
                    System.out.println("Type\n'list'\t to print the roster\n'add'\t to add a student\n'quit'\t to end it all");
            }
        }
    }
}

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Checkpoint8 {
    public static void main(String[] args) {
        HashMap<Character, Integer> hash = new HashMap<>();
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter string to count the number of each of it's characters it contains:");
        String uIn = scan.nextLine();
        for(int i=0; i<uIn.length(); i++){
            char c = uIn.charAt(i);
            if(hash.containsKey(c)){
                hash.replace(c, hash.get(c)+1);
            } else {
                hash.put(c, 1);
            }
        }
        System.out.println(hash.entrySet());
    }
}

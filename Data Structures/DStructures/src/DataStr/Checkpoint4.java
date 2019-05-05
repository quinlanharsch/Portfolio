import java.util.LinkedList;

public class Checkpoint4 {
    public static void main(String args[]){
        LinkedList<String> linky = new LinkedList<String>();
        linky.add("Java");linky.add("Python");linky.add("PHP");linky.add("C++");
        for (int i = 0; i<linky.size(); i++){
            System.out.print(linky.get(i)+" ");
        }
    }
}

package DataStr;

public class Checkpoint5 {
    public static void main(String[] Args){
        threeNPlusOne(4);
    }
    private static void threeNPlusOne(int n){
        if(n!=1){
            if (n%2==0){
                System.out.print(n +", ");
                threeNPlusOne(n/2);
            }else if(n%2==1){
                System.out.print(n +", ");
                threeNPlusOne(3*n+1);
            }
        }else{
            System.out.print(1);
        }
    }
}

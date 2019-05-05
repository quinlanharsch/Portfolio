import java.util.Scanner;

public class Project2 {
    public static void main(String[] args){
        int pScore = 0;
        int cScore = 0;
        while (pScore < 3 && cScore < 3){

            // player
            Scanner uin = new Scanner(System.in); // construct scanner
            String pPlay;
            char pThrow = 'z';
            boolean v = true;
            while(v){
                System.out.print("Rock, Paper, Scissors, Shoot! ");
                pPlay = uin.nextLine();
                switch (pPlay.toLowerCase()) {
                    case "rock":
                    case "r":
                        pThrow = 'r';
                        v = false;
                        break;
                    case "paper":
                    case "p":
                        pThrow = 'p';
                        v = false;
                        break;
                    case "scissors":
                    case "s":
                        pThrow = 's';
                        v = false;
                        break;
                    default:
                        System.out.println("You can only throw 'Rock' 'R', 'Paper' 'P', or 'Scissors' 'S' dummy.");
                        break;
                }
            }

            // 1337-AI
            int rngJesus = (int)(Math.random()*3);
            char[] options = new char[]{'r','p','s'};
            char cThrow = options[rngJesus];

            // Who won?
            System.out.println( pThrow+" vs "+cThrow );
            if (pThrow == cThrow){
                System.out.println("Tie!");
            } else if ((pThrow == 'r' && cThrow == 's')||
                       (pThrow == 's' && cThrow == 'p')||
                       (pThrow == 'p' && cThrow == 'r')){
                System.out.println("Player wins!");
                pScore++;
            } else {
                System.out.println("Computer wins!");
                cScore++;
            }
            System.out.println("Score is "+pScore+" to the computer's "+cScore);
        }

        // Announce best of 3
        if (pScore == 3){
            System.out.println("Player wins the game!");
        } else {
            System.out.println("Computer wins the game!");
        }
    }
}

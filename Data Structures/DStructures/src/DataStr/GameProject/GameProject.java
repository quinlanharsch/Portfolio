package GameProject;
import java.util.*;

public class GameProject {
    public static void main(String[] args){
        Random rand = new Random();
        Scanner scan = new Scanner(System.in);
        System.out.println("Quinn-lyn's Dungeon Drag\n" +
                "Once upon a time, in the land of the gays, a darkness began to consume \n" +
                "all in its path.  An evil Mike Pence commands an army of evangelicals from \n" +
                "the depths of the Conversion Therapy Camp.  \n" +
                "While things seemed bleak, not all was lost.  \n" +
                "From the town of Essex, a young gay wanders forth in search of \n" +
                "glory, riches, and fulfillment.\n" +
                "Name thy drag queen: ");
        String name = scan.nextLine();
        player p1 = new player(name);
        System.out.print(p1.getName()+" sashays around the main square of Essex.\n" +
                "Type the letter in quotes to select a location!\n");

        String destination = "town";
        String choice;

        boolean chooseQuit = false;
        while(!chooseQuit) {
            switch (destination.toLowerCase()) {
                case "town":
                    boolean choseTown = false;
                    while (!choseTown) {
                        System.out.println("go fight in the forest 'f'\ngo to the boutique 'b'\n" +
                                "go to Hamburger Mary's 'h'\nturn around and get some baeuty rest (quit) 'r'" +
                                "\ngo to the shrine of Ru Paul 's'\ngo storm the Conversion Therapy Camp 'c'");
                        choice = scan.nextLine();
                        switch (choice.toLowerCase()) {
                            case "f":
                            case "forest":
                                destination = "forest";
                                choseTown = true;
                                break;
                            case "b":
                            case "shop":
                                destination = "shop";
                                choseTown = true;
                                break;
                            case "shrine":
                            case "s":
                                destination = "shrine";
                                choseTown = true;
                                break;
                            case "bar":
                            case "h":
                                System.out.print("They're still cleaning up after the accident. " +
                                        "My girl flew too close to the sun.\n");
                                break;
                            case "c":
                            case "storm":
                                System.out.println("Type 'Mike Pence' if you're sure you want to fight the final boss");
                                String chooseBoss = scan.nextLine();
                                if (chooseBoss.equals("Mike Pence")) {
                                    destination = "boss";
                                    choseTown = true;
                                    break;
                                }
                                break;
                            case "rest":
                            case "quit":
                            case "r":
                            case "q":
                                destination = "bed";
                                choseTown = true;
                                break;
                            default:
                                System.out.print("Type the letter in quotes to select a location!\n");
                                break;
                        }
                    }
                    break;
                case "forest":
                    int type = rand.nextInt(3) + 1;
                    monster mon = new monster(type);
                    System.out.println("A wild evangelical " + mon.getName() + " has appeared.\nFight 'f', Heal 'h', or Run 'r'!");

                    boolean leaving = false;
                    while (!chooseQuit && !leaving) {
                        choice = scan.nextLine();
                        switch (choice.toLowerCase()) {
                            case "f":
                            case "fight":
                                int pHitMiss = rand.nextInt(10) + 1;
                                int hit = p1.weapon.getDamage();
                                if (pHitMiss < 8) {
                                    mon.setHP(mon.getHP() - hit);
                                    System.out.println(p1.getName() + " uses her " + p1.weapon.name + " to " + p1.weapon.atkTxt + " " + mon.getName() + " for "+hit+" damage.");
                                }
                                int mHitMiss = rand.nextInt(10) + 1;
                                if (mHitMiss < mon.getToHit()) {
                                    int mHit = mon.getDamage()-p1.armor.abs;
                                    if(mHit>0){
                                        p1.setHP(p1.getHP() - mHit);
                                        System.out.println(mon.getName() + " hit " + p1.getName() + " for "+mHit+" damage.");
                                    }else{
                                        System.out.println(mon.getName() + " hit " + p1.getName() + " but did no damage.");
                                    }
                                }
                                System.out.println(p1.getName() + ": " + p1.getHP() + "\t" + mon.getName() + ": " + mon.getHP());
                                break;

                            case "h":
                            case "heal":
                                if (p1.getPotions() > 0) {
                                    p1.setPotions(p1.getPotions() - 1);
                                    if (p1.getHP() >= p1.getMaxHP() - 8) {
                                        p1.setHP(p1.getMaxHP());
                                    } else {
                                        p1.setHP(p1.getHP() + 8);
                                    }
                                    System.out.println("Healed 8 hp! " + p1.getName() + " now has " + p1.getHP() + " hp!");
                                } else {
                                    System.out.println("Out of Potions!");
                                }
                                break;

                            case "r":
                            case "run":
                                destination = "town";
                                leaving = true;
                                break;
                        }
                        if (p1.isDead()) {
                            System.out.println("GAME OVER");
                            chooseQuit = true;
                        }
                        if (mon.isDead()) {
                            p1.setXP(p1.getXP() + mon.getXP());
                            p1.setGold(p1.getGold() + mon.getGold());
                            p1.levelCheck();
                            System.out.println("You beat him get " + mon.getXP() + " xp and " + mon.getGold() + "g. You have " + p1.getXP() + " xp and " + p1.getGold() + " gold.\n");
                            leaving = true;
                        }
                    }
                    if (leaving) destination = "town";
                    break;
                case "boss":
                    pence boss = new pence();
                    System.out.println("You have arrived at the house of the gay and God fearing christian, Mike Pence!");
                    while (!chooseQuit) {
                        choice = scan.nextLine();
                        switch (choice.toLowerCase()) {
                            case "f":
                            case "fight":
                                int pHitMiss = rand.nextInt(10) + 1;
                                int hit = p1.weapon.getDamage();
                                if (pHitMiss < 8) {
                                    boss.setHP(boss.getHP() - hit);
                                    System.out.println(p1.getName() + " uses her " + p1.weapon.name + " to " + p1.weapon.atkTxt + " Mike Pence for "+hit+" damage.");
                                }
                                int mHitMiss = rand.nextInt(10) + 1;
                                if (mHitMiss < 9) {
                                    int mHit = 10-p1.armor.abs;
                                    if(mHit>0){
                                        p1.setHP(p1.getHP() - mHit);
                                        System.out.println(boss.getName() + p1.getName() + " for "+mHit+" damage.");
                                    }else{
                                        System.out.println(boss.getName() + " hit " + p1.getName() + " but did no damage.");
                                    }
                                }
                                System.out.println(p1.getName() + ": " + p1.getHP() + "\tPence: " + boss.getHP());
                                break;

                            case "h":
                            case "heal":
                                if (p1.getPotions() > 0) {
                                    p1.setPotions(p1.getPotions() - 1);
                                    if (p1.getHP() >= p1.getMaxHP() - 8) {
                                        p1.setHP(p1.getMaxHP());
                                    } else {
                                        p1.setHP(p1.getHP() + 8);
                                    }
                                    System.out.println("Healed 8 hp! " + p1.getName() + " now has " + p1.getHP() + " hp!");
                                } else {
                                    System.out.println("Out of Potions!");
                                }
                                break;

                            case "r":
                            case "run":
                                System.out.println("You can't run from Mike 'Turn those Fruits into Vegetables' Pence");
                                break;
                        }
                        if (p1.isDead()) {
                            System.out.println("You are straight now...\n" +
                                    "A fate worse than death...\n" +
                                    "GAME OVER");
                            chooseQuit = true;
                        }
                        if (boss.isDead()) {
                            p1.setXP(p1.getXP() + 10000);
                            while (p1.getXP() >= 10 * Math.pow(2, p1.getLevel())) {
                                p1.levelCheck();
                            }
                            System.out.println("You beat Mike 'Pray the Gay Away' Pence and got 10000 xp and [aprox. 1 rich white dude's woth]g. You have " + p1.getXP() + " xp and unlimited gold.\n" +
                                    "Also, you saved Essex from yet another threat to gaykind! Yay!\n" +
                                    "YOU WIN!!!");
                            chooseQuit = true;
                        }
                    }
                    break;
                case "shop":
                    System.out.println("You see a small womanoid goblin in 7in heels standing on a stool behind the counter\n" +
                            "'Whatch you want?' she snarls");
                    boolean choseShop = false;
                    while (!choseShop) {
                        System.out.println("You heve "+p1.getGold()+" in your coin purse." +
                                "Potions\t20g\t'p'\n" +
                                "Weapons:" +
                                "Sword\t1-4 damage\t300g\t1" +
                                "Naughty Words\t1-8 damage\t900g\t2" +
                                "Inappropriate Etiquette\t1-16 damage\t2700g\t3" +
                                "Armor:" +
                                "Flats\t1 defense\t500g\t4" +
                                "Heels\t2 defense\t1500g\t5" +
                                "Pumps\t4 defense\t3500g\t6" +
                                "Leave\t\t'l'");
                        String shopChoice = scan.nextLine();
                        switch (shopChoice.toLowerCase()) {
                            case "1":
                                if (p1.getGold() >= 300) {
                                    p1.weapon = new weapon("Sword","slashes at",4,300);
                                    p1.setGold(p1.getGold() - 300);
                                } else {
                                    System.out.println("'You poor or something? Swords ain't cheap.'");
                                }
                                break;
                            case "2":
                                if (p1.getGold() >= 900) {
                                    p1.weapon = new weapon("Swears","curses at",8,900);
                                    p1.setGold(p1.getGold() - 900);
                                } else {
                                    System.out.println("'I aint givin' ya the gift of the gab fer free, honey.'");
                                }
                                break;
                            case"3":
                                if (p1.getGold() >= 2700) {
                                    p1.weapon = new weapon("Bad Touch","seduces",16,2700);
                                    p1.setGold(p1.getGold() - 2700);
                                } else {
                                    System.out.println("'Seduction is an art. And art ain't free.'");
                                }
                                break;
                            case"4":
                                if (p1.getGold() >= 500) {
                                    p1.armor = new armor("Flats",1,500);
                                    p1.setGold(p1.getGold() - 500);
                                } else {
                                    System.out.println("'You'll have to make do goin' barefoot'");
                                }
                                break;
                            case"5":
                                if (p1.getGold() >= 1500) {
                                    p1.armor = new armor("Heels",2,500);
                                    p1.setGold(p1.getGold() - 1500);
                                } else {
                                    System.out.println("'You could barely even handle the flats, hun! Hahaha! Maybe when you're ready.'");
                                }
                                break;
                            case"6":
                                if (p1.getGold() >= 3500) {
                                    p1.armor = new armor("Pumps",4,500);
                                    p1.setGold(p1.getGold() - 3500);
                                } else {
                                    System.out.println("'Maybe one day your heels will be as tall as mine, darlin'. Not today, though. Heh heh.'");
                                }
                                break;
                            case "p":
                                if (p1.getGold() >= 20) {
                                    p1.setPotions(p1.getHP() + 1);
                                    p1.setGold(p1.getGold() - 20);
                                } else {
                                    System.out.println("'You poor or something? I said 20g!'");
                                }
                                break;
                            case "l":
                                System.out.println("'Buh-bye, hun'");
                                choseShop = true;
                                destination = "town";
                                break;
                            default:
                                System.out.println("You want what!? Ain't got that, hun.' she snarls");
                                break;
                        }
                    }
                    break;
                case "shrine":
                    System.out.println("It costs 10g to heal at the shrine of the mighty Ru\n" +
                            "How much do you want to heal (10g/hp)?");
                    int heal = scan.nextInt();
                    if (p1.getGold() >= 10 * heal) {
                        p1.setHP(p1.getHP() + heal);
                        p1.setGold(p1.getGold() - (10 * heal));
                        System.out.println("Healed " + heal + " for " + 10 * heal + " gold.");
                    } else {
                        System.out.println("The Statue speaks 'This a church, not a charity'");
                    }
                    destination = "town";
                    break;
                case "bed":
                    chooseQuit = true;
                    break;
            }
        }
        System.out.println("You had " + p1.getGold() + "g\n");
        System.exit(0);
    }
}



package GameProject;
import java.util.*;

public class player {
    private String name;
    private int level;
    private int XP;
    private int maxHP;
    private int HP;
    private int gold;
    private int potions;
    public weapon weapon;
    public armor armor;

    player(String name){
        this.name = name;
        this.level = 1;
        this.XP = 0;
        this.maxHP = 20;
        this.HP = 20;
        this.gold = 100;
        this.potions = 0;
        weapon = new weapon("Pointy Stick", "poke at", 1, 0);
        armor = new armor("Shaggy Drag", 0, 0);
    }

    //Name
    public void setName(String n) {
        name = n;
    }
    public String getName() {
        return name;
    }

    //Level
    public void setLevel(int l) {
        level = l;
    }
    public int getLevel() {
        return level;
    }
    public void levelCheck(){
        if(XP==10*Math.pow(2, level)) {
            System.out.println("Level up! You're now lv"+level);
            level++;
            HP += 10;
        }
    }

    //XP
    public void setXP(int x) {XP = x;}
    public int getXP() {return XP;}

    //Max HP
    public void setMaxHP(int m) {maxHP = m;}
    public int getMaxHP() {return maxHP;}

    //HP
    public void setHP(int h) {HP = h;}
    public int getHP() {return HP;}
    public boolean isDead(){return HP == 0;}

    //Gold
    public void setGold(int g) {gold = g;}
    public int getGold() {return gold;}

    //Potions
    public void setPotions(int p) {potions = p;}
    public int getPotions() {return potions; }
    public boolean hasPtions(){return potions > 0;}

    //Weapon
    public Object getWeapon(){return weapon;}
}

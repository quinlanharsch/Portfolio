package GameProject;

import java.util.Random;

public class weapon {
    public String name;
    private int damage;
    public int gold;
    public String atkTxt = "pokes at";

    weapon(String weaponName, String attackText, int damageVal, int cost){
        this.name = weaponName;
        this.damage = damageVal;
        this.gold = cost;
        this.atkTxt = attackText;
    }

    public int getDamage() {
        Random rand = new Random();
        return rand.nextInt(damage) + 1;
    }
}

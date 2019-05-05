package GameProject;
public class monster {
    private int maxHP;
    private int HP;
    private String name;
    private int toHit;
    private int damage;
    private int XP;
    private int gold;

    monster(int type){
        switch (type){
            case 1:
                this.name = "Tex";
                this.maxHP = 4;
                this.HP = 4;
                this.toHit = 8;
                this.damage = 1;
                this.XP = 20;
                this.gold = 20;
            case 2:
                this.name = "Rex";
                this.maxHP = 8;
                this.HP = 8;
                this.toHit = 4;
                this.damage = 2;
                this.XP = 30;
                this.gold = 10;
            case 3:
                this.name = "Dex";
                this.maxHP = 5;
                this.HP = 5;
                this.toHit = 2;
                this.damage = 3;
                this.XP = 20;
                this.gold = 15;
        }


    }

    //Name
    public void setName(String n) {this.name = n;}
    public String getName() {return name;}

    //Max HP
    public void setMaxHP(int m) {this.maxHP = m;}
    public int getMaxHP() {return maxHP;}

    //HP
    public void setHP(int h){this.HP = h;}
    public int getHP(){return HP;}
    public boolean isDead(){return HP == 0;}

    //toHit
    public void setToHit(int t) {this.toHit = t;}
    public int getToHit() {return toHit;}

    //damage
    public void setDamage(int d) {this.damage = d;}
    public int getDamage() {return damage;}

    //XP
    public void setXP(int x) {this.XP = x;}
    public int getXP() {return XP;}

    //gold
    public void setGold(int g) {this.gold = g;}
    public int getGold() {return gold;}
}

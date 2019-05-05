package GameProject;

public class pence {
    private int maxHP;
    private int HP;
    private String name;

    pence(){
        this.name = "Mike Pence";
        this.maxHP = 40;
        this.HP = 40;
    }

    //Name
    public void setName(String n) {
        this.name = n;
    }
    public String getName() {
        return name;
    }

    //Max HP
    public void setMaxHP(int m) {
        this.maxHP = m;
    }
    public int getMaxHP() {
        return maxHP;
    }

    //HP
    public void setHP(int h) {
        this.HP = h;
    }
    public int getHP() {
        return HP;
    }
    public boolean isDead(){
        return HP == 0;
    }
    // in future could use `class [monster name] extends monster` to make more monster subclasses
}

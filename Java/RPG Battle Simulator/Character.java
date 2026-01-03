import java.util.Random;
public class Character{
    public String characterType;
    public int healthPoints, attackStrenth, defenseStrngth;
    public Character(String t){
        Random rand = new Random();
        this.characterType = t;
        this.healthPoints = rand.nextInt(10,50);
        this.attackStrenth = rand.nextInt(10,100);
        this.defenseStrngth = rand.nextInt(1,10);

    }

 
    public Character(String type,int healthLimit ){
        Random rand = new Random();
        this.characterType = type;
        this.healthPoints = rand.nextInt(10,healthLimit);
        this.attackStrenth = rand.nextInt(10,100);
        this.defenseStrngth = rand.nextInt(1,10);
    }
    public String getType()   {
        return this.characterType;
    }
    public int getHealthPoints(){
        return this.healthPoints;
    }
    public int getAttackStrength(){
        return this.attackStrenth;
    }
    public int getDefenseStrength(){
        return this.defenseStrngth;
    }
    public void setType(String type) {
        
    }
    public void setHealthPoints(int hp) {
        if (hp < 0) {
            this.healthPoints = 0;
        } else {
            this.healthPoints = hp;
        }
    }
    public void setAttackStrength(int as) {
        
    }
    public void setDefenseStrength(int ds) {
        
    }
    public void attack(Character target){
        System.out.println("The " + this.characterType + " tries to attack the " + target.getType() + "!");
        int damage = this.attackStrenth/ target.attackStrenth;
        System.out.println("The " + target.getType() + " takes " + damage + " points  of damage.");
        target.healthPoints -= damage;
    }
    public void printStats(){
        System.out.println("  -- "+this.characterType+ "--\n" +
                "             Health: "+ this.healthPoints +"\n" +
                "             Attack Str: "+ this.attackStrenth +"\n" +
                "             Defense Str: "+ this.defenseStrngth +"\n");
        if (this.healthPoints<1){
            System.out.println("-- DEFEATED -–");
        }
    }


}

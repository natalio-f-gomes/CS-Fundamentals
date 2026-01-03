import java.util.Random;
import java.util.Scanner;
public class Main{
    public static void main(String[] args) throws InterruptedException{

        Scanner user_in = new Scanner(System.in);
        System.out.println("""
        ----------------------------------------
        \tWelcome to the BATTLE SIMULATOR!
        ----------------------------------------
        """);
        System.out.print("How many monsters would you like to battle?\nA:");
        int numMonsters = user_in.nextInt();
        //createMonsterList(numMonsters);

        Character[] monsterList = createMonsterList(numMonsters);
        System.out.println("Here are your monsters: ");
        for (Character i : monsterList){
            i.printStats();
        }
        System.out.println("Press ENTER to create a HERO...");
        // wait for user to press ENTER...
        user_in.nextLine();
        Character newHero = new Character("HERO", 301);
        newHero.printStats();
        System.out.println("Press ENTER to begin the battle simulation...");
        // wait for user to press ENTER...
        user_in.nextLine();

        while (newHero.getHealthPoints() > 0 && !enemiesDefeated(monsterList)) {
            Character enemy = getRandomEnemy(monsterList);
            newHero.attack(enemy);
            //Thread.sleep(500);

            System.out.println("\n...");
            for(Character i: monsterList ){
                if(i.healthPoints>0){
                    i.attack(newHero);
                    System.out.println("...");
                }
            }
            printCharacterStats(newHero,monsterList);
    }
        endGame(newHero);




    }
    private static boolean enemiesDefeated(Character[] enemyList) {

        for(Character i: enemyList){
            if(i.healthPoints>0){
                return false;
            }

        }
        return true;
    }
    private static Character getRandomEnemy(Character[] enemyList) {
        // crate a new Random() object from the Java Random class
        Random randGen = new Random();

        // create a counter int and initialize it to 0
        int checkCount = 0;
        while(checkCount<enemyList.length){
            int randNum = randGen.nextInt( enemyList.length);
            Character monster = enemyList[randNum];
            if (monster.healthPoints>0){
                return monster;
            }
            checkCount++;

        }
        return  null;


    }
    private static Character[] createMonsterList(int numMonsters) {
        Character[] monsterList = new Character[numMonsters];
        for(int i =0; i < monsterList.length;i++){

            String monsterNameId = "MONSTER " + (i + 1);
            Character newMonster = new Character(monsterNameId);
            monsterList[i]= newMonster;
        }
        return monsterList;


    }
    private static void endGame(Character heroObj) {
        System.out.println("\n---------------------------------------------------------------");
        if(heroObj.healthPoints<=0){
            System.out.println("THE HERO HAS BEEN DEFEATED -- GAME OVER!");
        }else{
            System.out.println("VICTORY! -- THE HERO HAS DEFEATED ALL THE MONSTERS!");
        }

        System.out.println("---------------------------------------------------------------");
    }
    private static void printCharacterStats(Character heroObj, Character[] monsterList)
    { System.out.println("\n --- CURRENT STATS --- \n");

    System.out.println("\n------------------");
    heroObj.printStats();
    for(Character i: monsterList){
        if (i.getHealthPoints() > 0) {
            i.printStats();
            System.out.println();
        }
    }
    }

}

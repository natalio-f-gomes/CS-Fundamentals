import java.util.Arrays;

public class Main {
    public static void main(String[] args) {

        int[][] array = new int[4][];


        array[0] = new int[4];
        array[1] = new int[3];
        array[2] = new int[2];
        array[3] = new int[6];

        for (int i = 0 ;i < array.length ; i ++){
            for (int j = 0;j < array[i].length-1; j++){
                array[i][j] = (int)(Math.random()*10);

            }
        }

        for(int[] i: array){

            for (int j: i){
                System.out.print(j+ " ");
            }
            System.out.println();

        }









    }
}
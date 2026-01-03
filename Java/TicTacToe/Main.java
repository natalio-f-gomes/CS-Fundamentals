import java.util.Scanner;

public class Main{
    public static void main(String[] args) {
        String[] board_row_1 = {"1","2","3"};
        String[] board_row_2 = {"4","5","6"};
        String[] board_row_3 = {"7","8","9"};
        String[] allBoard = {"1","2","3","4","5","6","7","8","9"};
        Scanner user_in = new Scanner(System.in);
        String currentPlayer = "O";
        while(true){
            for(int i=0;i<3;i++){
                System.out.print(board_row_1[i]);
            } 
            System.out.println();
            for(int i=0;i<3;i++){
                System.out.print(board_row_2[i]);
            }  
            System.out.println();
            for(int i=0;i<3;i++){
                System.out.print(board_row_3[i]);
            }    
            System.out.println();         
            System.out.print("Choose a spot: ");
            int spot = user_in.nextInt();

            if (spot <= 3) {
                board_row_1[spot - 1] = handlePlayer(currentPlayer);
                allBoard[spot-1] = handlePlayer(currentPlayer);;
                currentPlayer = handlePlayer(currentPlayer);
                String next_player = currentPlayer;
            } else if (spot > 3 && spot <= 6) {
                board_row_2[spot - 4] = handlePlayer(currentPlayer);
                allBoard[spot-1] = handlePlayer(currentPlayer);;
                currentPlayer = handlePlayer(currentPlayer);
                String next_player = currentPlayer;
            } else if (spot > 6 && spot <= 9) {
                board_row_3[spot - 7] = handlePlayer(currentPlayer);
                allBoard[spot-1] = handlePlayer(currentPlayer);;
                currentPlayer = handlePlayer(currentPlayer);
                String next_player = currentPlayer;
            } else {
                System.out.println("Invalid Spot");
            }
            if((allBoard[0] == currentPlayer &&  allBoard[1] == currentPlayer && allBoard[2] == currentPlayer)
            || (allBoard[3] == currentPlayer &&  allBoard[4] == currentPlayer && allBoard[5] == currentPlayer)
            || (allBoard[6] == currentPlayer &&  allBoard[7] == currentPlayer && allBoard[8] == currentPlayer)
            || (allBoard[0] == currentPlayer &&  allBoard[3] == currentPlayer && allBoard[6] == currentPlayer)
            || (allBoard[2] == currentPlayer &&  allBoard[4] == currentPlayer && allBoard[7] == currentPlayer)
            || (allBoard[2] == currentPlayer &&  allBoard[5] == currentPlayer && allBoard[8] == currentPlayer)
            || (allBoard[0] == currentPlayer &&  allBoard[4] == currentPlayer && allBoard[8] == currentPlayer)
            || (allBoard[2] == currentPlayer &&  allBoard[4] == currentPlayer && allBoard[6] == currentPlayer))
            {
                System.out.print(currentPlayer + " Player Won ");
                break;
            }
            
        }
        
    }
    public static String handlePlayer(String Player){
        if (Player =="X"){
            return "O";
        }return "X";
    }

}

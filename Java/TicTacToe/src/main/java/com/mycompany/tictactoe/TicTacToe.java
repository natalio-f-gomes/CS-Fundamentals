/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.tictactoe;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JButton;
import javax.swing.JLabel;
import java.awt.Dimension;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Map;
import java.util.HashMap;

/**
 *
 * @author Natalio Gomes
 */
public class TicTacToe {
    private static String currentPlayer = "O";
    private static Map<String, Integer> gameHistory = new HashMap<>();
    public static void main(String[] args) {
        JButton[] bottonList = new JButton[9];
        String[] playBoard = new String[9];
        
        gameHistory.put("O", 0);
        gameHistory.put("X", 0);
        gameHistory.put("Draws", 0);
        
        for(int i=0;i<9;i++){ playBoard[i] = ""; }
        
        JFrame frame= new JFrame("Hello");
        JPanel panel = new JPanel();
        panel.setLayout(null);
        panel.setPreferredSize(new Dimension(500,300));
        
        JLabel playersTurn = new JLabel(currentPlayer + " turn");
        playersTurn.setBounds(350,0, 50,100);
        panel.add(playersTurn);
        
        JLabel gameStatus = new JLabel();
        gameStatus.setBounds(350,180, 100,100);
        panel.add(gameStatus);
        
        JLabel xHistoryLabel = new JLabel();
        xHistoryLabel.setBounds(350,210, 100,100);
        panel.add(xHistoryLabel);
        
        JLabel oHistoryLabel = new JLabel();
        oHistoryLabel.setBounds(350,220, 100,100);
        panel.add(oHistoryLabel);
        
        JLabel drawHistoryLabel = new JLabel();
        drawHistoryLabel.setBounds(350,230, 100,100);
        panel.add(drawHistoryLabel);
        
        
        
        int x =0;
        int y = 0;
        
        System.out.println(gameHistory.get("X"));
        
        int index = 0;
        for(int row=0;row<3;row++){
            for(int column=0;column<3;column++){
                
                final int buttonIndex = index;
                System.out.println("Button Index " + buttonIndex);
                bottonList[buttonIndex] = new JButton("");
                bottonList[buttonIndex].setBounds(x,y,100,100);
                bottonList[buttonIndex].addActionListener(new ActionListener(){
                    @Override
                    public void actionPerformed(ActionEvent event){
                        System.out.println("Button " + buttonIndex + " was clicked");
                        System.out.println(currentPlayer);
                        
                        xHistoryLabel.setText("X wins: "+ gameHistory.get("X").toString());
                        oHistoryLabel.setText("O wins: "+ gameHistory.get("O").toString());
                        drawHistoryLabel.setText("Draws: "+ gameHistory.get("Draws").toString());
                        
                        if(bottonList[buttonIndex].getText().equals("") && playBoard[buttonIndex].equals("") ){
                        bottonList[buttonIndex].setText(currentPlayer);
                            playBoard[buttonIndex] = currentPlayer;
                            System.out.println(buttonIndex + " "+playBoard[buttonIndex]);
                            String status = checkGameStatus(playBoard, currentPlayer);
                            gameStatus.setText(status);
                            currentPlayer = getPlayer(currentPlayer);
                            playersTurn.setText(currentPlayer+ " turn");
                        }else{
                            gameStatus.setText("Already Chosen");
                        }
                        
                    }
            });
                index++;
                x += 100;
            }
            x = 0;
            y += 100;

        }
        
        
        JButton newGameButton = new JButton("New Game");
        newGameButton.setBounds(350,100, 100,50);
        newGameButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent event){
                for(int i=0;i<9;i++){
                    bottonList[i].setText("");
                     playBoard[i] = "";
                }
            }
        });

        
        for(JButton button: bottonList){
            panel.add(button);
        }
        
        panel.add(newGameButton);
        frame.add(panel);
        frame.pack();
        frame.setVisible(true);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
     
    }
    public static String checkGameStatus(String[] board, String player){
      
        //check diagonals
        if(board[0].equals(player) && board[4].equals(player) &&  board[8].equals(player)){
            gameHistory.put(player, gameHistory.getOrDefault(player, 0) +1);
            return player + " wins";}
        if(board[2].equals(player) && board[4].equals(player) &&  board[6].equals(player)){
            gameHistory.put(player, gameHistory.getOrDefault(player, 0) +1);
            return player + " wins";}
        
        //check rows
        if(board[0].equals(player) && board[1].equals(player) &&  board[2].equals(player)){
            gameHistory.put(player, gameHistory.getOrDefault(player, 0) +1);
            return player + " wins";}
        if(board[3].equals(player) && board[4].equals(player) &&  board[5].equals(player)){
            gameHistory.put(player, gameHistory.getOrDefault(player, 0) +1);
            return player + " wins";}
        if(board[6].equals(player) && board[7].equals(player) &&  board[8].equals(player)){
            gameHistory.put(player, gameHistory.getOrDefault(player, 0) +1);
            return player + " wins";}
        //check columns
        if(board[0].equals(player) && board[3].equals(player) &&  board[6].equals(player)){
            gameHistory.put(player, gameHistory.getOrDefault(player, 0) +1);
            return player + " wins";}
        if(board[1].equals(player) && board[4].equals(player) &&  board[7].equals(player)){
            gameHistory.put(player, gameHistory.getOrDefault(player, 0) +1);
            return player + " wins";}
        if(board[2].equals(player) && board[5].equals(player) &&  board[8].equals(player)){
            gameHistory.put(player, gameHistory.getOrDefault(player, 0) +1);
            return player + " wins";}
        //check draw
        //loop through the board, and if all spaces has been filled with x or o, its a draw
        boolean isDraw = true;
        for(String i: board){
            if(i.equals("")){
                isDraw = false;
            }
        }
        if(isDraw){
            gameHistory.put("Draws", gameHistory.getOrDefault(player, 0) +1);
            return "Draw";}
        return "";
    }
    
    public static String getPlayer(String player){
        if(player.equals("O")){return "X";}
        else{return "O";}
    }
    
}

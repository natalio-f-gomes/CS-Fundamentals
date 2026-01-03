package org.example;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args)  {
        try {
            Scanner scannerObj = new Scanner(new File("src/main/resources/Questions.csv"));
            Scanner choiceObj = new Scanner(System.in);
            ArrayList<Quiz> quizData = new ArrayList<>();



            int num = 0;
            while(scannerObj.hasNextLine()){
                String line = scannerObj.nextLine();
                num +=1;
                String[] parts = line.split(",");
                String prompt = parts[0];
                String[] choices = parts[1].split(";");
                String correctAnswer = parts[2];

                List<String> choicesArray = new ArrayList<>(List.of(choices));
                Collections.shuffle(choicesArray);

                System.out.println(prompt);
                for(String choice : choicesArray){
                    System.out.println(choice);
                }
                System.out.print("Answer: ");
                String userChoice = choiceObj.nextLine();
                System.out.println();
                Quiz quizObj = new Quiz(prompt, choices, correctAnswer, userChoice);
                quizData.add(quizObj);



            }
            int totalScore = 0;
            for(Quiz i:  quizData){
                 totalScore +=  i.getScore();
            }
            double percentageScore = (((double) totalScore / quizData.size()) * 100);
            System.out.println(totalScore);
            System.out.println("You got "+ totalScore + " out of " + quizData.size() + ".\n " + percentageScore + "%");



        }
        catch (FileNotFoundException e){
            System.out.println("File not Found! Please Enter the correct path.");
        }
        }
    }


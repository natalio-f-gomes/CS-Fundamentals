package org.example;

class  Quiz {
    private final String[] choices;
    private final String prompt, correctAnswer, userAnswer;
    private int score;

    public Quiz(String prompt, String[] choices, String correctAnswer, String userAnswer) {
        this.prompt = prompt;
        this.choices = choices;
        this.correctAnswer = correctAnswer;
        this.userAnswer = userAnswer;
        if (this.correctAnswer.equals(this.userAnswer)) {
            this.score += 1;
        } else {
            return;
        }

    }

    public int getScore() {
        return this.score;
    }

    public String[] getChoices() {
        return this.choices;
    }

    public String getPrompt() {
        return this.prompt;
    }

    public String getUser_answer() {
        return this.userAnswer;
    }

    public String getCorrect_answer() {
        return this.correctAnswer;
    }


}
from Question import questions

movie_prompt = [
    "What is the best korean Movie\n a)Parasite\n b)Memories of Murder\n c)I saw the Devil\n d)Mother\n\n",
    "What is the best Tarantino movie\n a)Django Uncheined\n b)Pulp Fiction\nc)Unglory Bastards\nd)The Hateful Height\n\n",
    "What is the best Scorcese movie\n a)Taxi driver\n b)The Irishman\n c)Shutter Island\n d)The Departed\n\n",
    "What is the best superhero movie of the last decade\n a)Avengers\n b)Doctor Strange\n c)Batman vs Superman\n b)Civil War\n\n",
]

answers = [
    questions(movie_prompt[0], "b"),
    questions(movie_prompt[1], "b"),
    questions(movie_prompt[2], "c"),
    questions(movie_prompt[3], "a"),
]


def movie_questions(questions):
    score = 0

    for questionaires in questions:
        user_input = input(questionaires.prompt)
        if user_input == questionaires.answer:
            score += 1
    print("You got " + str(score) + " out of " + str(len(movie_prompt)) +
          " correct")


movie_questions(answers)

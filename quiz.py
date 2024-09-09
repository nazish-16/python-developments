questions = (
    "What is the capital city of France?",
    "Who wrote the play 'Romeo and Juliet'?",
    "What is the largest planet in our solar system?",
    "Which element has the chemical symbol 'O'?",
    "Who was the first President of the United States?",
    "In which year did the Titanic sink?",
    "What is the longest river in the world?",
    "Who painted the Mona Lisa?",
    "Which continent is the Sahara Desert located on?",
    "What is the hardest natural substance on Earth?"
)

options = (
    ("A. Paris", "B. London", "C. Berlin", "D. Rome"),
    ("A. William Shakespeare", "B. Charles Dickens", "C. Mark Twain", "D. Leo Tolstoy"),
    ("A. Earth", "B. Jupiter", "C. Saturn", "D. Mars"),
    ("A. Oxygen", "B. Gold", "C. Iron", "D. Osmium"),
    ("A. George Washington", "B. Abraham Lincoln", "C. Thomas Jefferson", "D. John Adams"),
    ("A. 1905", "B. 1912", "C. 1918", "D. 1923"),
    ("A. Nile", "B. Amazon", "C. Yangtze", "D. Mississippi"),
    ("A. Leonardo da Vinci", "B. Michelangelo", "C. Pablo Picasso", "D. Vincent van Gogh"),
    ("A. Africa", "B. Asia", "C. South America", "D. Europe"),
    ("A. Diamond", "B. Gold", "C. Iron", "D. Quartz")
)

answers = ("A", "A", "B", "A", "A", "B", "A", "A", "A", "A")
guesses = []
score = 0
question_num = 0

for question in questions:
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print('CORRECT!')
    else:
        print(f"Incorrect. The answer to the question is {answers[question_num]}")
    question_num += 1

print(f"Your score is {score / len(questions) * 100}")
questions = [
    "Is there class this thursday?",
    "Will it be in the 30s next week?",
    "Did I use any breaks in this code?",
    "Are you passing this class?",
    "Is the sky blue?",
]

answers = [False, True, False, True, True]

for i, question in enumerate(questions):
    user_answer = input(f"{question} (True/False): ").strip().lower()
    
    if user_answer == 'true':
        user_response = True
    elif user_answer == 'false':
        user_response = False
    else:
        print("Invalid input, please use 'True' or 'False'.")
        continue
    
    if user_response == answers[i]:
        print("Correct!")
    else:
        print("Incorrect!")

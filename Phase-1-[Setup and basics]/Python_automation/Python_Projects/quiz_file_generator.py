import random


states_and_capitals = {
    "Andhra Pradesh": "Amaravati",
    "Assam": "Dispur",
    "Bihar": "Patna",
    "Gujarat": "Gandhinagar",
    "Karnataka": "Bengaluru",
    "Kerala": "Thiruvananthapuram",
    "Madhya Pradesh": "Bhopal",
    "Maharashtra": "Mumbai",
    "Rajasthan": "Jaipur",
    "Tamil Nadu": "Chennai"
}

states = list(states_and_capitals.keys())

#generating 4 quiz file

for quiz_num in range(1,5):
    quiz_file = open(f"quiz_num_{quiz_num}.txt", mode = "w")
    quiz_ans = open(f"quiz_ans_{quiz_num}.txt",mode = "w")

    random.shuffle(states)

    quiz_states = states[:10]

    for question_num , state in enumerate(quiz_states, start=1):
        correc_capital = states_and_capitals[state]

        wrongopt = list(states_and_capitals.values())
        wrongopt.remove(correc_capital)
        wrong_choices = random.sample(wrongopt,3)


        options  = wrong_choices + [correc_capital]
        random.shuffle(options)

        quiz_file.write("NAME:\nRollno.:\nclass:\n")   
        quiz_file.write(f"{" " * 20}WELCOME TO THE QUIZ\n\n") 
        quiz_file.write(f"{question_num}. what is the capital of {state}? \n")
        quiz_file.write(f"  A.  {options[0]}\n")
        quiz_file.write(f"  B.  {options[1]}\n")
        quiz_file.write(f"  C.  {options[2]}\n")
        quiz_file.write(f"  D.  {options[3]}\n")


        correcopt = options.index(correc_capital)
        corect_letter = "ABCD"[correcopt]

        quiz_ans.write(f"{question_num}.{corect_letter}\n")
    
    quiz_file.close()
    quiz_ans.close()

        




    
    
    
    

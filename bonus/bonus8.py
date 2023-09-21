import json

with open('questions.json', 'r') as file:
    content = file.read()

data = json.loads(content)

for question in data:
    print(question['question_text'])
    for index, alternative in enumerate(question['alternatives'], start=1):
        print(index, '-', alternative)
    
    user_answer = int(input('Enter your answer: '))
    question['user_answer'] = user_answer

score = 0

for index, question in enumerate(data, start=1):
    if question['correct_answer'] == question['user_answer']:
        score = score + 1
        result = 'Your answer is correct. '
    else:
        result = 'Your answer is wrong. '
    
    message = f"Question {index}, your answer is: {question['user_answer']}, {result}The correct answer is: {question['correct_answer']}."
    print(message)

score_message = f"Your total score is: {score} \  {len(data)}"
print(score_message)
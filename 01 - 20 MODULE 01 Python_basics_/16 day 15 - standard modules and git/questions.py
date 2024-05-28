import json

with open(r'E:\Portfolio\UDEMY\CURRENT\Python mega\s16 day 15 - standard modules and git\questions.json', 'r') as file:
    content = file.read()

data = json.loads(content)

print(type(content))
print(type(data))


score = 0

for questions in data:
    print(questions['question_text'])
    for index, alternative in enumerate(questions['alternatives']):
        print(index + 1 , '- ', alternative)
    user_input = int(input('Enter your answer:'))
    if user_input == questions['correct_answer']:
        score = score + 1
        print('Correct')
    else:
        print('Wrong')

print('Your score is:', score , '/', len(data))

from random import * 

from art import logo, vs
from game_data import data

is_playing = True
score = 0

def format_choices(item):
    return f"{item['name']}, a {item['description']}, from {item['country']}."

def check_answer(a, b):
    if a > b:
        return "A"
    elif b > a:
        return "B"

def play(user_c, answer):
    global score
    global is_playing

    if user_c == answer:
        score += 1
        print(f"You're right! Current score: {score}")
    elif user_c != answer:
        is_playing = False
        print(f"Sorry, that's wrong. Final score: {score}")

print(logo)

while is_playing:
    A = choice(data)
    B = choice(data)

    while A["name"] == B["name"]:
        B = choice(data)

    print(f"Compare A: {format_choices(A)}")
    print(vs)
    print(f"Compare B: {format_choices(B)}")

    user_choice = input("Who has more folowers? Type 'A' or 'B': ").upper()

    answer = check_answer(A['follower_count'] , B['follower_count'])
    play(user_choice, answer)
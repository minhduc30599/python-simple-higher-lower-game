from random import * 

from art import logo, vs
from game_data import data

is_playing = True

def check_answer(a, b):
    if a > b:
        return "A"
    elif b > a:
        return "B"

def play(c, answer, is_playing, score):
    if c == answer:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        is_playing = False
        print(f"Sorry, that's wrong. Final score: {score}")

print(logo)
score = 0

while is_playing:
    A = choice(data)
    B = choice(data)
    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}.")
    print(vs)
    print(f"Compare B: {B['name']}, a {B['description']}, from {B['country']}.")
    c = input("Who has more folowers? Type 'A' or 'B': ").upper()

    answer = check_answer(A['follower_count'] , B['follower_count'])

    play(c, answer, is_playing, score)
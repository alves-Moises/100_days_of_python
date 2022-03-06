from replit import clear
from random import choice
from game_data import data


def choice_item(data):
    return choice(data)

def print_line(text_1, text_2):
    print(f"{text_1 :<50}# {text_2 : <}")

def info(artist_1, artist_2):
    print_line(artist_1["name"], artist_2["name"])
    print_line(artist_1["description"], artist_2["description"])
    print_line(artist_1["country"], artist_2["country"])

def quest(items, actual_score):
    # print(items)
    print(f"Actual score: {actual_score}")
    print(f"Who is more famous?")
    print(f"[0] {items[0]['name']}")
    print(f"[1] {items[1]['name']}")
    
    valid = False
    while not valid:
        try:
            choice = int(input())
        except ValueError:
            print("Please selec an intereger number")
        else:
            if choice in [0, 1]:
                valid = True
            else:
                print("Please, a valid answer...")

    values = [items[0]['follower_count'], items[1]['follower_count']]
    values = sorted(values)
    lose = True
    if items[choice]['follower_count'] == values[1]:
        lose = False
    return not lose

def main():
    score = 0
    lose = False

    while not lose:
        clear()
        item_1 = choice_item(data)
        item_2 = choice_item(data)

        while item_1["name"] == item_2["name"]:
            print("Equals items...")
            item_2 = choice_item(data)
        
        info(item_1, item_2)
        
        lose = quest([item_1, item_2], score)
        if not lose:
            score += 1
    print("End of game...")
    print(f"ACTUAL SCORE: {score}")

main()
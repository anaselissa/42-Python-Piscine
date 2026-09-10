import random


def main() -> None:
    print("=== Game Data Alchemist ===\n")

    players = [
        'Alice', 'bob', 'Charlie', 'dylan',
        'Emma', 'Gregory', 'john', 'kevin', 'Liam'
    ]
    print(f"Initial list of players: {players}")

    all_capped = [name.capitalize() for name in players]
    print(f"New list with all names capitalized: {all_capped}")

    initially_capped = [n for n in players if n[0].isupper()]
    print(f"New list of capitalized names only: {initially_capped}")

    scores = {name: random.randint(1, 1000) for name in all_capped}
    print(f"Score dict: {scores}")

    avg = sum(scores.values()) / len(scores)
    print(f"Score average is {round(avg, 2)}")

    high_scores = {k: scores[k] for k in scores if scores[k] > avg}
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()

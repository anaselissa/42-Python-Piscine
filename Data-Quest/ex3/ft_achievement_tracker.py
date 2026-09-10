import random


def gen_player_achievements() -> set[str]:
    achievements_list = [
        "Crafting Genius",
        "World Savior",
        "Master Explorer",
        "Collector Supreme",
        "Untouchable",
        "Boss Slayer",
        "Strategist",
        "Unstoppable",
        "Speed Runner",
        "Survivor",
        "Treasure Hunter",
        "First Steps",
        "Sharp Mind",
        "Hidden Path Finder"
    ]
    size_ret = random.randint(1, 14)
    ret_set = random.sample(achievements_list, size_ret)
    return set(ret_set)


def main() -> None:
    print("=== Achievement Tracker System ===")
    player1 = gen_player_achievements()
    print("player1: ", player1)
    player2 = gen_player_achievements()
    print("player2: ", player2)
    player3 = gen_player_achievements()
    print("player3: ", player3)
    player4 = gen_player_achievements()
    print("player4: ", player4)

    print("All distinct achievements: ", set.union(player1,
                                                   player2, player3, player4))
    print("Common achievements: ", set.intersection(player1,
                                                    player2, player3, player4))

    print("Only player1 has: ", player1.difference(player2, player3, player4))
    print("Only player2 has: ", player2.difference(player1, player3, player4))
    print("Only player3 has: ", player3.difference(player1, player2, player4))
    print("Only player4 has: ", player4.difference(player1, player2, player3))
    all_achievement = {"Crafting Genius", "World Savior", "Master Explorer",
                       "Collector Supreme", "Untouchable", "Boss Slayer",
                       "Strategist", "Unstoppable", "Speed Runner",
                       "Survivor", "Treasure Hunter", "First Steps",
                       "Sharp Mind", "Hidden Path Finder"}

    print("player1 is missing: ", all_achievement.difference(player1))
    print("player2 is missing: ", all_achievement.difference(player2))
    print("player3 is missing: ", all_achievement.difference(player3))
    print("player4 is missing: ", all_achievement.difference(player4))


if __name__ == "__main__":
    main()

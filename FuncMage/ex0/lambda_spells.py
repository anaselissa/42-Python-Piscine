from typing import Any


def artifact_sorter(artifacts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    sorted_list = sorted(
        artifacts,
        key=lambda x: x["power"],
        reverse=True
    )
    return sorted_list


def power_filter(
    mages: list[dict[str, Any]], min_power: int
) -> list[dict[str, Any]]:
    return list(
        filter(
            lambda mage: mage["power"] >= min_power,
            mages
        )
    )


def spell_transformer(spells: list[str]) -> list[str]:
    return list(
        map(
            lambda spell: f"* {spell} *",
            spells
        )
    )


def mage_stats(mages: list[dict[str, Any]]) -> dict[str, int | float]:
    ret_dic = {}
    ret_dic["max_power"] = max(
        mages,
        key=lambda mage: mage["power"]
    )["power"]
    ret_dic["min_power"] = min(
        mages,
        key=lambda mage: mage["power"]
    )["power"]
    ret_dic["avg_power"] = round(
        sum(map(lambda mage: mage["power"], mages)) / len(mages),
        2
    )
    return ret_dic


artifacts = [
    {"name": "Light Prism", "power": 113, "type": "focus"},
    {"name": "Shadow Blade", "power": 60, "type": "armor"},
    {"name": "Fire Staff", "power": 86, "type": "relic"},
    {"name": "Shadow Blade", "power": 109, "type": "armor"},
]

mages = [
    {"name": "Ash", "power": 85, "element": "earth"},
    {"name": "Sage", "power": 52, "element": "water"},
    {"name": "Jordan", "power": 84, "element": "ice"},
    {"name": "River", "power": 75, "element": "shadow"},
    {"name": "River", "power": 53, "element": "light"},
]

spells = [
    "meteor",
    "fireball",
    "tsunami",
    "heal",
]


if __name__ == "__main__":
    print("Testing artifact sorter...")

    art_list = artifact_sorter(artifacts)

    for i in range(len(art_list) - 1):
        print(
            f"{art_list[i]['name']} ({art_list[i]['power']} power)",
            "comes before",
            f"{art_list[i + 1]['name']} ({art_list[i + 1]['power']} power)"
        )

    print("\nTesting spell transformer...")

    x = spell_transformer(spells)

    for i in range(len(x)):
        print(x[i], end="")

    print()

# for i in spell_transformer(spells):
#     print(i)

# print(mage_stats(mages))

# for i in power_filter(mages, 80):
#     print(i["power"])

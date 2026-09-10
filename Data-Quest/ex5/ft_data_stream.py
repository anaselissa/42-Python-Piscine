import random
import typing


def gen_event() -> typing.Generator[typing.Tuple[str, str], None, None]:
    players = ["alice", "bob", "charlie", "dylan"]

    actions = [
        "run", "eat", "sleep", "grab", "move",
        "climb", "swim", "release", "use"
    ]
    while (True):
        player = random.choice(players)
        action = random.choice(actions)
        yield (player, action)


def consume_event(
    lst: list[tuple[str, str]]
) -> typing.Generator[tuple[str, str], None, None]:

    while len(lst) > 0:
        rand_s = random.randint(0, len(lst) - 1)
        event = lst[rand_s]
        del lst[rand_s]
        yield event


def main() -> None:
    print("=== Game Data Stream Processor ===")
    event_stream = gen_event()
    for i in range(1000):
        player, action = next(event_stream)
        print(f"Event {i}: Player {player} did action {action}")
    lst = []
    for i in range(10):
        player, action = next(event_stream)
        lst += [(player, action)]
        print(f"Event {i}: Player {player} did action {action}")
    print("Built list of 10 events: ", lst)
    for it in consume_event(lst):
        print("Got event from list:", it)
        print("Remains in list: ", lst)


if __name__ == "__main__":
    main()

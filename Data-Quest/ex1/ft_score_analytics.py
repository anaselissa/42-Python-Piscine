import sys


def main() -> None:
    print("=== Player Score Analytics ===")
    len_argv = len(sys.argv)
    n_lst = []
    if len_argv != 1:
        for i in sys.argv[1:]:
            try:
                n_lst += [int(i)]
            except ValueError:
                print(f"Invalid parameter: ’{i}’")
        if n_lst:
            print("Scores processed: ", n_lst)
            print("Total players: ", len(n_lst))
            print("Total score: ", sum(n_lst))
            print("Average score: ", sum(n_lst)/len(n_lst))
            print("High score: ", max(n_lst))
            print("Low score: ", min(n_lst))
            print("Score range: ", max(n_lst) - min(n_lst))
        else:
            print("No scores provided. Usage: "
                  "python3 ft_score_analytics.py <score1><score2> ...")
    else:
        print("No scores provided. Usage: "
              "python3 ft_score_analytics.py <score1><score2> ...")


if __name__ == "__main__":
    main()

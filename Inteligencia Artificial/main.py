import random

from structures.AlphaBethaTree import AlphaBethaTree


def main():
    t = AlphaBethaTree(3)
    for i in range(0, 18):
        t.insert(random.randint(-100, 100))
    print(t)

    print(t.pruning())

if __name__ == '__main__':
    main()



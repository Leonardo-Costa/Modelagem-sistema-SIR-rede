from lib import *


def main():
    mtx = GetMatrix(GetGraph(10, 10, 2), 10)
    for i in range(len(mtx)):
        print(mtx[i])


if __name__ == "__main__":
    main()

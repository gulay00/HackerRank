import os


def jumpingOnClouds(c, k):
    n = len(c)
    energy = 100
    position = 0

    while True:
        position = (position + k) % n

        if c[position] == 0:
            energy -= 1
        else:
            energy -= 3

        if position == 0:
            break

    return energy


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])
    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()

import os


def permutationEquation(p):
    n = len(p)
    result = []

    for i in range(1, n + 1):
        result.append(p.index(p.index(i) + 1) + 1)

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

# HackerRank Task: Find the Runner-Up Score!

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    if n >= 2 and n <= 10:
        arr = sorted(arr)
        num = n - arr.count(arr[-1])

    print(arr[num - 1])

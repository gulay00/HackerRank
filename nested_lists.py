# HackerRank Task: Nested Lists

if __name__ == '__main__':
    n = int(input())
    students = {}

    for x in range(n):
        name = input()
        score = float(input())
        students[name] = score

    scores = sorted(set(students.values()))
    sec_low = scores[1]

    result = [name for name, scor in students.items() if scor == sec_low]
    result.sort()

    for name in result:
        print(name)

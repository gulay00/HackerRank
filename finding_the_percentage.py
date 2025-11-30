# HackerRank Task: Finding the Percentage

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores

    query_name = input()
    out = 0

    if n >= 2 and n <= 10:
        for x in student_marks.keys():
            if x == query_name:
                out = sum(student_marks[x]) / len(student_marks[x])
                print(f"{out:.2f}")

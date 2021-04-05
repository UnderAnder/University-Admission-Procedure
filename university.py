departments = {'Biotech': [], 'Chemistry': [], 'Engineering': [], 'Mathematics': [], 'Physics': []}
# related exams fields indexes in input file
exam = {'Biotech': (2, 3), 'Chemistry': (3, 3), 'Engineering': (4, 5), 'Mathematics': (4, 4), 'Physics': (2, 4)}

max_accepted = int(input())
with open('applicants.txt') as f:
    applicants = [line.split() for line in f]

for i in range(7, 10):  # priority fields in input file
    for dep in departments.keys():
        sort_key = lambda x: (-max(int(x[exam[dep][0]]) + int(x[exam[dep][1]]), int(x[6]) * 2), x[0], x[1])
        for applicant in sorted(applicants, key=sort_key):
            if applicant[i] == dep and len(departments[dep]) < max_accepted:
                score = max(((int(applicant[exam[dep][0]]) + int(applicant[exam[dep][1]])) / 2), float(applicant[6]))
                departments[dep].append([applicant[0], applicant[1], score])
                applicants.remove(applicant)

for dep in departments.keys():
    with open(f'{dep.lower()}.txt', 'w', encoding='utf-8') as f:
        for student in sorted(departments[dep], key=lambda x: (-x[2], x[0], x[1])):
            print(*student, file=f)

applicants = []
departments = {'Biotech': [], 'Chemistry': [], 'Engineering': [], 'Mathematics': [], 'Physics': []}
exam = {'Biotech': 3, 'Chemistry': 3, 'Engineering': 5, 'Mathematics': 4, 'Physics': 2}  # field indexes in input file

max_accepted = int(input())
with open('applicants.txt') as f:
    for line in f:
        applicants.append(line.split())

for i in range(6, 9):  # priority fields in input file
    for dep in departments.keys():
        applicants_sorted = sorted(applicants, key=lambda x: (x[i], -float(x[exam[dep]]), x[0], x[1]))
        for applicant in applicants_sorted:
            if len(departments[dep]) < max_accepted and applicant[i] == dep:
                departments[dep].append((applicant[0], applicant[1], applicant[exam[dep]]))
                applicants.remove(applicant)

for department in departments.keys():
    print(department)
    for student in sorted(departments[department], key=lambda x: (-float(x[2]), x[0], x[1])):
        print(*student[:3])
    print()

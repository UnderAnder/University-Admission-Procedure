from copy import copy

applicants = []
departments = {'Mathematics': [], 'Physics': [], 'Biotech': [], 'Chemistry': [], 'Engineering': []}
max_accepted = int(input())
with open('applicants.txt') as f:
    for line in f:
        applicants.append(line.split())

applicants_sorted = sorted(applicants, key = lambda x: (-float(x[2]), x[0], x[1]))

for i in range (3, 6):  # priority fields in file
    for applicant in copy(applicants_sorted):
        if len(departments[applicant[i]]) < max_accepted:
            departments[applicant[i]].append(applicant)
            applicants_sorted.remove(applicant)


for department in sorted(departments.keys()):
    print(department)
    for student in sorted(departments[department], key = lambda x: (-float(x[2]), x[0], x[1])):
        print(*student[:3])
    print()

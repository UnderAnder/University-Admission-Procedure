applicants = []
total, max_accepted = int(input()), int(input())
for i in range(total):
    line = input()
    applicants.append(line.split())

applicants_sorted = sorted(applicants, key = lambda x: (-float(x[2]), x[0], x[1]))

print('Successful applicants:')
for i in applicants_sorted[:max_accepted]:
    print(i[0], i[1])

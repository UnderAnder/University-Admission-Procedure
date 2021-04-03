first, second, third = int(input()), int(input()), int(input())
avg = (first + second + third)/3
accept_message = 'Congratulations, you are accepted!'
reject_mesage = 'We regret to inform you that we will not be able to offer you admission.'
print(avg)
print(reject_mesage if avg < 60.0 else accept_message)

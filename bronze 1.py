# watched walkthrough -- https://www.youtube.com/watch?v=dP3JEK5B2Uo
# goal is to check if the cows would change their feeding type based on peer pressure i guess lol

N = input().split()

possibilities = [0]*N

for i in range(len(N)):
    if N[i] == N[i+1]:
        possibilities[i] = 1
    if i<N-2 and N[i] == N[i+2]:
        possibilities[i] = 1

valid = []
for i in range(N):
    if possibilities[i] == 1:
        valid.append(i+1)

#possible optimization: save index in first loop instead of doing twice
#but might be using append so similar timing anyways
#or maybe just print(end="") or smthn

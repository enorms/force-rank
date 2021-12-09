# force rank choices
to_rank = input('Enter comma separated list\n').split(',')
answers=[]
for i in range(0, len(to_rank)): 
  for j in range(0, len(to_rank)): # index 0 is self
    if i == j:
      continue
    a = to_rank[i]
    b = to_rank[j]
    answer = input(' '.join([a, 'or', b, '?', '\n']))
    answers.append([a, b, answer])
print(answers)
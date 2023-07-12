""" task->Nested Lists:Print the name(s) of any student(s) having the second lowest grade in. 
If there are multiple students, order their names alphabetically and print each one on a new line."""
# Z is nested list
# u is all scores list
# p is list of names of all students having the second lowest grade
z=[]
u=[]
p=[]
# N is number of students
N=input()
for i in range(int(N)):
        name = input()
        score = float(input())
        z.append([])
        z[i].append(name)
        z[i].append(score)
        u.append(score)
# sort u assending
u.sort()
lowest = u[0]
second_lowest =u[1]
for f in range(1,len(u)-1):
    if lowest==second_lowest:
        second_lowest=u[1+f] #value of the second lowest grade

for t in range(int(N)):
    if z[t][1]==second_lowest:
       p.append(z[t][0])
# sort p assending
p.sort()
for k in range(len(p)):
    print(p[k])
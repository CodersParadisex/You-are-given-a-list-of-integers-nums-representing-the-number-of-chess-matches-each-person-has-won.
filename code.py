'''You are given a list of integers nums, representing the number of chess matches each person has won.
Return a relative ranking (0-indexed) of each person. If two players have won the same amount, their ranking should be the same.'''

#replace values of nums with your own to test it
nums = [50, 30, 50, 90, 10]


n=list(set(nums))
n.sort(reverse=True)
d={}
for i in range(len(n)):
        d[n[i]]=d.get(n[i],0)+i
print([d[i] for i in nums])

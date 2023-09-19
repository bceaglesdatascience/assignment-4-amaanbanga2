num = int(input("Number of purchases: "))
tax = float(input("Sales tax: "))
i=0
names=[]
costs=[]
while i<num:
    name=input("Customer: ")
    names.append(name)
    cost=float(input("Cost: "))
    costs.append(cost)
    i+=1
def add_tax(cost_list, salestax):
    new_costs=[]
    for cost in cost_list:
        new_cost=cost*(salestax+1)
        new_costs.append(new_cost)
    return new_costs
new_costs= add_tax(costs, tax)
ans={}
for i in range(len(new_costs)):
    if names[i] in ans:
        ans[names[i]]+=new_costs[i]
    else:
        ans[names[i]]=new_costs[i]
print(ans)
    

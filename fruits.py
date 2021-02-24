# Python Program to Calculate Electricity Bill
fruits =['apple','banana','grapes','strwberry']
fruits= int(input(" Please enter Number of fruits you need : "))

if (fruits< 5):
    amount = fruits*200
elif (fruits<= 10):
    amount = fruits*170
elif (units <= 50):
    amount = fruits*150
else:
    amount = fruits*140

total = amount
print("\n fruit bill= %.2f" % total)

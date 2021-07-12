income = float(input("请输入年收入"))
deposit = float(input("请输入年存款项"))
earningrate = float(input("请输入年化投资收益"))
down_payment = float(input("请输入房首付金额"))
years = 1
total = income
deposit_sum = deposit
while total < down_payment:
    years = years + 1
    total = total - deposit_sum
    deposit_sum = deposit_sum * (earningrate + 1) + deposit
    total = total + income - deposit + deposit_sum
print("需要 %f 年可以付首付" %(years))

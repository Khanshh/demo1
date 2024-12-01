
def calc_total_money(rice_weigh, KILOGAM_RICE):
	return rice_weigh * KILOGAM_RICE

def calc_money(total_money, money_given):
	if money_given < total_money:
		return -1
	else:
		return money_given - total_money

def 

def main():
	KILOGAM_RICE = 28
	rice_weigh = input("Enter kg rice: ")
	rice_weigh = float(rice_weigh)
	money_given = input("How money given: ")
	money_given = float(money_given)

	total_money = calc_total_money(rice_weigh, KILOGAM_RICE)
	money_return = calc_money(total_money, money_given)
	if money_return == -1:
		print("Not enough cash")
	else:
		print("You need to return to customer: " + str(money_return))

main()	

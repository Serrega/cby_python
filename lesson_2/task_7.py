car_price = 11000
piter_bank_bill = 0.25
piter_spending = 0.15
car_spending_in_percent = 0.25

total_cash = car_price / car_spending_in_percent
piter_balance = int(total_cash*(1 - piter_spending - piter_bank_bill
                            - car_spending_in_percent))
print("Piter balance is:", piter_balance, "$")



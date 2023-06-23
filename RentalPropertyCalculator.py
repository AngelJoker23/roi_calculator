class RentalPropertyCalculator:
    def __init__(self):
        self.income = 0
        self.expenses = 0
        self.cashflow = 0
        self.cash_on_cash_return = 0

    def calculate_income(self, rental_income, laundry_income, storage_income, misc_income):
        self.income = rental_income + laundry_income + storage_income + misc_income

    def calculate_expenses(self, taxes, insurance, water_sewer, garbage, electric_gas, hoa_fee, lawn_snow,
                           vacancy, repairs, capex, prop_mgmt, mortgage):
        self.expenses = taxes + insurance + water_sewer + garbage + electric_gas + hoa_fee + lawn_snow + vacancy + \
                        repairs + capex + prop_mgmt + mortgage

    def calculate_cashflow(self):
        self.cashflow = self.income - self.expenses

    def calculate_cash_on_cash_return(self, downpayment, closing_costs, rehab_budget, misc_other):
        total_investment = downpayment + closing_costs + rehab_budget + misc_other
        self.cash_on_cash_return = (self.cashflow * 12) / total_investment * 100


# Example usage
calculator = RentalPropertyCalculator()

# Calculate income
calculator.calculate_income(1500, 100, 50, 25)

# Calculate expenses
calculator.calculate_expenses(200, 100, 50, 30, 80, 50, 20, 100, 200, 100, 150, 1000)

# Calculate cashflow
calculator.calculate_cashflow()

# Calculate cash-on-cash return
calculator.calculate_cash_on_cash_return(50000, 5000, 10000, 2000)

# Print the results
print("Income:", calculator.income)
print("Expenses:", calculator.expenses)
print("Cashflow:", calculator.cashflow)
print("Cash-on-Cash Return:", calculator.cash_on_cash_return)

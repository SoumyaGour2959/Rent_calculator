

#inputs
def calculate_rent(Total_rent, people, electricity_unit, charge_per_unit, food):
    Total_rent = float(Total_rent)
    people = int(people)
    electricity_unit = float(electricity_unit)
    charge_per_unit = float(charge_per_unit)
    food = float(food)

    Total_bill = electricity_unit* charge_per_unit

    Total_amount = (Total_rent + Total_bill + food)
    per_person = (Total_amount/people)
    return f"Total_Amount: Rs.{Total_amount:.2f}\n Amount per person: Rs. {per_person:.2f}"
    print("Amount per person is: ", per_person)

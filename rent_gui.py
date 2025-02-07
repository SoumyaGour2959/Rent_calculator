import tkinter 
from rent import calculate_rent

def on_calculate():
    result_text = calculate_rent(
        rent_entry.get(),
        people_entry.get(),
        electricity_unit_entry.get(),
        charge_per_unit_entry.get(),
        Food_entry.get()
    )
    result_label.config(text = result_text)


window = tkinter.Tk()
window.title("Rent Calculator")
window.geometry("400x300")


"""Labels"""
rent_label = tkinter.Label(window, text="Total rent")
rent_entry = tkinter.Entry(window)

people_label = tkinter.Label(window, text="No. of people sharing room")
people_entry = tkinter.Entry(window)

electricity_unit_label= tkinter.Label(window, text="Electricity unit spend")
electricity_unit_entry= tkinter.Entry(window)

charge_per_unit_label = tkinter.Label(window, text="Charge per unit")
charge_per_unit_entry= tkinter.Entry(window)

Food_label = tkinter.Label(window, text="Total amount spend on food")
Food_entry = tkinter.Entry(window)

Calculate_button= tkinter.Button(window, text="Calculate", command= on_calculate)

'''Geometry'''
rent_label.grid(row = 1, column= 0)
rent_entry.grid(row= 1, column=1 )

people_label.grid(row = 2, column= 0)
people_entry.grid(row= 2, column=1 )

electricity_unit_label.grid(row = 3, column= 0)
electricity_unit_entry.grid(row= 3, column=1 )

charge_per_unit_label.grid(row = 4, column= 0)
charge_per_unit_entry.grid(row= 4, column=1 )

Food_label.grid(row = 5, column= 0)
Food_entry.grid(row= 5, column=1 )

Calculate_button.grid(row = 6, column= 0, columnspan=3)

result_label = tkinter.Label(window, text = "")
result_label.grid(row= 8, column= 1, columnspan=2)


window.mainloop()
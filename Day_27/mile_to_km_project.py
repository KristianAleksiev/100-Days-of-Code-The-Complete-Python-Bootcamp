from tkinter import *


def conversion():
    miles = float(miles_input.get())
    in_km = miles*1.609
    result_km_label.config(text=f"{in_km:.1f}")


window = Tk()
window.title("Miles to kilometers converter")
window.config(padx=20, pady=20)

miles_input = Entry(width=8)
miles_input.grid(column=1, row= 0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row= 0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

result_km_label = Label(text="0")
result_km_label.grid(column=1, row=1)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=conversion)
calculate_button.grid(column=1, row=2)

window.mainloop()

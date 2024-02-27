import tkinter as tk

def calculate_current():
   try:
       power = float(power_entry.get())
       voltage = float(voltage_entry.get())
       current = power / voltage
       current_label.config(text="Current amperes: {:.2f} A".format(current))
   except ValueError:
       current_label.config(text="Please enter valid numbers")

def calculate_charging_time():
   try:
       capacity = float(capacity_entry.get())
       current = float(current_entry.get())
       time = capacity / current
       time_label.config(text="full of time: {:.2f} Hour".format(time))
   except ValueError:
       time_label.config(text="Please enter valid numbers")

def calculate_range_hours():
   try:
       current = float(range_current_entry.get())
       power = float(range_power_entry.get())
       voltage = float(range_voltage_entry.get())
       range_hours = current / (power / voltage)
       range_label.config(text="Battery life hours: {:.2f} Hour".format(range_hours))
   except ValueError:
       range_label.config(text="Please enter valid numbers")

root = tk.Tk()
root.title("Solar power calculator")

power_label = tk.Label(root, text="Solar Power (Watts): ")
power_label.grid(row=0, column=0, padx=5, pady=5)
power_entry = tk.Entry(root)
power_entry.grid(row=0, column=1, padx=5, pady=5)

voltage_label = tk.Label(root, text="Battery voltage (volts): ")
voltage_label.grid(row=1, column=0, padx=5, pady=5)
voltage_entry = tk.Entry(root)
voltage_entry.grid(row=1, column=1, padx=5, pady=5)

calculate_current_button = tk.Button(root, text="Calculate Current", command=calculate_current)
calculate_current_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

current_label = tk.Label(root, text="")
current_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

capacity_label = tk.Label(root, text="Battery capacity (Ah): ")
capacity_label.grid(row=4, column=0, padx=5, pady=5)
capacity_entry = tk.Entry(root)
capacity_entry.grid(row=4, column=1, padx=5, pady=5)

current_label2 = tk.Label(root, text="Current (amps): ")
current_label2.grid(row=5, column=0, padx=5, pady=5)
current_entry = tk.Entry(root)
current_entry.grid(row=5, column=1, padx=5, pady=5)

calculate_time_button = tk.Button(root, text="Calculate filling time", command=calculate_charging_time)
calculate_time_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

time_label = tk.Label(root, text="")
time_label.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

range_current_label = tk.Label(root, text="Battery (Amp): ")
range_current_label.grid(row=8, column=0, padx=5, pady=5)
range_current_entry = tk.Entry(root)
range_current_entry.grid(row=8, column=1, padx=5, pady=5)

range_power_label = tk.Label(root, text="Load power (watts): ")
range_power_label.grid(row=9, column=0, padx=5, pady=5)
range_power_entry = tk.Entry(root)
range_power_entry.grid(row=9, column=1, padx=5, pady=5)

range_voltage_label = tk.Label(root, text="Battery voltage (volts): ")
range_voltage_label.grid(row=10, column=0, padx=5, pady=5)
range_voltage_entry = tk.Entry(root)
range_voltage_entry.grid(row=10, column=1, padx=5, pady=5)

calculate_range_button = tk.Button(root, text="Calculate usage hours", command=calculate_range_hours)
calculate_range_button.grid(row=11, column=0, columnspan=2, padx=5, pady=5)

range_label = tk.Label(root, text="")
range_label.grid(row=12, column=0, columnspan=2, padx=5, pady=5)

root.update_idletasks()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = root.winfo_width()
window_height = root.winfo_height()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry('+{}+{}'.format(x, y))

root.mainloop()

#currency converter
#creating dictionary

import tkinter as tk

conversion_rates = {
    'USD': {'EUR': 0.85, 'GBP': 0.73, 'JPY': 110.52, 'INR': 74.83,"BRL":5.20},
    'EUR': {'USD': 1.18, 'GBP': 0.86, 'JPY': 130.87, 'INR': 88.70,"BRL":5.55},
    'GBP': {'USD': 1.37, 'EUR': 1.16, 'JPY': 151.34, 'INR': 102.57,"BRL":6.44},
    'JPY': {'USD': 0.0091, 'EUR': 0.0076, 'GBP': 0.0066, 'INR': 0.68,"BRL":0.034},
    'INR': {'USD': 0.013, 'EUR': 0.011, 'GBP': 0.0097, 'JPY': 1.46,"BRL":0.062},
    'BRL':{'USD': 0.19, 'EUR': 0.18, 'GBP': 0.16, 'JPY': 29.72,"INR":16.02}
}

def currency_converter(amount, from_currency, to_currency):
    #checking for same currency
    if from_currency == to_currency:
        return amount
    #checking for valid conversion
    if from_currency in conversion_rates and to_currency in conversion_rates[from_currency]:
        rate = conversion_rates[from_currency][to_currency]
        converted_amount = amount * rate
        return converted_amount
    else:
        
        return "Currency not supported or invalid conversion."


def convert_currency():
    amount = float(entry.get())
    base_currency = base_currency_var.get()
    target_currency = target_currency_var.get()

    converted_amount = currency_converter(amount, target_currency, base_currency)
    result_label.config(text=str(converted_amount))

window = tk.Tk()
window.title("Currency Converter")

label1 = tk.Label(window, text="Amount:")
label1.pack()

entry = tk.Entry(window)
entry.pack()

label2 = tk.Label(window, text="From currency:")
label2.pack()

base_currency_var = tk.StringVar(window)
base_currency_var.set("INR")  # Default base currency

base_currency_dropdown = tk.OptionMenu(window, base_currency_var, "USD", "EUR", "GBP", "INR","JYP","BRL")
base_currency_dropdown.pack()

label3 = tk.Label(window, text="To Currency:")
label3.pack()

target_currency_var = tk.StringVar(window)
target_currency_var.set("USD")  # Default target currency

target_currency_dropdown = tk.OptionMenu(window, target_currency_var, "USD", "EUR", "GBP", "INR","JYP","BRL")
target_currency_dropdown.pack()

label4 = tk.Label(window, text="Converted Amount:")
label4.pack()

result_label = tk.Label(window, text="")
result_label.pack()

button = tk.Button(window, text="Convert", command=convert_currency)
button.pack()

window.mainloop()

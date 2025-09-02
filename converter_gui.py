import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
import requests as rq
from converter_core import get_exchange_rates

# Function to load exchange rate
def load_exchange_rate(initial_currency):
    try:
        exchange_rate = get_exchange_rates(initial_currency)
        if not exchange_rate:
            mb.showerror("API Error", f"The API did not return any data.")
            return None
        return exchange_rate
    except rq.exceptions.RequestException as e:
        mb.showerror("Network Error",
                     f"A network error occurred! Please check your internet connection.\n\nError details: {e}")
        return None
    except Exception as e:
        mb.showerror("Error", f"Something unexpected went wrong.\n\nError details: {e}")
        return None

# Function to convert currency and present result in GUI
def converter():
    initial_currency = from_combo.get()
    try:
        initial_currency_value = float(amount_entry.get())
    except ValueError as e:
        mb.showerror("Value Error", f"Please enter a number!\n\nError details: {e}")
        return
    final_currency = to_combo.get()
    multiplier = load_exchange_rate(initial_currency)[final_currency]
    final_currency_value = initial_currency_value * multiplier
    results = f"{initial_currency_value:.2f} {initial_currency} = {final_currency_value:.2f} {final_currency}"
    result_label.config(text = results)

# Initialise window
root = tk.Tk()
root.title("Currency Converter")
root.geometry("420x350")

# Create frames
title_frame = tk.Frame(root)
title_frame.pack(pady = 10)
input_frame = tk.Frame(root)
input_frame.pack(pady = 10, fill = "x")
results_frame = tk.Frame(root)
results_frame.pack(pady = 10)

# Create styles for labels and buttons
style = ttk.Style()
style.configure("Title.TLabel", font = ("Arial", 24, "bold"))
style.configure("GeneralLabel.TLabel", font = ("Arial", 18))
style.configure("FormButton.TButton", font = ("Arial", 18))
style.configure("ResultLabel.TLabel", font = ("Arial", 14))

# Create widgets for title_frame
title_label = ttk.Label(title_frame, text = "Currency Converter", style = "Title.TLabel")
title_label.pack()

# Create variables for dropdowns
from_var = tk.StringVar()
from_var.set("USD")
to_var = tk.StringVar()
to_var.set("EUR")
currencies = ['USD', 'AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN', 'BAM', 'BBD', 'BDT', 'BGN', 'BHD', 'BIF', 'BMD', 'BND', 'BOB', 'BRL', 'BSD', 'BTN', 'BWP', 'BYN', 'BZD', 'CAD', 'CDF', 'CHF', 'CLP', 'CNY', 'COP', 'CRC', 'CUP', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 'EGP', 'ERN', 'ETB', 'EUR', 'FJD', 'FKP', 'FOK', 'GBP', 'GEL', 'GGP', 'GHS', 'GIP', 'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK', 'HTG', 'HUF', 'IDR', 'ILS', 'IMP', 'INR', 'IQD', 'IRR', 'ISK', 'JEP', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KID', 'KMF', 'KRW', 'KWD', 'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LYD', 'MAD', 'MDL', 'MGA', 'MKD', 'MMK', 'MNT', 'MOP', 'MRU', 'MUR', 'MVR', 'MWK', 'MXN', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RUB', 'RWF', 'SAR', 'SBD', 'SCR', 'SDG', 'SEK', 'SGD', 'SHP', 'SLE', 'SLL', 'SOS', 'SRD', 'SSP', 'STN', 'SYP', 'SZL', 'THB', 'TJS', 'TMT', 'TND', 'TOP', 'TRY', 'TTD', 'TVD', 'TWD', 'TZS', 'UAH', 'UGX', 'UYU', 'UZS', 'VES', 'VND', 'VUV', 'WST', 'XAF', 'XCD', 'XCG', 'XDR', 'XOF', 'XPF', 'YER', 'ZAR', 'ZMW', 'ZWL']

# Create widgets for input_frame
input_frame.columnconfigure(1, weight = 1)
amount_label = ttk.Label(input_frame, text = "Amount: ", style = "GeneralLabel.TLabel")
amount_label.grid(row = 0, column = 0, sticky = "w", padx = 5, pady = 10)
amount_entry = ttk.Entry(input_frame, font = ("Arial", 12))
amount_entry.grid(row = 0, column = 1, sticky = "ew", padx = 5, pady = 10)
from_label = ttk.Label(input_frame, text = "From:", style = "GeneralLabel.TLabel")
from_label.grid(row = 1, column = 0, sticky = "w", padx = 5, pady = 10)
from_combo = ttk.Combobox(input_frame, textvariable = from_var, font = ("Arial", 12), values = currencies, state = "readonly", height = 5)
from_combo.grid(row = 1, column = 1, sticky = "ew", padx = 5, pady = 10)
to_label = ttk.Label(input_frame, text = "To:", style = "GeneralLabel.TLabel")
to_label.grid(row = 2, column = 0, sticky = "w", padx = 5, pady = 10)
to_combo = ttk.Combobox(input_frame, textvariable = to_var, font = ("Arial", 12), values = currencies, state = "readonly", height = 5)
to_combo.grid(row = 2, column = 1, sticky = "ew", padx = 5, pady = 10)
convert_button = ttk.Button(input_frame, text = "Convert", style = "FormButton.TButton", command = converter)
convert_button.grid(row = 3, column = 0, columnspan= 2, sticky = "", pady = 10)

# Create widgets for results_frame
result_label = ttk.Label(results_frame, text = "", style = "ResultLabel.TLabel")
result_label.pack()

root.mainloop()
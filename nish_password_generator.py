import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from secrets import choice, SystemRandom
import string
import pyttsx3

def generate_password(length=12):
    # Character sets
    digits = string.digits
    lowercase_characters = string.ascii_lowercase
    uppercase_characters = string.ascii_uppercase
    symbols = '@#$%=:?./|~>*()<'  # Adjust symbols as needed

    # Combine character sets
    combined_list = digits + lowercase_characters + uppercase_characters + symbols

    # Ensure minimum requirements are met
    if length < 4:
        raise ValueError("Password length must be at least 4")

    # Randomly select one character from each character set
    rand_digit = choice(digits)
    rand_lower = choice(lowercase_characters)
    rand_upper = choice(uppercase_characters)
    rand_symbol = choice(symbols)

    # Combine the selected characters
    temp_pass = rand_digit + rand_lower + rand_upper + rand_symbol

    # Fill the rest of the password length by selecting randomly from the combined list
    for _ in range(length - 4):
        temp_pass += choice(combined_list)

    # Convert temporary password into a list and shuffle it
    temp_pass_list = list(temp_pass)
    SystemRandom().shuffle(temp_pass_list)

    # Convert the shuffled list back to a string
    password = ''.join(temp_pass_list)

    return password

def generate_and_show_password():
    try:
        length = int(length_var.get())
        password = generate_password(length)
        password_var.set(password)

        # Speak the generated password
        speak_text("Your awesome password has been generated!")

    except ValueError as e:
        messagebox.showerror("Error", str(e))
        speak_text("Error: " + str(e))

def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# GUI setup
root = tk.Tk()
root.title("🔐 Awesome Password Generator 🔐")

# Set colorful background
background_color = "#b3d9ff"  # Light blue color, you can change it
root.configure(background=background_color)

# Create a themed style
style = ttk.Style()

# Use the "clam" theme for a glowing effect (you can experiment with other available themes)
style.theme_use("clam")

# Length entry
length_label = ttk.Label(root, text="Password Length:")
length_var = tk.StringVar(value="12")  # Default length
length_entry = ttk.Entry(root, textvariable=length_var)

# Generate button
generate_button = ttk.Button(root, text="Generate Password", command=generate_and_show_password)

# Generated password display
password_var = tk.StringVar()
password_label = ttk.Label(root, text="Generated Password:")
password_display = ttk.Entry(root, textvariable=password_var, state="readonly", font=("Courier", 12))

# Layout
length_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
length_entry.grid(row=0, column=1, padx=10, pady=10)
generate_button.grid(row=1, column=0, columnspan=2, pady=10)
password_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")
password_display.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

# Adjust column weights to make the password display expandable
root.columnconfigure(1, weight=1)

# Run the GUI
root.mainloop()

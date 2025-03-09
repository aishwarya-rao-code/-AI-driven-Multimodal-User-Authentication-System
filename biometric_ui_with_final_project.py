import tkinter as tk
from tkinter import scrolledtext
import subprocess
import threading

# Function to run the biometric authentication script and display output in UI
def run_biometric_system():
    output_text.delete(1.0, tk.END)  # Clear previous output
    
    def execute():
        try:
            process = subprocess.Popen(
                ["python", r"C:\Users\aishu\OneDrive - University of South Florida\Documents\Trustworthy\Final_Project.py"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1
            )

            # Read line by line to update UI dynamically
            for line in process.stdout:
                output_text.insert(tk.END, line)
                output_text.see(tk.END)  # Auto-scroll
                root.update_idletasks()  # Update UI instantly

            # Capture errors if any
            for line in process.stderr:
                output_text.insert(tk.END, "[ERROR] " + line)
                output_text.see(tk.END)
                root.update_idletasks()

        except Exception as e:
            output_text.insert(tk.END, f"\n[ERROR] {e}\n")
            output_text.see(tk.END)

    # Run in separate thread to avoid UI freezing
    threading.Thread(target=execute, daemon=True).start()

# Create UI window
root = tk.Tk()
root.title("Biometric Authentication - Output Display")

auth_button = tk.Button(root, text="Run Biometric System", command=run_biometric_system, font=("Arial", 14))
auth_button.pack(pady=20)

output_text = scrolledtext.ScrolledText(root, width=80, height=20, font=("Arial", 12))
output_text.pack(pady=20)

root.mainloop()

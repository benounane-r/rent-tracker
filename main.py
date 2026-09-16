import tkinter as tk
from login_screen import LoginScreen

def main():
    root = tk.Tk()
    root.title("Rent Tracker")
    root.geometry("480x700")
    root.resizable(False, False)
    
    app = LoginScreen(root)
    
    root.mainloop()

if __name__ == "__main__":
    main()
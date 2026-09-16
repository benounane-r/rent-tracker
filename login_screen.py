import tkinter as tk
from tkinter import messagebox
from auth import login

class LoginScreen:
    def __init__(self, root):
        self.root = root
        self.root.configure(bg="#1a1a2e")
        self.build_ui()

    def build_ui(self):
        # Title
        tk.Label(
            self.root,
            text="Rent Tracker",
            font=("Arial", 24, "bold"),
            bg="#1a1a2e",
            fg="#4fc3f7"
        ).pack(pady=(60, 4))

        tk.Label(
            self.root,
            text="Property management made simple",
            font=("Arial", 11),
            bg="#1a1a2e",
            fg="#888888"
        ).pack(pady=(0, 40))

        # User type selection
        tk.Label(
            self.root,
            text="I am a...",
            font=("Arial", 11),
            bg="#1a1a2e",
            fg="#cccccc"
        ).pack()

        self.user_type = tk.StringVar(value="landlord")

        btn_frame = tk.Frame(self.root, bg="#1a1a2e")
        btn_frame.pack(pady=8)

        tk.Radiobutton(
            btn_frame, text="Landlord",
            variable=self.user_type, value="landlord",
            bg="#1a1a2e", fg="#ffffff",
            selectcolor="#4fc3f7",
            font=("Arial", 11)
        ).pack(side="left", padx=16)

        tk.Radiobutton(
            btn_frame, text="Tenant",
            variable=self.user_type, value="tenant",
            bg="#1a1a2e", fg="#ffffff",
            selectcolor="#4fc3f7",
            font=("Arial", 11)
        ).pack(side="left", padx=16)

        # Email
        tk.Label(
            self.root, text="Email",
            font=("Arial", 11), bg="#1a1a2e", fg="#cccccc"
        ).pack(anchor="w", padx=80, pady=(16, 2))

        self.email_entry = tk.Entry(
            self.root, font=("Arial", 12),
            width=30, bg="#16213e", fg="#ffffff",
            insertbackground="white",
            relief="flat", bd=8
        )
        self.email_entry.pack(padx=80)

        # Password
        tk.Label(
            self.root, text="Password",
            font=("Arial", 11), bg="#1a1a2e", fg="#cccccc"
        ).pack(anchor="w", padx=80, pady=(12, 2))

        self.password_entry = tk.Entry(
            self.root, font=("Arial", 12),
            width=30, bg="#16213e", fg="#ffffff",
            insertbackground="white",
            relief="flat", bd=8, show="*"
        )
        self.password_entry.pack(padx=80)

        # Login button
        tk.Button(
            self.root,
            text="Login",
            font=("Arial", 13, "bold"),
            bg="#4fc3f7", fg="#000000",
            relief="flat", bd=0,
            padx=20, pady=10,
            cursor="hand2",
            command=self.handle_login
        ).pack(pady=32)

        # Register link
        tk.Label(
            self.root,
            text="New landlord? Register here",
            font=("Arial", 10, "underline"),
            bg="#1a1a2e", fg="#4fc3f7",
            cursor="hand2"
        ).pack()

    def handle_login(self):
        email = self.email_entry.get().strip()
        password = self.password_entry.get().strip()
        user_type = self.user_type.get()

        if not email or not password:
            messagebox.showerror("Error", "Please fill in all fields")
            return

        user = login(email, password, user_type)

        if user:
            messagebox.showinfo("Success", f"Welcome {user[1]}!")
        else:
            messagebox.showerror("Error", "Invalid email or password")
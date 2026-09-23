import tkinter as tk
from tkinter import ttk, messagebox
import datetime

class AnimatedPersonalDataApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Interactive Personal Data Collector - Animated Edition")
        self.root.geometry("680x780")
        self.root.configure(bg="#0f172a")  # Dark Slate Background
        self.root.resizable(False, False)

        # ----------------------------------------------------------------------
        # COLOR PALETTE
        # ----------------------------------------------------------------------
        self.BG_DARK = "#0f172a"
        self.PANEL_BG = "#1e293b"
        self.CARD_BG = "#334155"
        self.ACCENT_CYAN = "#38bdf8"
        self.ACCENT_GREEN = "#10b981"
        self.HOVER_GREEN = "#059669"
        self.ACCENT_RED = "#ef4444"
        self.HOVER_RED = "#dc2626"
        self.TEXT_LIGHT = "#f8fafc"
        self.TEXT_MUTED = "#94a3b8"

        # Configure TTK Styles
        self.style = ttk.Style()
        self.style.theme_use("clam")

        # Custom Progressbar Style
        self.style.configure(
            "Custom.Horizontal.TProgressbar", 
            troughcolor=self.PANEL_BG, 
            background=self.ACCENT_CYAN, 
            thickness=6
        )

        # ----------------------------------------------------------------------
        # 1. HEADER BANNER WITH GLOW ANIMATION
        # ----------------------------------------------------------------------
        self.header_frame = tk.Frame(root, bg=self.PANEL_BG, pady=18, highlightthickness=1, highlightbackground="#334155")
        self.header_frame.pack(fill="x")

        self.title_label = tk.Label(
            self.header_frame, 
            text="✨ INTERACTIVE PERSONAL DATA COLLECTOR ✨", 
            font=("Segoe UI", 16, "bold"), 
            fg=self.ACCENT_CYAN, 
            bg=self.PANEL_BG
        )
        self.title_label.pack()

        self.subtitle_label = tk.Label(
            self.header_frame, 
            text="Python Fundamentals: Data Types • Type Casting • Memory (id) Tracking • Calculations", 
            font=("Segoe UI", 9), 
            fg=self.TEXT_MUTED, 
            bg=self.PANEL_BG
        )
        self.subtitle_label.pack(pady=(4, 0))

        # ----------------------------------------------------------------------
        # 2. MAIN CONTAINER
        # ----------------------------------------------------------------------
        main_frame = tk.Frame(root, bg=self.BG_DARK, padx=24, pady=16)
        main_frame.pack(fill="both", expand=True)

        # ----------------------------------------------------------------------
        # 3. INPUT FORM SECTION (CARD)
        # ----------------------------------------------------------------------
        input_group = tk.LabelFrame(
            main_frame, 
            text=" 📝 STEP 1: Enter Your Personal Details ", 
            font=("Segoe UI", 10, "bold"), 
            fg=self.ACCENT_CYAN, 
            bg=self.PANEL_BG, 
            bd=1, 
            relief="solid", 
            padx=18, 
            pady=14
        )
        input_group.pack(fill="x", pady=(0, 14))

        # Fields Config
        fields = [
            ("Name (string):", "entry_name", "e.g., Alice"),
            ("Age (integer):", "entry_age", "e.g., 25"),
            ("Height in meters (float):", "entry_height", "e.g., 1.68"),
            ("Favourite Number (integer):", "entry_fav_num", "e.g., 7")
        ]

        self.entries = {}

        for idx, (label_text, var_name, placeholder) in enumerate(fields):
            lbl = tk.Label(
                input_group, 
                text=label_text, 
                font=("Segoe UI", 9, "bold"), 
                fg=self.TEXT_LIGHT, 
                bg=self.PANEL_BG
            )
            lbl.grid(row=idx, column=0, sticky="w", pady=6)

            entry = tk.Entry(
                input_group, 
                width=34, 
                font=("Consolas", 10), 
                bg=self.CARD_BG, 
                fg=self.TEXT_LIGHT, 
                insertbackground=self.TEXT_LIGHT, 
                bd=1, 
                relief="flat"
            )
            entry.grid(row=idx, column=1, pady=6, padx=12)
            
            # Focus Animation Bindings
            entry.bind("<FocusIn>", lambda e, widget=entry: self._on_focus_in(widget))
            entry.bind("<FocusOut>", lambda e, widget=entry: self._on_focus_out(widget))

            self.entries[var_name] = entry

        # Animated Progress Bar
        self.progress = ttk.Progressbar(
            input_group, 
            style="Custom.Horizontal.TProgressbar", 
            orient="horizontal", 
            mode="determinate"
        )
        self.progress.grid(row=4, column=0, columnspan=2, sticky="ew", pady=(10, 5))

        # Button Row
        btn_frame = tk.Frame(input_group, bg=self.PANEL_BG)
        btn_frame.grid(row=5, column=0, columnspan=2, pady=(8, 0))

        # Process Button with Hover Animation
        self.process_btn = tk.Button(
            btn_frame, 
            text="⚡ Process & Analyze Data", 
            command=self.start_processing_animation, 
            bg=self.ACCENT_GREEN, 
            fg="#ffffff", 
            font=("Segoe UI", 10, "bold"), 
            padx=18, 
            pady=6, 
            bd=0, 
            activebackground=self.HOVER_GREEN, 
            activeforeground="#ffffff", 
            cursor="hand2"
        )
        self.process_btn.pack(side="left", padx=8)
        self.process_btn.bind("<Enter>", lambda e: self.process_btn.config(bg=self.HOVER_GREEN))
        self.process_btn.bind("<Leave>", lambda e: self.process_btn.config(bg=self.ACCENT_GREEN))

        # Clear Button with Hover Animation
        self.clear_btn = tk.Button(
            btn_frame, 
            text="🧹 Clear Form", 
            command=self.clear_form, 
            bg=self.ACCENT_RED, 
            fg="#ffffff", 
            font=("Segoe UI", 10, "bold"), 
            padx=18, 
            pady=6, 
            bd=0, 
            activebackground=self.HOVER_RED, 
            activeforeground="#ffffff", 
            cursor="hand2"
        )
        self.clear_btn.pack(side="left", padx=8)
        self.clear_btn.bind("<Enter>", lambda e: self.clear_btn.config(bg=self.HOVER_RED))
        self.clear_btn.bind("<Leave>", lambda e: self.clear_btn.config(bg=self.ACCENT_RED))

        # ----------------------------------------------------------------------
        # 4. OUTPUT DISPLAY SECTION (CARD)
        # ----------------------------------------------------------------------
        output_group = tk.LabelFrame(
            main_frame, 
            text=" 📊 STEP 2: Live Analysis & Type Inspector ", 
            font=("Segoe UI", 10, "bold"), 
            fg=self.ACCENT_CYAN, 
            bg=self.PANEL_BG, 
            bd=1, 
            relief="solid", 
            padx=14, 
            pady=10
        )
        output_group.pack(fill="both", expand=True)

        # Output Text Console
        self.txt_output = tk.Text(
            output_group, 
            wrap="word", 
            font=("Consolas", 9), 
            bg="#090d16", 
            fg="#38bdf8", 
            insertbackground=self.TEXT_LIGHT, 
            bd=0, 
            padx=12, 
            pady=10
        )
        self.txt_output.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(output_group, command=self.txt_output.yview)
        scrollbar.pack(side="right", fill="y")
        self.txt_output.config(yscrollcommand=scrollbar.set)

        self.typing_job = None

    # --------------------------------------------------------------------------
    # FOCUS ANIMATION HELPERS
    # --------------------------------------------------------------------------
    def _on_focus_in(self, widget):
        widget.config(bg="#334155", highlightthickness=1, highlightbackground=self.ACCENT_CYAN)

    def _on_focus_out(self, widget):
        widget.config(bg=self.CARD_BG, highlightthickness=0)

    # --------------------------------------------------------------------------
    # PROCESSING & TYPEWRITER ANIMATION LOGIC
    # --------------------------------------------------------------------------
    def start_processing_animation(self):
        name_str = self.entries["entry_name"].get().strip()
        age_str = self.entries["entry_age"].get().strip()
        height_str = self.entries["entry_height"].get().strip()
        fav_num_str = self.entries["entry_fav_num"].get().strip()

        # Validation
        if not name_str or not age_str or not height_str or not fav_num_str:
            messagebox.showwarning("Input Error", "Please fill in all input fields!")
            return

        try:
            name = name_str
            age = int(age_str)
            height = float(height_str)
            favourite_number = int(fav_num_str)
        except ValueError:
            messagebox.showerror(
                "Type Casting Error", 
                "Invalid data types!\n- Age & Favourite Number must be integers (e.g., 25, 7)\n- Height must be a decimal float (e.g., 1.68)"
            )
            return

        # Animate progress bar step by step
        self.progress["value"] = 0
        self.animate_progress(0, lambda: self.render_typewriter_results(name, age, height, favourite_number))

    def animate_progress(self, val, on_complete):
        if val <= 100:
            self.progress["value"] = val
            self.root.after(8, lambda: self.animate_progress(val + 5, on_complete))
        else:
            on_complete()

    def render_typewriter_results(self, name, age, height, favourite_number):
        current_year = datetime.datetime.now().year
        birth_year = current_year - age
        height_as_int = int(height)

        # Build detailed formatted string
        text = "========================================================================\n"
        text += "                    📊 COLLECTED DATA & MEMORY INSPECTOR                \n"
        text += "========================================================================\n\n"

        text += f" [👤 Name]             : {name}\n"
        text += f"   ├── Data Type      : {type(name)}\n"
        text += f"   └── Memory Address : {id(name)}\n\n"

        text += f" [🎂 Age]              : {age}\n"
        text += f"   ├── Data Type      : {type(age)}\n"
        text += f"   └── Memory Address : {id(age)}\n\n"

        text += f" [📏 Height]           : {height} meters\n"
        text += f"   ├── Data Type      : {type(height)}\n"
        text += f"   └── Memory Address : {id(height)}\n\n"

        text += f" [🔢 Favourite Number] : {favourite_number}\n"
        text += f"   ├── Data Type      : {type(favourite_number)}\n"
        text += f"   └── Memory Address : {id(favourite_number)}\n\n"

        text += "------------------------------------------------------------------------\n"
        text += "                 🧮 CALCULATIONS & TYPE CONVERSION                      \n"
        text += "------------------------------------------------------------------------\n"
        text += f" 🎈 Calculated Birth Year : {birth_year} (Calculated as {current_year} - {age})\n\n"
        text += f" 🔄 Height Type Conversion: Float ({height}) -> Integer ({height_as_int})\n"
        text += f"   ├── Converted Type    : {type(height_as_int)}\n"
        text += f"   └── New Memory (id)   : {id(height_as_int)}\n\n"

        text += "========================================================================\n"
        text += " ✨ Processing Complete! Thank you for using Personal Data Collector! ✨\n"
        text += "========================================================================\n"

        # Cancel active typing job if any
        if self.typing_job:
            self.root.after_cancel(self.typing_job)

        self.txt_output.config(state="normal")
        self.txt_output.delete("1.0", tk.END)
        
        # Start typewriter animation
        self.typewriter_effect(text, 0)

    def typewriter_effect(self, full_text, index):
        if index < len(full_text):
            # Print chunks of 4 chars for smooth fast typing feel
            chunk = full_text[index:index+4]
            self.txt_output.insert(tk.END, chunk)
            self.txt_output.see(tk.END)
            self.typing_job = self.root.after(4, lambda: self.typewriter_effect(full_text, index+4))
        else:
            self.txt_output.config(state="disabled")

    def clear_form(self):
        if self.typing_job:
            self.root.after_cancel(self.typing_job)

        for entry in self.entries.values():
            entry.delete(0, tk.END)

        self.progress["value"] = 0
        self.txt_output.config(state="normal")
        self.txt_output.delete("1.0", tk.END)
        self.txt_output.config(state="disabled")


if __name__ == "__main__":
    root = tk.Tk()
    app = AnimatedPersonalDataApp(root)
    root.mainloop()

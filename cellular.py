import tkinter as tk
from tkinter import ttk

def rule_to_bin(rule_number):
    binary_rule = f"{rule_number:08b}"
    patterns = ["111", "110", "101", "100", "011", "010", "001", "000"]
    return {p: int(b) for p, b in zip(patterns, binary_rule)}

def evolve(current_gen, rule_dict):
    next_gen = ""
    padded = "0" + current_gen + "0"
    for i in range(len(current_gen)):
        neighborhood = padded[i:i+3]
        next_gen += str(rule_dict.get(neighborhood, 0))
    return next_gen

class CellularAutomatonApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Elementary Cellular Automaton (Play/Pause)")

        self.playing = False
        self.timer = None

        # === Controls ===
        control_frame = tk.Frame(root)
        control_frame.pack(pady=10)

        tk.Label(control_frame, text="Rule (0-255):").grid(row=0, column=0)
        self.rule_entry = tk.Entry(control_frame, width=5)
        self.rule_entry.insert(0, "110")
        self.rule_entry.grid(row=0, column=1)

        tk.Label(control_frame, text="Width:").grid(row=0, column=2)
        self.width_entry = tk.Entry(control_frame, width=5)
        self.width_entry.insert(0, "100")
        self.width_entry.grid(row=0, column=3)

        tk.Label(control_frame, text="Steps:").grid(row=0, column=4)
        self.steps_entry = tk.Entry(control_frame, width=5)
        self.steps_entry.insert(0, "150")
        self.steps_entry.grid(row=0, column=5)

        self.play_button = tk.Button(control_frame, text="Play", command=self.toggle_play)
        self.play_button.grid(row=0, column=6, padx=5)

        self.reset_button = tk.Button(control_frame, text="Reset", command=self.reset)
        self.reset_button.grid(row=0, column=7, padx=5)

        # === Canvas + Scrollbar ===
        self.canvas_frame = tk.Frame(root)
        self.canvas_frame.pack(fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(self.canvas_frame, bg="white", height=600)
        self.scrollbar = ttk.Scrollbar(self.canvas_frame, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.cell_size = 5
        self.reset()

    def toggle_play(self):
        if not self.playing:
            self.playing = True
            self.play_button.config(text="Pause")
            self.run_generation()
        else:
            self.playing = False
            self.play_button.config(text="Play")
            if self.timer:
                self.root.after_cancel(self.timer)

    def run_generation(self):
        if self.current_step >= self.steps or not self.playing:
            self.toggle_play()  # auto pause
            return

        # Draw current generation
        for i, c in enumerate(self.current_gen):
            if c == "1":
                x = i * self.cell_size
                y = self.current_step * self.cell_size
                self.canvas.create_rectangle(x, y, x+self.cell_size, y+self.cell_size, fill="black", outline="")

        self.current_gen = evolve(self.current_gen, self.rule_dict)
        self.current_step += 1
        self.canvas.config(scrollregion=(0, 0, self.width * self.cell_size, self.steps * self.cell_size))

        # Auto-scroll down as it grows
        self.canvas.yview_moveto(self.current_step / self.steps)

        # Continue animation
        self.timer = self.root.after(50, self.run_generation)

    def reset(self):
        # Stop running animation
        self.playing = False
        self.play_button.config(text="Play")
        if self.timer:
            self.root.after_cancel(self.timer)

        # Grab values from UI
        try:
            self.rule = int(self.rule_entry.get())
            self.width = int(self.width_entry.get())
            self.steps = int(self.steps_entry.get())
            if not (0 <= self.rule <= 255):
                raise ValueError
        except ValueError:
            print("Please enter valid integers for rule (0–255), width, and steps.")
            return

        # Setup new simulation
        self.rule_dict = rule_to_bin(self.rule)
        self.current_gen = "0" * (self.width // 2) + "1" + "0" * (self.width // 2)
        self.current_step = 0

        self.canvas.delete("all")
        self.canvas.config(scrollregion=(0, 0, self.width * self.cell_size, self.steps * self.cell_size))
        self.canvas.yview_moveto(0)

if __name__ == "__main__":
    root = tk.Tk()
    app = CellularAutomatonApp(root)
    root.mainloop()

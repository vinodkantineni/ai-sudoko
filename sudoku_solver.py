import tkinter as tk
from tkinter import ttk, messagebox
import time, random

PUZZLES = {
    "Easy": [
        [[5, 3, 0, 0, 7, 0, 0, 0, 0],
         [6, 0, 0, 1, 9, 5, 0, 0, 0],
         [0, 9, 8, 0, 0, 0, 0, 6, 0],
         [8, 0, 0, 0, 6, 0, 0, 0, 3],
         [4, 0, 0, 8, 0, 3, 0, 0, 1],
         [7, 0, 0, 0, 2, 0, 0, 0, 6],
         [0, 6, 0, 0, 0, 0, 2, 8, 0],
         [0, 0, 0, 4, 1, 9, 0, 0, 5],
         [0, 0, 0, 0, 8, 0, 0, 7, 9]],
        [[0, 0, 0, 2, 6, 0, 7, 0, 1],
         [6, 8, 0, 0, 7, 0, 0, 9, 0],
         [1, 9, 0, 0, 0, 4, 5, 0, 0],
         [8, 2, 0, 1, 0, 0, 0, 4, 0],
         [0, 0, 4, 6, 0, 2, 9, 0, 0],
         [0, 5, 0, 0, 0, 3, 0, 2, 8],
         [0, 0, 9, 3, 0, 0, 0, 7, 4],
         [0, 4, 0, 0, 5, 0, 0, 3, 6],
         [7, 0, 3, 0, 1, 8, 0, 0, 0]],
        [[0, 0, 0, 0, 6, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 5, 0, 0, 0],
         [0, 8, 9, 0, 0, 0, 6, 0, 0],
         [2, 0, 0, 9, 0, 0, 0, 0, 8],
         [0, 4, 0, 0, 0, 0, 0, 3, 0],
         [3, 0, 0, 0, 0, 2, 0, 0, 7],
         [0, 0, 3, 0, 0, 0, 2, 5, 0],
         [0, 0, 0, 7, 0, 4, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 0]],
        [[8, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 3, 6, 0, 0, 0, 0, 0],
         [0, 7, 0, 0, 9, 0, 2, 0, 0],
         [0, 5, 0, 0, 0, 7, 0, 0, 0],
         [0, 0, 0, 0, 4, 5, 7, 0, 0],
         [0, 0, 0, 1, 0, 0, 0, 3, 0],
         [0, 0, 1, 0, 0, 0, 0, 6, 8],
         [0, 0, 8, 5, 0, 0, 0, 1, 0],
         [0, 9, 0, 0, 0, 0, 4, 0, 0]],
        [[0, 0, 0, 0, 0, 9, 0, 7, 0],
         [0, 0, 0, 0, 6, 0, 0, 0, 0],
         [0, 0, 5, 0, 0, 0, 9, 0, 0],
         [0, 0, 0, 0, 0, 1, 0, 0, 0],
         [8, 0, 0, 9, 0, 0, 0, 0, 6],
         [0, 2, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 5, 0, 0, 3, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 5, 0],
         [0, 0, 0, 0, 0, 0, 6, 0, 4]],
        [[0, 6, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 9, 5, 0, 0, 0, 0, 8],
         [0, 0, 1, 0, 0, 0, 2, 0, 0],
         [0, 0, 0, 0, 0, 6, 0, 0, 0],
         [0, 7, 0, 0, 3, 0, 0, 9, 0],
         [0, 0, 0, 9, 0, 0, 0, 0, 0],
         [0, 0, 8, 0, 0, 0, 4, 0, 0],
         [3, 0, 0, 0, 0, 2, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 8, 0]]
    ],
"Medium": [
    [[0, 0, 0, 0, 0, 0, 2, 0, 0],
     [0, 8, 0, 0, 0, 7, 0, 9, 0],
     [6, 0, 2, 0, 0, 0, 5, 0, 0],
     [0, 7, 0, 0, 6, 0, 0, 0, 0],
     [0, 0, 0, 9, 0, 1, 0, 0, 0],
     [0, 0, 0, 0, 2, 0, 0, 4, 0],
     [0, 0, 5, 0, 0, 0, 6, 0, 3],
     [0, 9, 0, 4, 0, 0, 0, 7, 0],
     [0, 0, 6, 0, 0, 0, 0, 0, 0]],

    [[0, 0, 0, 0, 0, 0, 4, 0, 2],
     [0, 0, 6, 0, 0, 0, 0, 0, 0],
     [0, 8, 0, 0, 0, 0, 0, 3, 0],
     [0, 9, 0, 5, 0, 0, 0, 7, 0],
     [4, 0, 0, 0, 0, 0, 0, 0, 9],
     [0, 1, 0, 0, 0, 3, 0, 2, 0],
     [0, 2, 0, 0, 0, 0, 0, 5, 0],
     [0, 0, 0, 0, 0, 0, 3, 0, 0],
     [6, 0, 4, 0, 0, 0, 0, 0, 0]],

    [[0, 0, 3, 0, 2, 0, 6, 0, 0],
     [9, 0, 0, 3, 0, 5, 0, 0, 1],
     [0, 0, 1, 8, 0, 6, 4, 0, 0],
     [0, 0, 8, 1, 0, 2, 9, 0, 0],
     [7, 0, 0, 0, 0, 0, 0, 0, 8],
     [0, 0, 6, 7, 0, 8, 2, 0, 0],
     [0, 0, 2, 6, 0, 9, 5, 0, 0],
     [8, 0, 0, 2, 0, 3, 0, 0, 9],
     [0, 0, 5, 0, 1, 0, 3, 0, 0]],

    [[0, 3, 0, 0, 0, 5, 0, 0, 9],
     [0, 0, 0, 2, 0, 0, 0, 5, 0],
     [0, 0, 0, 0, 3, 0, 6, 0, 0],
     [5, 0, 0, 0, 0, 0, 0, 8, 0],
     [0, 9, 0, 0, 7, 0, 0, 2, 0],
     [0, 1, 0, 0, 0, 0, 0, 0, 6],
     [0, 0, 9, 0, 1, 0, 0, 0, 0],
     [0, 6, 0, 0, 0, 4, 0, 0, 0],
     [8, 0, 0, 6, 0, 0, 0, 1, 0]],

    [[0, 0, 0, 0, 0, 6, 0, 0, 0],
     [0, 4, 0, 0, 2, 0, 0, 3, 0],
     [0, 0, 2, 0, 0, 9, 0, 0, 0],
     [0, 0, 7, 0, 0, 0, 0, 0, 2],
     [3, 0, 0, 0, 0, 0, 0, 0, 5],
     [4, 0, 0, 0, 0, 0, 6, 0, 0],
     [0, 0, 0, 5, 0, 0, 9, 0, 0],
     [0, 6, 0, 0, 9, 0, 0, 1, 0],
     [0, 0, 0, 6, 0, 0, 0, 0, 0]],

    [[0, 0, 6, 0, 0, 0, 8, 0, 0],
     [0, 1, 0, 9, 0, 5, 0, 7, 0],
     [2, 0, 0, 0, 1, 0, 0, 0, 3],
     [0, 0, 0, 0, 0, 0, 5, 0, 0],
     [8, 0, 0, 0, 0, 0, 0, 0, 4],
     [0, 0, 1, 0, 0, 0, 0, 0, 0],
     [5, 0, 0, 0, 3, 0, 0, 0, 6],
     [0, 4, 0, 2, 0, 9, 0, 3, 0],
     [0, 0, 3, 0, 0, 0, 7, 0, 0]]
],
      "Hard": [
        [[0, 0, 0, 0, 0, 0, 0, 1, 2],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 5, 0, 0, 4, 0, 7],
         [0, 0, 2, 0, 0, 6, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 3, 0],
         [0, 0, 0, 0, 0, 7, 0, 0, 0],
         [3, 0, 0, 6, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 0, 0]],

        [[0, 0, 0, 6, 0, 0, 4, 0, 0],
         [7, 0, 0, 0, 0, 3, 6, 0, 0],
         [0, 0, 0, 0, 9, 1, 0, 8, 0],
         [0, 0, 7, 0, 4, 0, 2, 6, 0],
         [0, 0, 1, 0, 5, 0, 9, 3, 0],
         [9, 0, 4, 0, 0, 0, 0, 0, 5],
         [0, 7, 0, 3, 0, 0, 0, 1, 2],
         [1, 2, 0, 0, 0, 7, 4, 0, 0],
         [0, 4, 9, 2, 0, 6, 0, 0, 0]],

        [[0, 0, 5, 0, 0, 0, 3, 0, 0],
         [8, 0, 0, 0, 0, 0, 0, 2, 0],
         [0, 7, 0, 0, 0, 4, 0, 0, 0],
         [0, 0, 6, 0, 0, 0, 0, 0, 0],
         [0, 9, 0, 8, 0, 0, 0, 4, 0],
         [0, 0, 0, 0, 7, 5, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 3, 0],
         [0, 0, 2, 0, 6, 0, 0, 0, 9],
         [0, 4, 0, 0, 0, 0, 7, 0, 0]],

        [[0, 0, 0, 0, 0, 8, 0, 0, 0],
         [0, 0, 0, 4, 0, 0, 0, 0, 9],
         [2, 0, 0, 0, 0, 0, 6, 0, 0],
         [0, 0, 0, 7, 0, 0, 0, 0, 6],
         [0, 0, 0, 0, 9, 1, 0, 0, 0],
         [0, 2, 0, 0, 0, 0, 8, 0, 0],
         [0, 3, 0, 0, 0, 6, 0, 0, 0],
         [7, 0, 0, 0, 0, 0, 0, 5, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 0]],

        [[0, 0, 0, 0, 3, 0, 0, 6, 0],
         [0, 0, 0, 9, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 8, 1, 0, 0],
         [0, 6, 0, 0, 0, 0, 0, 9, 0],
         [0, 0, 1, 0, 8, 0, 0, 0, 0],
         [0, 0, 0, 5, 0, 0, 4, 0, 0],
         [3, 0, 0, 0, 0, 0, 0, 7, 0],
         [0, 0, 0, 0, 2, 6, 0, 0, 0],
         [0, 4, 0, 0, 0, 0, 0, 0, 0]],

        [[0, 5, 0, 0, 0, 0, 0, 0, 8],
         [0, 0, 0, 0, 7, 0, 0, 4, 0],
         [0, 0, 0, 5, 0, 0, 0, 0, 0],
         [0, 0, 9, 0, 0, 4, 0, 0, 0],
         [5, 0, 0, 0, 0, 0, 7, 0, 0],
         [0, 0, 0, 1, 0, 0, 0, 0, 6],
         [0, 0, 0, 0, 0, 5, 0, 9, 0],
         [0, 0, 0, 0, 4, 0, 0, 0, 0],
         [0, 2, 6, 0, 0, 0, 0, 0, 0]]
    ]
}

class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🧠 Sudoku Solver")
        self.entries = [[None] * 9 for _ in range(9)]
        self.grid = [[0] * 9 for _ in range(9)]
        self.timer_label = tk.Label(self.root, text="Time: 0.00s", font=("Arial", 12))
        self.timer_label.pack(pady=5)
        self.start_time = None

        container = tk.Frame(self.root, padx=10, pady=10, bg="#f0f0f0")
        container.pack()

        self.difficulty = tk.StringVar()
        self.difficulty_combo = ttk.Combobox(container, textvariable=self.difficulty, values=["Easy", "Medium", "Hard"], state="readonly", font=("Arial", 12), width=10)
        self.difficulty_combo.grid(row=0, column=0, columnspan=9, pady=(0, 10))
        self.difficulty_combo.current(0)
        self.difficulty_combo.bind("<<ComboboxSelected>>", self.load_random)

        for i in range(9):
            for j in range(9):
                e = tk.Entry(container, width=2, font=("Arial", 18), justify="center", relief="solid", bd=1)
                e.grid(row=i + 1, column=j, padx=(1 if j % 3 == 0 else 0, 1), pady=(1 if i % 3 == 0 else 0, 1))
                self.entries[i][j] = e

        tk.Button(container, text="Solve", font=("Arial", 12), bg="green", fg="white", command=self.solve).grid(row=10, column=0, columnspan=9, pady=10)
        self.load_random()

    def load_random(self, event=None):
        level = self.difficulty.get() or "Easy"
        puzzle = random.choice(PUZZLES[level])
        for i in range(9):
            for j in range(9):
                val = puzzle[i][j]
                entry = self.entries[i][j]
                entry.config(state="normal")
                entry.delete(0, tk.END)
                if val != 0:
                    entry.insert(0, str(val))
                    entry.config(fg='black')
                else:
                    entry.config(fg='blue')

    def read_grid(self):
        for i in range(9):
            for j in range(9):
                val = self.entries[i][j].get()
                self.grid[i][j] = int(val) if val.isdigit() else 0

    def update_gui(self, r, c, val):
        entry = self.entries[r][c]
        entry.delete(0, tk.END)
        if val:
            entry.insert(0, str(val))
        self.root.update()
        time.sleep(0.02)

    def is_valid(self, r, c, num):
        for i in range(9):
            if self.grid[r][i] == num or self.grid[i][c] == num:
                return False
        br, bc = 3 * (r // 3), 3 * (c // 3)
        for i in range(br, br + 3):
            for j in range(bc, bc + 3):
                if self.grid[i][j] == num:
                    return False
        return True

    def solve_sudoku(self):
        for r in range(9):
            for c in range(9):
                if self.grid[r][c] == 0:
                    for num in range(1, 10):
                        if self.is_valid(r, c, num):
                            self.grid[r][c] = num
                            self.update_gui(r, c, num)
                            if self.solve_sudoku():
                                return True
                            self.grid[r][c] = 0
                            self.update_gui(r, c, "")
                    return False
        return True

    def solve(self):
        self.read_grid()
        self.start_time = time.time()
        solved = self.solve_sudoku()
        duration = time.time() - self.start_time
        self.timer_label.config(text=f"Time: {duration:.2f} seconds")
        if not solved:
            messagebox.showerror("Sudoku", "No solution exists!")

root = tk.Tk()
app = SudokuGUI(root)
root.mainloop()

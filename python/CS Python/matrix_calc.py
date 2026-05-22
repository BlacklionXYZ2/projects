import tkinter as tk
from tkinter import messagebox, ttk
import numpy as np

class MatrixCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dynamic Matrix Calculator - Independent Matrices")
        self.root.geometry("900x750")

        # --- Variables ---
        self.rows_a = tk.IntVar(value = 2)
        self.cols_a = tk.IntVar(value = 2)
        self.rows_b = tk.IntVar(value = 2)
        self.cols_b = tk.IntVar(value = 2)
        
        self.entries_a = []
        self.entries_b = []

        # --- Top Section: Controls & Generators ---
        top_frame = tk.Frame(root)
        top_frame.pack(pady = 10, fill = "x", padx = 20)

        # Control Panel A (Left)
        ctrl_a = tk.LabelFrame(top_frame, text = "Matrix A Settings", padx = 10, pady = 5)
        ctrl_a.pack(side = "left", fill = "both", expand = True, padx = 5)
        
        tk.Label(ctrl_a, text = "Dims:").grid(row = 0, column = 0)
        tk.Spinbox(ctrl_a, from_ = 1, to = 10, textvariable = self.rows_a, width = 3).grid(row = 0, column = 1)
        tk.Label(ctrl_a, text = "x").grid(row = 0, column = 2)
        tk.Spinbox(ctrl_a, from_ = 1, to = 10, textvariable = self.cols_a, width = 3).grid(row = 0, column = 3)
        tk.Button(ctrl_a, text = "Resize A", command = lambda: self.build_grid('A')).grid(row = 0, column = 4, padx = 10)

        tk.Button(ctrl_a, text = "Zero", command = lambda: self.fill_matrix('A', 'zero')).grid(row = 1, column = 0, columnspan = 2, pady = 5, sticky = "we")
        tk.Button(ctrl_a, text = "Identity", command = lambda: self.fill_matrix('A', 'identity')).grid(row = 1, column = 2, columnspan = 2, pady = 5, sticky = "we")
        tk.Button(ctrl_a, text = "Rotation...", command = lambda: self.open_rotation_dialog('A')).grid(row = 1, column = 4, padx = 10, pady = 5)

        # Control Panel B (Right)
        ctrl_b = tk.LabelFrame(top_frame, text = "Matrix B Settings", padx = 10, pady = 5)
        ctrl_b.pack(side = "right", fill = "both", expand = True, padx = 5)

        tk.Label(ctrl_b, text = "Dims:").grid(row = 0, column = 0)
        tk.Spinbox(ctrl_b, from_ = 1, to = 10, textvariable = self.rows_b, width = 3).grid(row = 0, column = 1)
        tk.Label(ctrl_b, text = "x").grid(row = 0, column = 2)
        tk.Spinbox(ctrl_b, from_ = 1, to = 10, textvariable = self.cols_b, width = 3).grid(row = 0, column = 3)
        tk.Button(ctrl_b, text = "Resize B", command = lambda: self.build_grid('B')).grid(row = 0, column = 4, padx = 10)

        tk.Button(ctrl_b, text = "Zero", command = lambda: self.fill_matrix('B', 'zero')).grid(row = 1, column = 0, columnspan = 2, pady = 5, sticky = "we")
        tk.Button(ctrl_b, text = "Identity", command = lambda: self.fill_matrix('B', 'identity')).grid(row = 1, column = 2, columnspan = 2, pady = 5, sticky = "we")
        tk.Button(ctrl_b, text = "Rotation...", command = lambda: self.open_rotation_dialog('B')).grid(row = 1, column = 4, padx = 10, pady = 5)

        # --- Middle Section: Matrix Grids ---
        self.grid_frame = tk.Frame(root)
        self.grid_frame.pack(pady = 10)
        
        self.frame_a = tk.LabelFrame(self.grid_frame, text = "Matrix A")
        self.frame_a.grid(row = 0, column = 0, padx = 20, sticky = "n")
        
        self.frame_b = tk.LabelFrame(self.grid_frame, text = "Matrix B")
        self.frame_b.grid(row = 0, column = 1, padx = 20, sticky = "n")

        # --- Operations Section ---
        op_frame = tk.Frame(root, pady = 10)
        op_frame.pack()

        tk.Label(op_frame, text = "Operations:", font = ("Arial", 10, "bold")).grid(row = 0, column = 0, columnspan = 7, pady = 5)
        tk.Button(op_frame, text = "A + B", command = lambda: self.calculate('add')).grid(row = 1, column = 0, padx = 5)
        tk.Button(op_frame, text = "A * B", command = lambda: self.calculate('multiply')).grid(row = 1, column = 1, padx = 5)
        tk.Button(op_frame, text = "sin(A)", command = lambda: self.calculate('sin')).grid(row = 1, column = 2, padx = 5)
        tk.Button(op_frame, text = "cos(A)", command = lambda: self.calculate('cos')).grid(row = 1, column = 3, padx = 5)
        tk.Button(op_frame, text = "e^A", command = lambda: self.calculate('exp')).grid(row = 1, column = 4, padx = 5)
        tk.Button(op_frame, text = "√A", command = lambda: self.calculate('sqrt')).grid(row = 1, column = 5, padx = 5)
        tk.Button(op_frame, text = "A^2", command = lambda: self.calculate('power2')).grid(row = 1, column = 6, padx = 5)

        # --- Bottom Section: Results ---
        res_frame = tk.LabelFrame(root, text = "Result")
        res_frame.pack(fill = "both", expand = True, padx = 20, pady = 10)
        self.result_text = tk.Text(res_frame, height = 8, state = "disabled", font = ("Courier", 12))
        self.result_text.pack(fill = "both", expand = True, padx = 5, pady = 5)

        # Initialize default grids
        self.build_grid('A')
        self.build_grid('B')

    def build_grid(self, matrix_name):
        """Builds or rebuilds a specific matrix grid."""
        if matrix_name == 'A':
            rows, cols = self.rows_a.get(), self.cols_a.get()
            target_frame = self.frame_a
            self.entries_a.clear()
            target_list = self.entries_a
        else:
            rows, cols = self.rows_b.get(), self.cols_b.get()
            target_frame = self.frame_b
            self.entries_b.clear()
            target_list = self.entries_b

        # Clear existing widgets in the target frame
        for widget in target_frame.winfo_children():
            widget.destroy()

        # Rebuild grid
        for r in range(rows):
            row_entries = []
            for c in range(cols):
                entry = tk.Entry(target_frame, width = 6, justify = "center")
                entry.insert(0, "0")
                entry.grid(row = r, column = c, padx = 2, pady = 2)
                row_entries.append(entry)
            target_list.append(row_entries)

    def get_matrix_data(self, entries):
        """Extracts data from the tkinter Entry grid into a numpy array."""
        if not entries: return None
        try:
            return np.array([[float(entry.get()) for entry in row] for row in entries])
        except ValueError:
            messagebox.showerror("Input Error", "Please ensure all matrix cells contain valid numbers.")
            return None

    def fill_matrix(self, matrix_name, fill_type):
        """Fills a specific matrix with 0s or an Identity matrix."""
        if matrix_name == 'A':
            rows, cols, entries = self.rows_a.get(), self.cols_a.get(), self.entries_a
        else:
            rows, cols, entries = self.rows_b.get(), self.cols_b.get(), self.entries_b

        if fill_type == 'identity' and rows != cols:
            messagebox.showwarning("Dimension Error", f"Matrix {matrix_name} must be square (Rows = Cols) for an identity matrix.")
            return

        for r in range(rows):
            for c in range(cols):
                entries[r][c].delete(0, tk.END)
                if fill_type == 'zero':
                    entries[r][c].insert(0, "0")
                elif fill_type == 'identity':
                    entries[r][c].insert(0, "1" if r == c else "0")

    def open_rotation_dialog(self, target_matrix):
        """Opens a dialog to generate a rotation matrix for A or B."""
        dialog = tk.Toplevel(self.root)
        dialog.title(f"Generate Rotation Matrix -> {target_matrix}")
        dialog.geometry("300x200")
        dialog.transient(self.root)
        dialog.grab_set()

        tk.Label(dialog, text = "Select Plane/Axis:").pack(pady = 5)
        plane_var = tk.StringVar()
        plane_cb = ttk.Combobox(dialog, textvariable = plane_var, state = "readonly", width = 25)
        plane_cb['values'] = [
            "2D: XY Plane", 
            "3D: X-Axis (YZ Plane)", 
            "3D: Y-Axis (XZ Plane)", 
            "3D: Z-Axis (XY Plane)"
        ]
        plane_cb.current(0)
        plane_cb.pack(pady = 5)

        tk.Label(dialog, text = "Angle (Degrees):").pack(pady = 5)
        angle_var = tk.StringVar(value = "90")
        tk.Entry(dialog, textvariable = angle_var, justify = "center").pack(pady = 5)

        def apply_rotation():
            try:
                angle_deg = float(angle_var.get())
                angle_rad = np.radians(angle_deg)
                choice = plane_var.get()

                c, s = np.cos(angle_rad), np.sin(angle_rad)

                if "2D" in choice:
                    mat, dim = np.array([[c, -s], [s, c]]), 2
                elif "X-Axis" in choice:
                    mat, dim = np.array([[1, 0, 0], [0, c, -s], [0, s, c]]), 3
                elif "Y-Axis" in choice:
                    mat, dim = np.array([[c, 0, s], [0, 1, 0], [-s, 0, c]]), 3
                elif "Z-Axis" in choice:
                    mat, dim = np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]]), 3

                mat = np.round(mat, decimals = 5)

                # Resize the targeted grid
                if target_matrix == 'A':
                    self.rows_a.set(dim + 1)
                    self.cols_a.set(dim + 1)
                    self.build_grid('A')
                    entries = self.entries_a
                else:
                    self.rows_b.set(dim + 1)
                    self.cols_b.set(dim + 1)
                    self.build_grid('B')
                    entries = self.entries_b

                # Inject values
                for r in range(dim):
                    for col in range(dim):
                        entries[r][col].delete(0, tk.END)
                        val = str(mat[r][col])
                        if val.endswith('.0'): val = val[:-2]
                        entries[r][col].insert(0, val)
                
                dialog.destroy()

            except ValueError:
                messagebox.showerror("Input Error", "Please enter a valid numeric angle.")

        tk.Button(dialog, text = f"Generate into Matrix {target_matrix}", command = apply_rotation).pack(pady = 10)

    def display_result(self, result_matrix):
        """Formats and displays the numpy array in the text box."""
        self.result_text.config(state = "normal")
        self.result_text.delete("1.0", tk.END)
        formatted = np.round(result_matrix, decimals = 4)
        self.result_text.insert(tk.END, str(formatted))
        self.result_text.config(state = "disabled")

    def calculate(self, operation):
        """Handles operations, leveraging numpy's built-in dimension checking."""
        A = self.get_matrix_data(self.entries_a)
        B = self.get_matrix_data(self.entries_b)

        if A is None or B is None:
            return 

        try:
            if operation == 'add':
                if A.shape != B.shape:
                    messagebox.showerror("Dimension Error", f"Addition requires matrices of the exact same size.\nA is {A.shape[0]}x{A.shape[1]}, B is {B.shape[0]}x{B.shape[1]}")
                    return
                result = np.add(A, B)
            elif operation == 'multiply':
                if A.shape[1] != B.shape[0]:
                    messagebox.showerror("Dimension Error", f"To multiply A * B, Matrix A columns ({A.shape[1]}) must equal Matrix B rows ({B.shape[0]}).")
                    return
                result = np.dot(A, B)
            elif operation == 'sin':
                result = np.sin(A)
            elif operation == 'cos':
                result = np.cos(A)
            elif operation == 'exp':
                result = np.exp(A)
            elif operation == 'sqrt':
                if np.any(A < 0):
                    messagebox.showerror("Math Error", "Cannot calculate real square root of negative numbers.")
                    return
                result = np.sqrt(A)
            elif operation == 'power2':
                if A.shape[0] != A.shape[1]:
                    messagebox.showerror("Math Error", "Matrix must be square to calculate powers.")
                    return
                result = np.linalg.matrix_power(A, 2)
            else:
                return

            self.display_result(result)

        except Exception as e:
            messagebox.showerror("Math Error", f"An error occurred during calculation:\n{str(e)}")


root = tk.Tk()
app = MatrixCalculatorApp(root)
root.mainloop()
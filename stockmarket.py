import tkinter as tk
from tkinter import ttk

# Class to store company information
class CompanyInfo:
    def __init__(self, name, market_cap, revenue, pe_ratio, dividend_yield):
        self.name = name
        self.market_cap = market_cap
        self.revenue = revenue
        self.pe_ratio = pe_ratio
        self.dividend_yield = dividend_yield

# Tree node for the binary search tree
class TreeNode:
    def __init__(self, company):
        self.company = company
        self.left = None
        self.right = None

# Binary search tree for managing companies
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, company):
        if not self.root:
            self.root = TreeNode(company)
        else:
            self._insert_recursive(self.root, company)

    def _insert_recursive(self, node, company):
        current_value = (
            node.company.market_cap + node.company.revenue -
            node.company.pe_ratio + node.company.dividend_yield
        )
        new_value = (
            company.market_cap + company.revenue -
            company.pe_ratio + company.dividend_yield
        )
        if new_value > current_value:
            if node.right:
                self._insert_recursive(node.right, company)
            else:
                node.right = TreeNode(company)
        else:
            if node.left:
                self._insert_recursive(node.left, company)
            else:
                node.left = TreeNode(company)

# Investment advisor GUI application
class InvestmentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Company Investment Advisor")
        self.company_binary_tree = BinarySearchTree()

        # GUI setup
        ttk.Label(root, text="Company Name:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.name_entry = ttk.Entry(root, width=15)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(root, text="Market Cap:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.market_cap_entry = ttk.Entry(root, width=15)
        self.market_cap_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(root, text="Revenue:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.revenue_entry = ttk.Entry(root, width=15)
        self.revenue_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(root, text="P/E Ratio:").grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
        self.pe_ratio_entry = ttk.Entry(root, width=15)
        self.pe_ratio_entry.grid(row=3, column=1, padx=5, pady=5)

        ttk.Label(root, text="Dividend Yield:").grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
        self.dividend_yield_entry = ttk.Entry(root, width=15)
        self.dividend_yield_entry.grid(row=4, column=1, padx=5, pady=5)

        self.add_button = ttk.Button(root, text="Add Company", command=self.add_company)
        self.add_button.grid(row=5, column=0, columnspan=2, pady=10)

        self.result_text = tk.Text(root, width=50, height=10)
        self.result_text.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

    def add_company(self):
        # Get input values
        name = self.name_entry.get()
        market_cap = float(self.market_cap_entry.get())
        revenue = float(self.revenue_entry.get())
        pe_ratio = float(self.pe_ratio_entry.get())
        dividend_yield = float(self.dividend_yield_entry.get())

        # Create a company object and add to the tree
        company = CompanyInfo(name, market_cap, revenue, pe_ratio, dividend_yield)
        self.company_binary_tree.insert(company)

        # Clear input fields and update results
        self.clear_entries()
        self.result_text.insert(tk.END, f"Company {name} added successfully!\n\n")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.market_cap_entry.delete(0, tk.END)
        self.revenue_entry.delete(0, tk.END)
        self.pe_ratio_entry.delete(0, tk.END)
        self.dividend_yield_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = InvestmentApp(root)
    root.mainloop()

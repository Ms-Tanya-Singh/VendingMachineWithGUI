import tkinter as tk

# Backend logic for the vending machine
class VendingMachine:
    def __init__(self):
        self.inventory = {
            "Soda": {"price": 1.50, "count": 10},
            "Water": {"price": 1.00, "count": 10},
            "Coffee": {"price": 2.00, "count": 10},
            "Chips": {"price": 1.75, "count": 5},
            "Candy": {"price": 1.25, "count": 7}
        }

    def buy(self, item):
        if self.inventory[item]["count"] <= 0:
            return f"{item} is out of stock."
        self.inventory[item]["count"] -= 1
        return f"Dispensed one {item}."

    def restock(self, item, amount):
        self.inventory[item]["count"] += amount
        return f"Restocked {amount} units of {item}."


# GUI class using tkinter
class VendingApp:
    def __init__(self, root, machine):
        self.machine = machine
        self.root = root
        self.root.title("Vending Machine")
        self.root.geometry("400x500")

        self.message = tk.StringVar()
        self.selected_item = tk.StringVar(value="Soda")
        self.amount_entry = tk.StringVar()

        tk.Label(root, text="Vending Machine", font=("Helvetica", 16)).pack(pady=10)

        self.buttons_frame = tk.Frame(root)
        self.buttons_frame.pack(pady=5)
        self.render_buttons()

        tk.Label(root, text="Select item to restock:").pack()
        tk.OptionMenu(root, self.selected_item, *machine.inventory.keys()).pack()
        tk.Entry(root, textvariable=self.amount_entry, width=10).pack()
        tk.Button(root, text="Restock", command=self.handle_restock).pack(pady=5)

        tk.Label(root, textvariable=self.message, wraplength=300, fg="blue").pack(pady=10)

    def render_buttons(self):
        for widget in self.buttons_frame.winfo_children():
            widget.destroy()
        for item in self.machine.inventory:
            info = self.machine.inventory[item]
            btn_text = f"{item} - ${info['price']:.2f} ({info['count']} left)"
            btn = tk.Button(self.buttons_frame, text=btn_text,
                            command=lambda i=item: self.handle_buy(i), width=30)
            btn.pack(pady=2)

    def handle_buy(self, item):
        result = self.machine.buy(item)
        self.message.set(result)
        self.render_buttons()

    def handle_restock(self):
        item = self.selected_item.get()
        try:
            amount = int(self.amount_entry.get())
            result = self.machine.restock(item, amount)
            self.message.set(result)
            self.render_buttons()
        except ValueError:
            self.message.set("Please enter a valid number.")


if __name__ == "__main__":
    root = tk.Tk()
    machine = VendingMachine()
    app = VendingApp(root, machine)
    root.mainloop()

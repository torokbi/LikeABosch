import models
import tkinter as tk
import sqlite3

index = 1

senzors = sqlite3.connect("db.db")

# for row in senzors.execute("SELECT * FROM Group_349_1"):
#     print(row)


root = tk.Tk()
root.geometry('500x500')
root.resizable(False, False)
root.title('Car area')

car_button = tk.Button(
        root,
        state = tk.DISABLED,
        fg = 'white',
        text = 'Car',
        bg = 'blue',
        command = lambda: root.quit()
    )

car_button.pack(
    ipadx=14.56,
    ipady=42.4002,
    expand=True,
    padx=0,
    pady=0,
)

for row in senzors.execute("SELECT * FROM Group_349_1"):
    barriers = tk.Button(
        state= tk.DISABLED,
        bg='red',
    )
    barriers.pack(
        ipadx=2,
        ipady=2,
        expand=True,
        padx=,
        pady=,
    )
    index += 1
    break

root.mainloop()


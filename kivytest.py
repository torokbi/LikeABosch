import tkinter as tk

root = tk.Tk()
root.geometry('500x500')
root.resizable(False, False)
root.title('Button Demo')

# exit button
exit_button = tk.Button(
    root,
    state= tk.DISABLED,
    text='Car',
    command=lambda: root.quit()
)

exit_button.pack(
    ipadx=14.56,
    ipady=42.4002,
    expand=True
)

root.mainloop()
from tkinter import Tk, Label
from psutil import cpu_percent, virtual_memory


def get_color(percent):
    """Return a color based on current usage percentage."""

    if percent < 10:
        return "blue2"
    elif 10 < percent < 30:
        return "cyan4"
    elif 30 < percent < 50:
        return "dark green"
    elif 50 < percent < 70:
        return "coral"
    elif 70 < percent < 85:
        return "OrangeRed2"
    elif 85 < percent < 100:
        return "red3"

    return "black"


def get_resource_usage():
    """Get and display CPU and RAM usage every second."""

    cpu_usage = cpu_percent()
    cpu_load_label.config(text=f"{cpu_usage}%", fg=get_color(int(cpu_usage)))
    memory_usage = virtual_memory()[2]
    memory_load_label.config(text=f"{memory_usage}%", fg=get_color(int(memory_usage)))

    cpu_label.after(1000, get_resource_usage)


root = Tk()
root.geometry("+700+300")
root.title("Resource Usage")
root.resizable(0,0)

cpu_label = Label(root, text="CPU", font="Trajan 15")
cpu_label.grid(row=0, column=0, padx=30, pady=[10, 0])

cpu_load_label = Label(root, text="0.0%", font="Trajan 18 bold")
cpu_load_label.grid(row=1, column=0, pady=[0, 10])

memory_label = Label(root, text="RAM", font=("Trajan 15"))
memory_label.grid(row=0, column=1, padx=30, pady=[10, 0])

memory_load_label = Label(root, text="0.0%", font=("Trajan 18 bold"))
memory_load_label.grid(row=1, column=1, pady=[0, 10])

get_resource_usage()

root.mainloop()

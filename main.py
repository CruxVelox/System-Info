import tkinter as tk
from tkinter import Menu

# root window
root = tk.Tk()
root.geometry("240x330")
root.title('System Details')

import platform
#Intro
intro = "---------- System Info ----------"
# Architecture
a = "Architecture: " + platform.architecture()[0]
print(a)

# machine
b = "Machine: " + platform.machine()
print(b)

	# node
c = "Node: " + platform.node()
print(c)

	# processor
with open("/proc/cpuinfo", "r")  as f:
	info = f.readlines()

cpuinfo = [x.strip().split(":")[1] for x in info if "model name"  in x]
for index, item in enumerate(cpuinfo):
	d = "    " + str(index) + ": " + item
	print("Processor:\n")
	print(d)

# system

e = "System OS: " + platform.system()
print(e)


# Load
with open("/proc/loadavg", "r") as f:
	g = "Average Load: " + f.read().strip()
	print(g)

# Memory
print("Memory Info: ")
with open("/proc/meminfo", "r") as f:
	lines = f.readlines()
h = "     " + lines[0].strip()
h1 = "     " + lines[1].strip()
print(h)
print(h1)

# uptime
uptime = None
with open("/proc/uptime", "r") as f:
	uptime = f.read().split(" ")[0].strip()
	uptime = int(float(uptime))
	uptime_hours = uptime // 3600
	uptime_minutes = (uptime % 3600) // 60
i = "Uptime: " + str(uptime_hours) + ":" + str(uptime_minutes) + " hours"
print(i)
def exportinfo():
	#Intro
	intro = "---------- System Info ----------"
	# Architecture
	a = "Architecture: " + platform.architecture()[0]
	print(a)

	# machine
	b = "Machine: " + platform.machine()
	print(b)

	# node
	c = "Node: " + platform.node()
	print(c)

	# processor
	with open("/proc/cpuinfo", "r")  as f:
		info = f.readlines()

	cpuinfo = [x.strip().split(":")[1] for x in info if "model name"  in x]
	for index, item in enumerate(cpuinfo):
		d = "    " + str(index) + ": " + item
		print("Processor:\n")
		print(d)

	# system

	e = "System OS: " + platform.system()
	print(e)


	# Load
	with open("/proc/loadavg", "r") as f:
		g = "Average Load: " + f.read().strip()
		print(g)

	# Memory
	print("Memory Info: ")
	with open("/proc/meminfo", "r") as f:
		lines = f.readlines()
	h = "     " + lines[0].strip()
	h1 = "     " + lines[1].strip()
	print(h)
	print(h1)

	# uptime
	uptime = None
	with open("/proc/uptime", "r") as f:
		uptime = f.read().split(" ")[0].strip()
		uptime = int(float(uptime))
		uptime_hours = uptime // 3600
		uptime_minutes = (uptime % 3600) // 60
	i = "Uptime: " + str(uptime_hours) + ":" + str(uptime_minutes) + " hours"
	print(i)
	lines = [intro, a,"\n", b, "\n", c, "\n", d, "\n", e, "\n", g, "\n", h, "\n", h1, "\n", i]
	with open('SystemSpecs.txt', 'w') as f:
		f.writelines(lines)
	#notification from when it ends exporting the file
	from plyer import notification
	notification.notify(
		title = "Success",
		message = "Your system details were saved\nsuccessfully in the file. (SysDetails.txt)",
		app_icon = 'info.ico',
		timeout = 3,
)
#Copy All Function
def copytoclipboard():
	tocopy = (intro + a + "\n" + b + "\n" + c + "\n" + d + "\n" + e + "\n" + g + "\n" + h + "\n" + h1 + "\n" + i)
	import pyperclip as pc
	pc.copy(tocopy)

# create a menubar
menubar = Menu(root)
root.config(menu=menubar)

# create a menu
file_menu = Menu(menubar)

# add a menu item to the menu
file_menu.add_command(
    label='Exit',
    command=root.destroy
)

# add a menu item to the menu
file_menu.add_command(
    label='Copy All',
    command=copytoclipboard
)

# add a menu item to the menubar
file_menu.add_command(
    label='Export',
    command=exportinfo
)


# add the File menu to the menubar
menubar.add_cascade(
    label="File",
    menu=file_menu
)
# add the Edit menu to the menubar
menubar.add_cascade(
    label="Edit",
    menu=file_menu
)
#add title and architecture
#intro
title = tk.Label(
	root,
	text="System Specs",
	font=("Roboto", "12", "bold"),
	bg="#282828",
	fg="#CACACA"
)
#packing everything
title.pack(fill=tk.X, ipady=10)
root.mainloop()

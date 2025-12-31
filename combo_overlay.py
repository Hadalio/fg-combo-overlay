import tkinter as tk
import re

# Store your combos in a clean list format here. These are some example Terry combos from SF6.
COMBO_LIST = [
    "PC DR 2HP > 236HP, 2HP xx 236PP, 5MP > DR 2HP > 236HK > 236HP, 236MK, 214214P(PP)",
    "2MK > DR 2HP > 236HK dl.> 214HK, 214LP",
    "DI, 5HP xx 236HK > 214HK, 623HP"
]

root = tk.Tk()
root.overrideredirect(True)
root.attributes("-topmost", True)
root.attributes("-alpha", 0.85)

# Here is where you can adjust how the combo list looks. I would suggest changing the font size first before anything.
BG = "black"
font = ("Arial", 15, "bold")
LINE_SPACING = 30 # Distance between each combo line

def seg_color(seg):
    s = seg.upper()
    if "H" in s: return "red"
    if "M" in s: return "yellow"
    if "L" in s: return "cyan"
    if "PP" in s or "KK" in s: return "magenta"
    return "lightgray"

canvas = tk.Canvas(root, bg=BG, highlightthickness=0, bd=0)
canvas.pack()

drc_green = "forest green" 
current_y = 0 # Track vertical position

# --- MAIN DRAWING LOOP ---
for combo in COMBO_LIST:
    current_x = 0
    parts = re.split(r"(xx|[>,])", combo)

    for p in parts:
        if p in [">", ",", "xx"]:
            display_text = f" {p} " if p == "xx" else p
            tid = canvas.create_text(current_x, current_y, text=display_text, font=font, fill="white", anchor="nw")
            current_x = canvas.bbox(tid)[2]
            continue

        # Skip empty strings that can result from re.split
        if not p.strip():
            continue

        current_color = seg_color(p)
        up = p.upper()
        i = 0
        
        while i < len(p):
            # Special case: DRC~
            if up.startswith("DRC~", i):
                text_segment = p[i:i+4] 
                tid = canvas.create_text(current_x, current_y, text=text_segment, font=font, fill=drc_green, anchor="nw")
                current_x = canvas.bbox(tid)[2]
                i += 4 
            # Special case: PC
            elif up.startswith("PC", i):
                tid = canvas.create_text(current_x, current_y, text="PC", font=font, fill="white", anchor="nw")
                current_x = canvas.bbox(tid)[2]
                i += 2
            # Default character
            else:
                tid = canvas.create_text(current_x, current_y, text=p[i], font=font, fill=current_color, anchor="nw")
                current_x = canvas.bbox(tid)[2]
                i += 1
    
    # After finishing one combo string, move down for the next one
    current_y += LINE_SPACING

# --- WINDOW AUTO-RESIZE ---
canvas.update_idletasks()
bbox = canvas.bbox("all")
width = (bbox[2] - bbox[0]) + 10
height = (bbox[3] - bbox[1]) + 10

canvas.config(width=width, height=height)
root.geometry(f"{width}x{height}+100+100")

# Drag-to-move logic
def start_drag(e):
    root._x, root._y = e.x, e.y
def do_drag(e):
    root.geometry(f"+{e.x_root-root._x}+{e.y_root-root._y}")

canvas.bind("<Button-1>", start_drag)
canvas.bind("<B1-Motion>", do_drag)

root.mainloop()
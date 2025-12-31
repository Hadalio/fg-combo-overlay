# FG Combo Overlay
This is a lightweight Python overlay for displaying combos in a draggable, transparent window. Combos are automatically color-coded for SF6 based on the inputs you provide.

## Features

- Draggable, always-on-top window
- Transparent background with adjustable opacity
- Automatically formatted combos:
  - Heavy → red
  - Medium → yellow
  - Light → cyan
  - OD (PP/KK) → magenta
  - DRC and PC highlighted
- Easy to customize combo list

## Installation

Ensure you have Python 3.10+ installed. Then, download and run `combo_overlay.py`.

## Usage

- Drag the overlay anywhere on your screen by clicking and holding the left mouse button.
- Edit the `COMBO_LIST` list in `combo_overlay.py` to add your own combos.
- The window automatically resizes to fit all combos.

import pyautogui

# Read screen size.
w, h = pyautogui.size()
print(w, h)

# Display current mouse position
print(pyautogui.displayMousePosition())

# Mouse movement. Params : x : m, y : m, time in seconds : opt
#pyautogui.moveTo(553, 73)

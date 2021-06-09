import pyperclip, time


clipboard = open("clipboard.txt", "w")
print("", file = clipboard)
clipboard.close()

RecentValue = ""
while True:
    time.sleep(0.1)
    TempValue = pyperclip.paste()
    if TempValue != RecentValue:
        RecentValue = TempValue
        
        clipboard = open("clipboard.txt", "a")
        print(f"{RecentValue}\n", file = clipboard)
        clipboard.close()
    

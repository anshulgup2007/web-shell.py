import webbrowser

for i in range(0, 10):
    sr_wb = input(">>> ")
    if (sr_wb == "you.tb"):
        webbrowser.open("youtube.com")
    
    elif (sr_wb == "gol"):
        webbrowser.open("google.com")
    
    else:
        webbrowser.open("facebook.com")
        
print(i)
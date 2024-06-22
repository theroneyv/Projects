from datetime import datetime

now = datetime.now()
time = now.strftime("%I:%M %P")
date = now.strftime("%m/%d/%Y")

hour = now.hour
great = ""

if hour < 12:
    great = "Good morning"
elif hour < 19:
    great = "Good afternoon"
else:
    great = "Good evening"

print("\033[1;32m    ~   \033[0m" + time)
print("\033[1;32m  C|_|  \033[0m" + date)
print("\033[1;32m   ---  \033[0m" + great + ", take a coffee!" + "\n")
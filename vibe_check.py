import datetime

now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("log.txt", "a") as f:
    f.write(f"Vibe check passed at: {now}\n")

print(f"Successfully logged the vibe at {now}")

# reminder_bot.py

import datetime

def write_reminder():
    today = datetime.date.today().isoformat()
    message = f"{today} - Reminder:\n- ✅ Do 1 Leetcode problem\n- ✅ Work on your project\n"

    with open("reminder_log.md", "a") as f:
        f.write(message + "\n")

if __name__ == "__main__":
    write_reminder()

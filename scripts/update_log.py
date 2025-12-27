#!/usr/bin/env python3
import os
from datetime import datetime

LOG_PATH = "progress/daily-log.md"

def ensure_log_file():
    if not os.path.exists("progress"):
        os.makedirs("progress")

    if not os.path.exists(LOG_PATH):
        with open(LOG_PATH, "w", encoding="utf-8") as f:
            f.write("# Daily Progress Log\n\n")

def add_entry():
    # 🔑 Use UTC to match GitHub Actions cron schedule
    today = datetime.utcnow()
    date_str = today.strftime("%Y-%m-%d (%A)")

    ensure_log_file()

    with open(LOG_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # Prevent duplicate entries
    if f"### {date_str}" in content:
        print("Entry already exists for today.")
        return

    new_entry = f"### {date_str}\n_No updates yet_\n\n"

    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(new_entry)

    print("Added new entry:", date_str)

if __name__ == "__main__":
    add_entry()

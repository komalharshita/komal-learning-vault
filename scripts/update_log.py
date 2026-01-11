#!/usr/bin/env python3
import os
from datetime import datetime

LOG_DIR = "progress"
LOG_PATH = os.path.join(LOG_DIR, "daily-log.md")

def ensure_log_file():
    # Safe directory creation
    os.makedirs(LOG_DIR, exist_ok=True)

    if not os.path.exists(LOG_PATH):
        with open(LOG_PATH, "w", encoding="utf-8") as f:
            f.write("# Daily Progress Log\n\n")

def add_entry():
    # Use UTC to match GitHub Actions cron
    today = datetime.utcnow()
    date_str = today.strftime("%Y-%m-%d (%A)")
    timestamp = today.strftime("%H:%M UTC")

    ensure_log_file()

    with open(LOG_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    header = f"### {date_str}"

    if header in content:
        # 🔑 Force a deterministic daily update (ensures commit)
        updated_content = content.rstrip() + f"\n\n_Last checked: {timestamp}_\n"
        with open(LOG_PATH, "w", encoding="utf-8") as f:
            f.write(updated_content + "\n")
        print("Updated timestamp for existing entry:", date_str)
        return

    # New daily entry
    new_entry = (
        f"{header}\n"
        f"_No updates yet._\n"
        f"_Created at: {timestamp}_\n\n"
    )

    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(new_entry)

    print("Added new entry:", date_str)

if __name__ == "__main__":
    add_entry()

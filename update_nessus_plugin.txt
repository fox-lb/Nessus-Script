#!/bin/bash

# Path to the log file
LOGFILE="/var/log/nessus_plugin_update.log"

# Print start timestamp
echo "=== [$(date '+%Y-%m-%d %H:%M:%S')] === Starting Nessus plugin update..." >> "$LOGFILE"

# Execute the Python update script and append output to log => CHANGE THE PATH
/usr/bin/python3 /home/khanhlb/Download/update_nessus_plugin.py >> "$LOGFILE" 2>&1

# Print end timestamp
echo "=== [$(date '+%Y-%m-%d %H:%M:%S')] === Ended Nessus plugin update..." >> "$LOGFILE"

# Add newline for readability
echo "" >> "$LOGFILE"
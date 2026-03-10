#!/bin/bash
# sync_to_vault.sh — Pull latest notes from GitHub and copy into Obsidian vault
#
# Designed to run via launchd on wake/login. Lightweight: just git pull + rsync.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
NOTES_DIR="$SCRIPT_DIR/notes"
VAULT_DIR="/Users/kushan/dev/Obsidian Vaults/Kush-Personal-Sync/03 🎯 PM Craft/Reading Notes"

LOG_FILE="$SCRIPT_DIR/logs/sync.log"
mkdir -p "$SCRIPT_DIR/logs"

log() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') [INFO] $*" >> "$LOG_FILE"
}

log "Starting sync"

# Pull latest from GitHub
cd "$SCRIPT_DIR"
git pull --ff-only >> "$LOG_FILE" 2>&1 || {
    log "git pull failed — may need manual intervention"
    exit 1
}

# If no notes directory yet, nothing to sync
if [ ! -d "$NOTES_DIR" ]; then
    log "No notes/ directory yet — nothing to sync"
    exit 0
fi

# Rsync notes into the Obsidian vault
# -a: archive mode (recursive, preserves timestamps)
# --ignore-existing: don't overwrite notes already in the vault
rsync -a --ignore-existing "$NOTES_DIR/" "$VAULT_DIR/" >> "$LOG_FILE" 2>&1

log "Sync complete"

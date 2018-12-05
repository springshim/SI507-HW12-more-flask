
import json

GUESTBOOK_ENTRIES_FILE = "entries.json"

f = open(GUESTBOOK_ENTRIES_FILE)
entries = json.loads(f.read())

res = len(entries)
print(res)
# 🐧 Week 1 Linux Cheat Sheet
## CloudOps · Month 1 · Week 1

---

## Navigation
| Command | What it does |
|---|---|
| `pwd` | Shows where you are right now |
| `cd foldername` | Move into a folder |
| `cd ..` | Go back one level |
| `cd ~` | Go straight home |

## Files & Folders
| Command | What it does |
|---|---|
| `mkdir foldername` | Create a folder |
| `mkdir -p a/b/c` | Create folders all at once |
| `touch file.txt` | Create an empty file |
| `ls` | List files in current folder |
| `ls -la` | List files + permissions |
| `rm file.txt` | Delete a file 🗑️ |

## Permissions
| Command | What it does |
|---|---|
| `chmod 600 file` | Only you can read+write 🔒 |
| `chmod 644 file` | You write, others read 📄 |
| `chmod 755 file` | Everyone can execute ▶️ |
| `chmod 400 file` | AWS .pem key protection 🗝️ |

## The Points System
r = 4 · w = 2 · x = 1 · add them up = chmod number
# 🐧 Linux Cheatsheet — Month 1

## Week 1: Navigation & Files
| Command | Example | What it does |
|---|---|---|
| `pwd` | `pwd` | Shows current folder location |
| `ls` | `ls -la` | Lists files (with `-la` shows hidden files + details) |
| `cd` | `cd Documents` | Moves into a folder |
| `mkdir` | `mkdir new_folder` | Creates a new folder |
| `touch` | `touch notes.txt` | Creates an empty file |
| `rm` | `rm file.txt` | Deletes a file |
| `cp` | `cp file.txt backup.txt` | Copies a file |
| `mv` | `mv old.txt new.txt` | Moves or renames a file |
## Week 2: Permissions, Users & SSH
| Command | Example | What it does |
|---|---|---|
| `chmod` | `chmod 755 script.sh` | Changes who can read/write/run a file |
| `chmod 400` | `chmod 400 key.pem` | Locks a file so only YOU can read it (no write, no execute) — required for SSH keys |
| `chown` | `chown user file.txt` | Changes who owns a file |
| `whoami` | `whoami` | Tells you which user you're logged in as |
| `id` | `id` | Shows your user ID and group memberships |
| `sudo` | `sudo apt install git` | Temporarily act as the "admin" (root) to run one command |
| `su` | `su username` | Switches you to another user account |
| `adduser` | `sudo adduser newuser` | Creates a new user account |
| `ssh-keygen` | `ssh-keygen -t rsa -b 4096` | Generates a public/private key pair for secure login |
| `ssh` | `ssh -i key.pem ubuntu@1.2.3.4` | Connects securely to a remote server using a key |
## Week 3: Processes, Search & Pipes
| Command | Example | What it does |
|---|---|---|
| `ps aux` | `ps aux` | Lists all currently running programs (processes) |
| `top` | `top` | Shows live, updating view of CPU/memory usage per process |
| `htop` | `htop` | Like `top` but prettier and easier to read |
| `kill` | `kill 1234` | Stops a process using its ID number (PID) |
| `killall` | `killall python3` | Stops all processes with a matching name |
| `grep` | `grep "error" file.log` | Searches for a word/pattern inside a file |
| `grep -r` | `grep -r "TODO" ./project` | Searches for a word inside ALL files in a folder |
| `find` | `find . -name "*.log"` | Finds files by name pattern |
| `find -mtime` | `find . -mtime -1` | Finds files changed in the last 1 day |
| `\|` (pipe) | `ps aux \| grep python` | Sends the output of one command INTO another command |
| `>` | `ls > files.txt` | Saves command output into a file (overwrites it) |
| `>>` | `ls >> files.txt` | Adds command output to the END of a file (doesn't erase) |
| `2>&1` | `command > out.txt 2>&1` | Also captures error messages into the same file |
## Week 4: Shell Scripts + Vim + Git
| Command | Example | What it does |
|---|---|---|
| `#!/bin/bash` | (first line of script) | The "shebang" — tells the computer this file is a bash script |
| `chmod +x` | `chmod +x hello.sh` | Makes a script file "runnable" |
| `./script.sh` | `./hello.sh` | Runs a script sitting in the current folder |
| `if / else` | `if [ -f file.txt ]; then echo "exists"; fi` | Checks a condition inside a script |
| `for loop` | `for i in 1 2 3; do echo $i; done` | Repeats an action for each item in a list |
| `vim file` | `vim notes.txt` | Opens a file inside the Vim text editor |
| `i` | (inside vim) | Switches Vim into "Insert mode" so you can type |
| `Esc` | (inside vim) | Exits Insert mode, back to "Command mode" |
| `:w` | (inside vim) | Saves the file |
| `:q` | (inside vim) | Quits Vim |
| `/word` | (inside vim) | Searches for "word" inside the file |
| `dd` | (inside vim) | Deletes the current line |
| `git init` | `git init` | Turns a folder into a Git-tracked project |
| `git add` | `git add .` | Stages all changed files, ready to be saved (committed) |
| `git commit -m` | `git commit -m "message"` | Saves a snapshot of your staged changes |
| `git push` | `git push` | Uploads your commits to GitHub |
| `git pull` | `git pull` | Downloads new changes from GitHub |
| `git status` | `git status` | Shows what's changed / staged / not staged |
| `git log --oneline` | `git log --oneline` | Shows a short history of all commits |
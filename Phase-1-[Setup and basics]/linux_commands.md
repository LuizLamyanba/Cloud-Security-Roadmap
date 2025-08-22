# Phase 1 – Linux Commands (Cloud Security Foundation)

This phase focuses on learning **Linux command fundamentals**, which are essential for cloud security engineering.  
Most cloud servers and DevOps environments run on **Linux-based systems**, so mastering these commands is critical for managing, securing, and troubleshooting infrastructure.  

---

## 📚 What I Learned  

### 1. File & Directory Management  
- `ls` – list directory contents (`ls -l` shows details).  
- `cd` – change directory (`cd /home/user`).  
- `mkdir` – create a new directory (`mkdir projects`).  
- `cat` – display file contents (`cat file.txt`).  

### 2. Help & Documentation  
- `man` – open manual for a command (`man ls`).  
- `alias` – create shortcuts (`alias ll='ls -l'`).  

### 3. File Search & Navigation  
- `locate` – find files by name (`locate hello.txt`).  
- `find` – search files in directories (`find /home -name file.txt`).  
- `-maxdepth` – limit search depth (`find / -maxdepth 2 -name file.txt`).  

### 4. File Permissions & Security  
- `chmod` – change file permissions (`chmod 755 script.sh`).  
- **Security context**: Proper permissions are key to preventing unauthorized access on cloud servers.  

### 5. Text Processing & Editing  
- `grep` – search text with patterns (`grep 'hello' file.txt`).  
- **Regex** – use regular expressions for advanced search (`grep '[0-9]' file.txt`).  
- `tr` – translate/replace characters (`echo 'hi' | tr i o`).  
- `diff` – compare files line by line (`diff file1 file2`).  
- `sed` – stream editor for text manipulation (`sed 's/old/new/g' file.txt`).  

### 6. System & Process Management  
- `top` – monitor processes and resource usage.  
- `ps` – show running processes (`ps aux`).  
- `systemctl` – control system services (`systemctl status ssh`).  
- `cron` – schedule recurring tasks (`crontab -e`).  

### 7. Networking & Downloads  
- `wget` – download files from the internet (`wget http://example.com/file.txt`).  
- **Cloud Security use case**: Always prefer HTTPS to ensure secure package retrieval.  

---

## 📂 Resources & References  

- [Linux Journey](https://linuxjourney.com/)  
  ![Linux Journey Snippet](https://github.com/LuizLamyanba/Cloud-Security-Roadmap/blob/main/Phase-1-%5BSetup%20and%20basics%5D/Assets_linux_commands/overthe%20jouney.png)  
  *One of the best free resources to start learning Linux. The site is structured into stages (Grasshopper, Journeyman, etc.) which gradually increase depth.  
  I often revisit this site when I have doubts — the theory is simple, clear, and practical. Highly recommended for anyone starting out.*  

- [OverTheWire Bandit](https://overthewire.org/wargames/bandit/)  
  *A popular wargame (CTF-style challenge) that teaches Linux, command-line basics, and security fundamentals through hands-on practice.  
  I plan to complete at least the first 15 levels in this phase and progress further in the next. Bandit really tests your problem-solving skills and makes Linux learning practical.*  

- [ChatGPT](https://chatgpt.com/)  
  *I used ChatGPT as a study companion to break down complex Linux concepts and generate structured notes for revision.*  

---

## 📺 YouTube Video Guides  

#### 1️⃣ [Introduction to Linux & Terminal Commands – Kunal Kushwaha](https://youtu.be/iwolPf6kN-k?si=eXgN-zaC9k4DpTr5)  
![Kunal Kushwaha Linux Screenshot](https://github.com/LuizLamyanba/Cloud-Security-Roadmap/blob/main/Phase-1-%5BSetup%20and%20basics%5D/Assets_linux_commands/kunal%20kushwaha%20ss.png)  

*This video by Kunal Kushwaha simplified the core Linux commands and their practical use cases.  
The clarity in his teaching style helped me understand **how commands actually work under the hood**, not just memorize them.  
A highly recommended introduction for both beginners and international learners.*  

---

## 📄 Notes  

#### 📝 Personal Notes  
![Linux Handwritten Notes](https://github.com/LuizLamyanba/Cloud-Security-Roadmap/blob/main/Phase-1-%5BSetup%20and%20basics%5D/Assets_linux_commands/LINUX%20NOTES.pdf)  
*My handwritten notes created while studying Linux fundamentals via Linux Journey and YouTube tutorials.  
These notes are my quick reference guide whenever I forget a command.  
My advice: **make your own notes** — writing them helps build long-term memory.*  

---

##  Linux Cheat Sheet  

#### 📊 Linux Command Overview  
![Linux Cheat Sheet PDF](https://github.com/LuizLamyanba/Cloud-Security-Roadmap/blob/main/Phase-1-%5BSetup%20and%20basics%5D/Assets_linux_commands/Linux_Commands_CheatSheet.pdf)  
*A summarized cheat sheet of all Linux commands I practiced, compiled during my ChatGPT study sessions.  
This makes revision quick and structured.*  

---

## 🔐 Cloud Security Mapping (Linux → Security)  

| **Command/Concept** | **Security Relevance** |
|----------------------|-------------------------|
| `chmod` | Prevents unauthorized access by enforcing least privilege. |
| `ps` / `top` | Helps detect malicious/suspicious processes. |
| `systemctl` | Allows control of services (disabling unused ones reduces attack surface). |
| `cron` | Attackers often abuse cron jobs for persistence; auditing them is critical. |
| `grep`, `find` | Useful in incident response to quickly locate indicators of compromise. |
| `wget` | Must be used carefully; insecure downloads can introduce malware. |

---

## 💡 Tips & Tricks I Learned  
- Always check file permissions (`ls -l`) before executing scripts.  
- Combine `grep` with `less` to efficiently search large log files (incident response).  
- Use `ps aux | grep <process>` to hunt for suspicious background tasks.  
- Regularly audit `crontab -l` for unauthorized scheduled jobs.  
- Use `history | grep <command>` to track command usage during investigations.  
- Keep unnecessary services disabled with `systemctl disable <service>`.  
- Always use SSH with key-based login — never rely on root password login.  
- Alias frequently used long commands (e.g., `alias ll='ls -l'`) to save time in daily tasks.  
- Redirect outputs with `>` and `>>` for logging during troubleshooting.  

---

## ✅ Summary  
Linux is the **backbone of cloud servers**.  
In this phase, I learned fundamental commands that every cloud security engineer must master — from **file permissions** to **process monitoring** and **log analysis**.  
This knowledge equips me to securely manage cloud systems, detect anomalies, and minimize attack surfaces in production environments. 

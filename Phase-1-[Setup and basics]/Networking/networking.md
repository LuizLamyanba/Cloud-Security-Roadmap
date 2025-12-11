# Phase 1 – Networking (Cloud Security Foundation)

This phase is about building a **solid networking foundation** with a focus on **cloud security engineering**.  
Networking is the backbone of all cloud systems, and security relies heavily on understanding **how data flows, which protocols are used, and where vulnerabilities exist**.  

---

## 📚 What I Learned  

### 1. Networking Fundamentals  
- **OSI Model (7 layers)** – crucial for mapping security tools like firewalls (Layer 3/4), TLS encryption (Layer 6), and WAFs (Layer 7).  
- **TCP/IP Model (4 layers)** – simplified model widely used in real-world networking and the cloud.  
- **Client-Server vs Peer-to-Peer** – helps understand how cloud services communicate and why centralized client-server models dominate cloud.  
- **IP Addressing & Subnetting** – essential for designing secure **VPCs (Virtual Private Clouds)** in AWS/Azure.  
- **MAC Addresses & ARP** – learned their importance and how attacks like **ARP spoofing** can compromise networks.  

### 2. Security-Relevant Protocols  
- **TCP** – reliable, ordered delivery. Basis for secure protocols (HTTPS, SSH).  
- **UDP** – faster but unreliable, exploited in **DDoS amplification attacks**.  
- **HTTP/HTTPS** – stateless web protocol, with HTTPS securing traffic via TLS encryption.  
- **DNS** – critical but vulnerable to **spoofing and poisoning**.  
- **DHCP** – simplifies IP assignment, but rogue DHCP servers can cause attacks.  
- **ICMP** – useful for troubleshooting but often abused for reconnaissance.  

### 3. Ports & Services  
- **Well-known ports** (0–1023) are the most attacked. Key examples:  
  - `80` → HTTP  
  - `443` → HTTPS (encrypted)  
  - `25` → SMTP (email)  
  - `53` → DNS  
- In the cloud, these are **controlled with firewalls and security groups**.  

### 4. Practical Commands for Security Engineers  
- `ping`, `traceroute` → connectivity & routing checks.  
- `ipconfig` / `ifconfig` → verify network configs in **incident response**.  
- `netstat` → check for suspicious open ports/connections.  
- `nslookup` / `dig` → detect DNS misconfigurations/spoofing.  
- `curl` / `wget` → test APIs, TLS configs, and HTTP responses.  

### 5. Tools & Security Use Cases  
- **Wireshark** – deep packet inspection to detect anomalies, malware traffic, or intrusions.  
- **Nmap** – scans systems for open ports/services, revealing potential attack surfaces.  
- **SSH vs Telnet** – shows the difference between secure (encrypted SSH) and insecure (plain text Telnet) remote logins.  
- **Firewalls & Security Groups** – enforce **least privilege** at the network layer in both on-prem and cloud.  

---

## 📂 Resources & References  

- [ChatGPT](https://chatgpt.com/) – helped me with explanations, Q&A, and creating detailed notes.  
- [Cisco Networking Basics](https://www.netacad.com/courses/networking-basics?courseLang=en-US)  
  *This was a very useful free source to build a clear understanding of networking basics.  
  The course is structured for beginners and explains networking concepts step by step with real-world examples.  
  It helped me strengthen my fundamentals before moving toward **cloud networking and security topics**.*  

---

## 📺 YouTube Video Guides  

#### 1️⃣ [Kunal Kushwaha – Networking Full Course](https://youtu.be/IPvYjXCsTg8?si=KHfpcPtkmaSyjoY6)  
![Kunal Kushwaha Networking Course Screenshot](https://github.com/LuizLamyanba/Cloud-Security-Roadmap/blob/main/Phase-1-%5BSetup%20and%20basics%5D/Networking/Assets_networking/kunal_ss.png)  

*This 4-hour video was my **perfect starting point**.  
I completed it over two days and gained clear insight into how data moves across networks, with a strong explanation of OSI & TCP/IP models.  
Instead of memorizing, I developed **conceptual clarity**.  
Highly recommended for beginners pursuing careers in **cloud, security, or even non-tech fields** (since networking knowledge is universal).*  

---

#### 2️⃣ [OSI and TCP/IP Models – Best Explanation (Drunk Engineer)](https://youtu.be/3b_TAYtzuho?si=8clKAxpnxQGwsAQW)  
![Drunk Engineer TCP/IP Model Screenshot](https://github.com/LuizLamyanba/Cloud-Security-Roadmap/blob/main/Phase-1-%5BSetup%20and%20basics%5D/Networking/Assets_networking/drunkar_ss.png)  

*This short 20-minute video gave me one of the **clearest explanations** of the TCP/IP model.  
It’s concise, visual, and perfect for quickly understanding this critical concept.  
A great companion to longer tutorials and ideal for quick revisions.*  

---

## 📄 Notes  

#### 📝 Handwritten Notes  
![Network Handwritten Notes](https://github.com/LuizLamyanba/Cloud-Security-Roadmap/blob/main/Phase-1-%5BSetup%20and%20basics%5D/Networking/Assets_networking/handwritten_notes_networking.pdf)  
*My personal handwritten notes with diagrams and summaries.  
Useful for quick revision and reinforcing fundamentals.*  

---

#### 📑 Short Notes  
![Network Short Notes](https://github.com/LuizLamyanba/Cloud-Security-Roadmap/blob/main/Phase-1-%5BSetup%20and%20basics%5D/Networking/Assets_networking/Computer_Networking_Notes.docx)  
*Concise summary notes compiled from multiple internet resources.  
They serve as a **cheat sheet** for exam prep and quick lookups.*  

---

#### 📘 ChatGPT Study Notes  
![Networking ChatGPT Full Notes](https://github.com/LuizLamyanba/Cloud-Security-Roadmap/blob/main/Phase-1-%5BSetup%20and%20basics%5D/Networking/Assets_networking/networking%20chat%20gpt%20full%20notes.docx)  
*Detailed notes from my ChatGPT study sessions.  
Covers fundamentals, practical commands, and cloud security mappings in depth.*  

---

## 🖼 Image Notes  

#### 🔗 OSI Model vs TCP/IP Model  
![OSI vs TCP/IP Model](https://github.com/LuizLamyanba/Cloud-Security-Roadmap/blob/main/Phase-1-%5BSetup%20and%20basics%5D/Networking/Assets_networking/OSI%20VS%20TCPIP.png)  
*A comparative diagram that shows how the OSI and TCP/IP models align.  
This helped me map **security tools and vulnerabilities** to the correct layers.*  

---

## 🔐 Cloud Security Mapping (Networking → Security)  

| **Layer/Concept**   | **Security Threats**                        | **Cloud Security Controls** |
|----------------------|---------------------------------------------|-----------------------------|
| **Physical/Data Link** | MAC spoofing, ARP poisoning                 | VLANs, switch port security |
| **Network (IP)**    | IP spoofing, routing attacks                | Security Groups, NACLs, VPC Firewalls |
| **Transport (TCP/UDP)** | Port scanning, SYN flood, UDP flood         | AWS Shield, WAF, rate-limiting |
| **Application (HTTP/DNS)** | XSS, DNS poisoning, SQL injection         | HTTPS/TLS, WAF, DNSSEC, IAM policies |
| **Email (SMTP/IMAP)** | Phishing, spoofing, spam                   | SES security, DMARC, SPF, DKIM |

---

## 💡 Tips & Tricks I Learned  
- Always map issues to the **OSI model** for troubleshooting.  
- Default open ports (22, 80, 443) = common attack surface.  
- DNS is one of the **most targeted services** → monitor & secure with DNSSEC.  
- Use **private subnets** + security groups for least-privilege cloud design.  
- Monitor traffic continuously with tools like **VPC Flow Logs, CloudTrail, Wireshark**.  

---

## ✅ Summary  
Networking is the **first step to mastering cloud security**.  
By learning protocols, commands, and tools, I built the **foundation to secure cloud environments** — from **VPCs to firewalls to encrypted communications**.  
This knowledge is critical as I progress into **cloud security, DevSecOps, and advanced threat defense**.  

# Phase 1 – Networking (Cloud Security Foundation)

This phase is about building a **solid networking foundation** with a focus on **cloud security engineering**.  
Networking is the backbone of all cloud systems, and security relies heavily on understanding **how data flows, which protocols are used, and where vulnerabilities exist**.  

---

## 📚 What I Learned  

### 1. Networking Fundamentals  
- **OSI Model (7 layers)** – crucial for mapping security tools like firewalls (Layer 3/4), TLS encryption (Layer 6), and WAFs (Layer 7).  
- **TCP/IP Model (4 layers)** – simplified model widely used in real-world networking and the cloud.  
- **Client-Server vs Peer-to-Peer** – understanding how cloud services use client-server, and how P2P introduces unique risks.  
- **IP Addressing & Subnetting** – foundation of cloud **VPC (Virtual Private Cloud)** design.  
- **MAC Addresses & ARP** – and their security risks (ARP spoofing attacks).  

### 2. Security-Relevant Protocols  
- **TCP** – reliable, connection-oriented, ensures ordered delivery. Secure services (HTTPS, SSH) rely on it.  
- **UDP** – faster but unreliable, often exploited in **DDoS attacks** (e.g., amplification).  
- **HTTP/HTTPS** – stateless web protocol. HTTPS adds TLS encryption → critical for cloud web security.  
- **DNS** – enables hostname-to-IP mapping. Vulnerable to **DNS spoofing, poisoning, hijacking**.  
- **DHCP** – automates IP assignment, but attackers may run rogue DHCP servers.  
- **ICMP** – used in ping/traceroute, but also reconnaissance and flooding attacks.  

### 3. Ports & Services  
- **Well-known ports** (0–1023) are frequent attack targets. Examples:  
  - `80` – HTTP  
  - `443` – HTTPS (encrypted)  
  - `25` – SMTP (email)  
  - `53` – DNS  
- In cloud, **restricting ports via firewalls/security groups** is a key defense mechanism.  

### 4. Practical Commands for Security Engineers  
- `ping`, `traceroute` – check connectivity & detect routing issues.  
- `ipconfig` / `ifconfig` – network configs during **incident response**.  
- `netstat` – monitor open/suspicious connections.  
- `nslookup` / `dig` – detect DNS misconfigurations or spoofing.  
- `curl` / `wget` – inspect HTTP responses, test TLS, APIs.  

### 5. Tools & Security Use Cases  
- **Wireshark** – packet analysis, intrusion detection, malware traffic analysis.  
- **Nmap** – port scanning, vulnerability detection.  
- **SSH vs Telnet** – secure vs insecure remote login.  
- **Firewalls & Security Groups** – applying least privilege at the network layer.  

---

## 📂 Resources & References  

- [Chat gpt](https://chatgpt.com/)
- [Cisco Networking Basics](https://www.netacad.com/courses/networking-basics?courseLang=en-US)  
  *This was a very useful free source to build a clear understanding of networking basics.  
  The course is structured for beginners and explains networking concepts step by step with real-world examples.  
  It helped me strengthen my fundamentals before moving toward cloud networking and security topics.*  


### 📺 YouTube Video Guides  

#### 1️⃣ [Kunal Kushwaha – Networking Full Course](https://youtu.be/IPvYjXCsTg8?si=KHfpcPtkmaSyjoY6)  
![Kunal Kushwaha Networking Course Screenshot](Phase-1-[Setup and basics]/Assets_networking/kunal_ss.png)  

*This 4-hour video by Kunal Kushwaha was the **perfect starting point** for me.  
I completed it over two days and it helped me clearly understand how data is transferred across networks and how models like OSI & TCP/IP actually work.  
Instead of just memorizing theory, I gained **conceptual clarity** and a practical perspective on networking fundamentals.  
I highly recommend this course to beginners, whether pursuing a **tech or non-tech career**, as networking basics are universally valuable.*  

---

#### 2️⃣ [OSI and TCP/IP Models – Best Explanation (Drunk Engineer)](https://youtu.be/3b_TAYtzuho?si=8clKAxpnxQGwsAQW)  
![Drunk Engineer TCP/IP Model Screenshot](Phase-1-[Setup and basics]/Assets_networking/drunkar_ss.png)  

*I stumbled on this 20-minute video by chance, but it turned out to be one of the **best explanations** I’ve found.  
The **TCP/IP model** is one of the most fundamental topics in networking, and this video explained it in such a simple, visual way that it cleared up many of my doubts instantly.  
It’s short, concise, and highly effective — a great companion to longer, more detailed tutorials.*  
 
---

### 📄 NOTES  
- ![Network Handwritten notes](X:\CLOUD ROADMAP\phase 1\git and git hub\git demo\Phase-1-[Setup and basics]\Assets_networking\NETWORKING HANDWRITTEN NOTES.pdf)  
*handwritten notes by me which i made during my study of networking using the resources hope it will be useful for u*. 
- ![Network short notes](X:\CLOUD ROADMAP\phase 1\git and git hub\git demo\Phase-1-[Setup and basics]\Assets_networking\NETWORKING HANDWRITTEN NOTES.pdf)
*summary of short notes i made and merged during my net surfing and study in internet*
- ![Networking chat gpt full notes](X:\CLOUD ROADMAP\phase 1\git and git hub\git demo\Phase-1-[Setup and basics]\Assets_networking\networking chat gpt full notes.docx)

---

### 🖼 Image Notes  
![OSI model vs TC/IP model](X:\CLOUD ROADMAP\phase 1\git and git hub\git demo\Phase-1-[Setup and basics]\Assets_networking\OSI VS TCPIP.png)  

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
- Map all troubleshooting to the **OSI model**.  
- Default open ports (22, 80, 443) = highest attack surface.  
- DNS is one of the most **exploited services** → always monitor.  
- Use **private subnets** + security groups in cloud deployments.  
- Always check traffic logs (VPC Flow Logs, CloudTrail, Wireshark).  

---

## ✅ Summary  
Networking is the **first step to mastering cloud security**.  
By learning networking protocols, commands, and tools, I built the **foundation to secure cloud environments** — from **VPCs to firewalls to encrypted communications**.  
This knowledge will be critical as I move forward into cloud security, DevSecOps, and advanced threat defense.  

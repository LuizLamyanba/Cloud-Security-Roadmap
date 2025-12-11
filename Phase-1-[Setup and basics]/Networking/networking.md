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
  - 80 → HTTP  
  - 443 → HTTPS (encrypted)  
  - 25 → SMTP  
  - 53 → DNS  
- In the cloud, these are **controlled with firewalls and security groups**.

### 4. Practical Commands for Security Engineers
- `ping`, `traceroute` → connectivity & routing checks  
- `ipconfig` / `ifconfig` → verify network configs in **incident response**  
- `netstat` → check for suspicious open ports  
- `nslookup` / `dig` → detect DNS misconfigurations or spoofing  
- `curl` / `wget` → test APIs, TLS configs, and HTTP responses  

### 5. Tools & Security Use Cases
- **Wireshark** – packet analysis for intrusion detection  
- **Nmap** – scan ports & detect exposed attack surfaces  
- **SSH vs Telnet** – secure vs insecure remote login  
- **Firewalls & Security Groups** – enforce least-privilege access  

---

## 📂 Resources & References

- [ChatGPT](https://chatgpt.com/) – helped with notes, explanations, and breakdowns  
- [Cisco Networking Basics](https://www.netacad.com/courses/networking-basics?courseLang=en-US)  
  *A beginner-friendly course for understanding networking concepts deeply with real-world examples.*

---

## 📺 YouTube Video Guides

### 1️⃣ **Kunal Kushwaha – Networking Full Course**  
https://youtu.be/IPvYjXCsTg8?si=KHfpcPtkmaSyjoY6  
![Kunal Kushwaha Networking Course Screenshot](https://github.com/LuizLamyanba/Cloud-Security-Roadmap/blob/main/Phase-1-%5BSetup%20and%20basics%5D/Assets_networking/kunal_ss.png)

*A very solid start for networking basics, OSI/TCP-IP, routing & packet flow.*

---

### 2️⃣ **OSI & TCP/IP Models – Drunk Engineer**  
https://youtu.be/3b_TAYtzuho?si=8clKAxpnxQGwsAQW  
![Drunk Engineer TCP/IP Model Screenshot](https://github.com/LuizLamyanba/Cloud-Security-Roadmap/blob/main/Phase-1-%5BSetup%20and%20basics%5D/Assets_networking/drunkar_ss.png)

*One of the clearest visual explanations of the networking models.*

---

## 📄 Notes

### 📝 Handwritten Notes  
![Network Handwritten Notes](https://github.com/LuizLamyanba/Cloud-Security-Roadmap/blob/main/Phase-1-%5BSetup%20and%20basics%5D/Assets_networking/NETWORKING%20HANDWRITTEN%20NOTES.pdf)

### 📑 Short Notes  
![Network Short Notes](https://github.com/LuizLamyanba/Cloud-Security-Roadmap/blob/main/Phase-1-%5BSetup%20and%20basics%5D/Assets_networking/Computer_Networking_Notes.docx)



---

## 🖼 Image Notes

### 🔗 OSI Model vs TCP/IP Model  
![OSI vs TCP/IP Model](https://github.com/LuizLamyanba/Cloud-Security-Roadmap/blob/main/Phase-1-%5BSetup%20and%20basics%5D/Assets_networking/OSI%20VS%20TCPIP.png)

*A visual mapping useful for troubleshooting & understanding attack layers.*

---

## 🔐 Cloud Security Mapping (Networking → Security)

| Layer | Security Threats | Cloud Security Controls |
|-------|------------------|--------------------------|
| **Physical/Data Link** | MAC spoofing, ARP poisoning | VLANs, Port Security |
| **Network (IP)** | IP spoofing, routing attacks | NACLs, SGs, VPC Firewalls |
| **Transport (TCP/UDP)** | SYN flood, UDP flood | AWS Shield, Rate Limiting |
| **Application (HTTP/DNS)** | XSS, DNS poisoning | WAF, DNSSEC, IAM |
| **Email (SMTP)** | Phishing, Spoofing | SPF, DKIM, DMARC |

---

## 💡 Tips & Tricks I Learned
- Always troubleshoot using the **OSI model**  
- Default open ports = common attack vectors  
- DNS is one of the most attacked services → secure it  
- Use **private subnets** & strict SGs for cloud design  
- Monitor traffic using **VPC Flow Logs, CloudTrail, Wireshark**

---

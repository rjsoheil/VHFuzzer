
# Host Header Fuzzer

A simple tool for fuzzing virtual hosts on a given IP using the `Host` header and comparing response sizes to detect active virtual hosts.
> Host header fuzzing is a technique used by security researchers to identify hidden assets and vulnerabilities on a web server.
> **That asset (subdomain) may still exist as a `virtual host on the web server`, or may still be set up as a role in the `firewall routing`.**


## Features

- Detects valid virtual hosts on a single IP or a list of IPs
- Uses `httpx` for fast and silent HTTP probing
- Compares `Content-Length` values to identify meaningful responses
- Supports both single and batch mode
- Colorful terminal output using `colorama`

## Requirements

- Python 3.x
- [`httpx`](https://github.com/projectdiscovery/httpx) (must be installed and available in `$PATH`)
- `zsh` (only required if using a `.zshrc`-dependent environment)
- Install required Python packages:

```bash
pip install colorama
```

---

## 🚀 Usage

### ✅ Scan a Single IP
```bash
python main.py --ip 127.0.0.1 --wordlist wordlist.txt
```

### ✅ Scan Multiple IPs
```bash
python main.py --ip-list ip.txt --wordlist wordlist.txt
```

---

## Arguments

| Argument      | Short | Description                                      |
|---------------|-------|--------------------------------------------------|
| `--ip`        | `-i`  | Target IP address (e.g., `127.0.0.1`)            |
| `--ip-list`   | `-il` | Path to a file containing list of IP addresses   |
| `--wordlist`  | `-w`  | Path to wordlist file containing hostnames       |

---

## Example Output

```
Fuzzing on Single IP: 127.0.0.1
[+] A host was Detected: [ site1.local ]
[+] A host was Detected: [ dev.app.local ]

[+] Total hosts found for [127.0.0.1]: 2
```

---

## File Structure

```
.
├── main.py
├── wordlist.txt
├── ip.txt           # Optional: used for scanning multiple IPs
├── README.md
```

---

## Author

Created by: [rjsoheil](https://github.com/rjsoheil)

---

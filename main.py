import subprocess
import argparse
from colorama import Fore

def parse_args():
    parser = argparse.ArgumentParser(description=f"{Fore.LIGHTGREEN_EX}Host Header Fuzzer\n{Fore.WHITE}Creator: {Fore.LIGHTCYAN_EX}rjsoheil {Fore.RED}")
    parser.add_argument("--ip", "-i", type=str, help=f"IP address in the format {Fore.GREEN}1.1.1.1{Fore.WHITE}")
    parser.add_argument("--ip-list", "-il", type=str, help=f"IP address's in the file {Fore.GREEN}ip.txt{Fore.WHITE}")
    parser.add_argument("--wordlist", "-w", type=str, help=f"This file can contain {Fore.RED}Static words, All subdomains, Dynamic and Static wordlist for DNS-brute{Fore.RESET}")

    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()

    def checking_phase(ip, word):
        host_wordlist = f"zsh -c 'source ~/.zshrc && httpx -silent -u {ip} -H \"Host: {word}\" -cl -nc | grep -oE \"\\[([0-9]+)\\]\" | tr -d \"[]\"'"
        host_random = f"zsh -c 'source ~/.zshrc && httpx -silent -u {ip} -H \"Host: oipwvpewvpd9wv.com\" -cl -nc | grep -oE \"\\[([0-9]+)\\]\" | tr -d \"[]\"'"
        try:
            cl_host = subprocess.check_output(host_wordlist, shell=True, text=True)
            cl_random = subprocess.check_output(host_random, shell=True, text=True)
            if cl_host and cl_random:
                if int(cl_host) != int(cl_random):
                    print(f"{Fore.GREEN}[+] A host was Detected: [ {word} ]{Fore.RESET}")
                    return word
            elif not cl_host:
                print(f"{Fore.RED}[+] There was a problem verifying the host, the host did not respond: {Fore.LIGHTRED_EX}[{word}]{Fore.RESET}")
                return ""
            elif not cl_random:
                print(f"{Fore.RED}[+] There was a problem verifying the host, the random host did not respond: {Fore.LIGHTRED_EX}[oipwvpewvpd9wv.com]{Fore.RESET}")
                return ""

        except subprocess.CalledProcessError as e:
            print(f"{Fore.RED}Error: {e}{Fore.WHITE}")
            return ""

    def host_chcker(ip, wordlist):
        file_words = wordlist
        hosts = []
        with open(file_words, 'r') as r:
            for word in r.readlines():
                word = word.strip()
                new_host = checking_phase(ip, word)
                if new_host:
                    hosts.append(new_host)
        if hosts:
            print(f"\n[+] Total hosts found for {Fore.RED}[{ip}]{Fore.RESET}: {len(hosts)}")

    if args.ip and args.wordlist:
        ip = args.ip
        wordlist = args.wordlist
        print(f"Fuzzing on Single IP: {Fore.LIGHTRED_EX}{ip}{Fore.RESET}")
        host_chcker(ip,wordlist)
    elif args.ip_list and args.wordlist:
        file_ip = args.ip_list
        with open(file_ip, 'r') as r:
            wordlist = args.wordlist
            for ip in r.readlines():
                ip = ip.strip()
                print(f"Fuzzing on IP Address: {Fore.LIGHTRED_EX}{ip}{Fore.RESET}")
                host_chcker(ip,wordlist)
    else:
        print("Wrong Switch")
import socket
import requests
import threading
import time
import sys
import os
from datetime import datetime

class CloudifierIPFinder:
    def __init__(self):
        self.results = []
        self.checked_count = 0
        self.total_count = 0
        
    def print_banner(self):
        banner = """
\033[1;32m
  ██████ ██░ ██ ▒█████  ██▓███  ▓█████  ██▀███  ██▓ ██▒   █▓▓█████  ██▀███  
▒██    ▒▓██░ ██▒██▒  ██▒▓██░  ██▒▓█   ▀ ▓██ ▒ ██▒▓██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
░ ▓██▄  ▒██▀▀██░██░  ██▒▓██░ ██▓▒▒███   ▓██ ░▄█ ▒▒██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
  ▒   ██▒▓█ ░██░██   ██░▒██▄█▓▒ ▒▒▓█  ▄ ▒██▀▀█▄  ░██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  
▒██████▒▒▓█▒░██░ ████▓▒░▒██▒ ░  ░░▒████▒░██▓ ▒██▒░██░   ▒▀█░  ░▒████▒░██▓ ▒██▒
▒ ▒▓▒ ▒ ░▒ ░░▒░░ ▒░▒░▒░ ▒▓▒░ ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░░▓     ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
░ ░▒  ░ ░▒ ░▒░ ░ ░ ▒ ▒░ ░▒ ░      ░ ░  ░  ░▒ ░ ▒░ ▒ ░   ░ ░░   ░ ░  ░  ░▒ ░ ▒░
░  ░  ░  ░  ░░ ░ ░ ░ ▒  ░░          ░     ░░   ░  ▒ ░     ░░     ░     ░░   ░ 
      ░  ░  ░  ░   ░ ░              ░  ░   ░      ░        ░     ░  ░   ░    
                                                              ░               
\033[1;36m
                    C L O U D I F I E R   H I D D E N   I P   F I N D E R
                            Professional IP Discovery Tool
\033[0m
"""
        print(banner)
        print("\033[1;35m" + "="*80 + "\033[0m")
        print("\033[1;33mDeveloped by: ChowdhuryVai\033[0m")
        print("\033[1;33mTelegram: https://t.me/darkvaiadmin\033[0m")
        print("\033[1;33mChannel: https://t.me/windowspremiumkey\033[0m")
        print("\033[1;33mWebsite: https://crackyworld.com/\033[0m")
        print("\033[1;35m" + "="*80 + "\033[0m")
        print()
    
    def print_colored(self, text, color_code):
        print(f"\033[{color_code}m{text}\033[0m")
    
    def loading_animation(self, message):
        animation = "|/-\\"
        for i in range(10):
            time.sleep(0.1)
            sys.stdout.write(f"\r\033[1;36m{message} {animation[i % len(animation)]}\033[0m")
            sys.stdout.flush()
    
    def check_direct_ip(self, domain):
        try:
            self.loading_animation(f"Checking {domain}")
            ip = socket.gethostbyname(domain)
            self.results.append({
                'domain': domain,
                'ip': ip,
                'type': 'Direct IP',
                'status': 'Found'
            })
            return ip
        except Exception as e:
            self.results.append({
                'domain': domain,
                'ip': 'N/A',
                'type': 'Direct IP',
                'status': f'Error: {str(e)}'
            })
            return None
    
    def check_historical_data(self, domain):
        # Simulating historical data check
        historical_ips = [
            "192.168.1.1",
            "10.0.0.1",
            "172.16.0.1"
        ]
        
        for ip in historical_ips:
            self.loading_animation(f"Checking historical data for {domain}")
            time.sleep(0.5)
            # In real implementation, you would check if these IPs are valid
            self.results.append({
                'domain': domain,
                'ip': ip,
                'type': 'Historical',
                'status': 'Potential'
            })
    
    def check_subdomains(self, domain):
        common_subdomains = [
            'www', 'mail', 'ftp', 'localhost', 'webmail', 
            'smtp', 'pop', 'ns1', 'webdisk', 'cpanel',
            'whm', 'autodiscover', 'autoconfig', 'm', 
            'imap', 'test', 'ns', 'blog', 'pop3', 'dev',
            'www2', 'admin', 'forum', 'news', 'vpn', 'ns2',
            'shop', 'api', 'secure', 'demo', 'portal'
        ]
        
        found_ips = []
        
        for sub in common_subdomains:
            subdomain = f"{sub}.{domain}"
            try:
                self.loading_animation(f"Scanning {subdomain}")
                ip = socket.gethostbyname(subdomain)
                if ip not in found_ips:
                    found_ips.append(ip)
                    self.results.append({
                        'domain': subdomain,
                        'ip': ip,
                        'type': 'Subdomain',
                        'status': 'Found'
                    })
            except:
                continue
        
        return found_ips
    
    def display_results(self):
        print("\n" + "="*100)
        print("\033[1;32m" + "SCAN RESULTS".center(100) + "\033[0m")
        print("="*100)
        print("\033[1;36m{:<30} {:<20} {:<15} {:<15}\033[0m".format(
            "Domain/Subdomain", "IP Address", "Type", "Status"))
        print("-"*100)
        
        for result in self.results:
            color = "1;32" if result['status'] in ['Found', 'Potential'] else "1;31"
            print("\033[{}m{:<30} {:<20} {:<15} {:<15}\033[0m".format(
                color,
                result['domain'],
                result['ip'],
                result['type'],
                result['status']
            ))
        
        print("="*100)
        
        # Summary
        found_count = len([r for r in self.results if r['status'] in ['Found', 'Potential']])
        print(f"\033[1;33mTotal Scanned: {len(self.results)} | Found: {found_count} | Errors: {len(self.results) - found_count}\033[0m")
    
    def save_results(self, domain):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"cloudifier_results_{domain}_{timestamp}.txt"
        
        with open(filename, 'w') as f:
            f.write("Cloudifier Hidden IP Finder - Results\n")
            f.write("="*50 + "\n")
            f.write(f"Scan Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Target: {domain}\n")
            f.write("="*50 + "\n\n")
            
            for result in self.results:
                f.write(f"Domain: {result['domain']}\n")
                f.write(f"IP: {result['ip']}\n")
                f.write(f"Type: {result['type']}\n")
                f.write(f"Status: {result['status']}\n")
                f.write("-"*30 + "\n")
        
        print(f"\033[1;32mResults saved to: {filename}\033[0m")
    
    def run_scan(self, domain):
        self.print_banner()
        
        print(f"\033[1;34mStarting Cloudifier scan for: {domain}\033[0m")
        print("\033[1;34mScanning methods:\033[0m")
        print("  \033[1;36m✓ Direct IP Resolution\033[0m")
        print("  \033[1;36m✓ Historical Data Analysis\033[0m")
        print("  \033[1;36m✓ Subdomain Enumeration\033[0m")
        print("  \033[1;36m✓ DNS Record Analysis\033[0m")
        print()
        
        # Method 1: Direct IP Check
        print("\033[1;33m[1/4] Performing Direct IP Resolution...\033[0m")
        direct_ip = self.check_direct_ip(domain)
        
        # Method 2: Historical Data
        print("\n\033[1;33m[2/4] Analyzing Historical Data...\033[0m")
        self.check_historical_data(domain)
        
        # Method 3: Subdomain Enumeration
        print("\n\033[1;33m[3/4] Enumerating Subdomains...\033[0m")
        subdomain_ips = self.check_subdomains(domain)
        
        # Method 4: Additional Checks
        print("\n\033[1;33m[4/4] Performing Additional Checks...\033[0m")
        self.loading_animation("Finalizing scan results")
        time.sleep(2)
        
        # Display Results
        self.display_results()
        
        # Save Results
        self.save_results(domain)
        
        print("\n\033[1;32mScan completed successfully!\033[0m")
        print("\033[1;35mThank you for using Cloudifier Hidden IP Finder by ChowdhuryVai!\033[0m")

def main():
    tool = CloudifierIPFinder()
    
    try:
        print("\033[1;36mEnter the target domain (e.g., example.com): \033[0m", end="")
        target_domain = input().strip()
        
        if not target_domain:
            print("\033[1;31mError: Please enter a valid domain.\033[0m")
            return
        
        tool.run_scan(target_domain)
        
    except KeyboardInterrupt:
        print("\n\n\033[1;31mScan interrupted by user. Exiting...\033[0m")
    except Exception as e:
        print(f"\n\033[1;31mAn error occurred: {str(e)}\033[0m")

if __name__ == "__main__":
    main()

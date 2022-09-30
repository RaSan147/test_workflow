import subprocess

def main():
    subprocess.call('wget https://git.io/vpn -O openvpn-install.sh'.split())
    subprocess.call('chmod +x openvpn-install.sh'.split())
    subprocess.call('sudo ./openvpn-install.sh'.split())

if __name__ == '__main__':
    main()
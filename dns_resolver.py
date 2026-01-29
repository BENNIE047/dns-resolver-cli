import socket

def get_ip_address(hostname):
    try:
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except socket.gaierror:
        return None

def clean_input(user_input):
    user_input = user_input.replace("https://", "")
    user_input = user_input.replace("http://", "")
    user_input = user_input.replace("www.", "")
    return user_input.strip()

print(" WEBSITE TO IP ADDRESS RESOLVER")
print("----------------------------------")

website = input("Enter a website name (e.g., google.com): ")
hostname = clean_input(website)

ip = get_ip_address(hostname)

if ip:
    print(f" The IP address of {hostname} is: {ip}")
else:
    print("Could not resolve the website. Please check the name and try again.")

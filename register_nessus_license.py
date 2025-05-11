import requests
import random
import string
import re
from os import system
import platform

print("""
▒█▄░▒█ █▀▀ █▀▀ █▀▀ █░░█ █▀▀ 　 ▒█░▄▀ █▀▀ █░░█ █▀▀▀ █▀▀ █▀▀▄ 
▒█▒█▒█ █▀▀ ▀▀█ ▀▀█ █░░█ ▀▀█ 　 ▒█▀▄░ █▀▀ █▄▄█ █░▀█ █▀▀ █░░█ 
▒█░░▀█ ▀▀▀ ▀▀▀ ▀▀▀ ░▀▀▀ ▀▀▀ 　 ▒█░▒█ ▀▀▀ ▄▄▄█ ▀▀▀▀ ▀▀▀ ▀░░▀""")
print("==== Developed - Harsh Dhamaniya - Consultant ====")

def generate_random_string(length, chars=string.ascii_letters):
    return ''.join(random.choice(chars) for _ in range(length))

def generate_random_phone():
    return ''.join(random.choice(string.digits) for _ in range(10))

def generate_random_company_name():
    return generate_random_string(random.randint(5, 10))

def get_mail():
    company = generate_random_company_name()
    return generate_random_string(15) + "@" + company + random.choice([".com", ".in", ".co", ".org", ".net"])

def generate_nessus_key(app_type):
    random_first_name = generate_random_string(random.randint(5, 10))
    random_last_name = generate_random_string(random.randint(4, 8))
    random_phone = generate_random_phone()
    random_company = generate_random_company_name()
    email = get_mail()

    data = {
        "skipContactLookup": "true",
        "product": app_type,
        "first_name": random_first_name,
        "last_name": random_last_name,
        "email": email,
        "partnerId": "",
        "phone": random_phone,
        "title": "Test",
        "company": random_company,
        "companySize": "10-49",
        "pid": "",
        "utm_source": "",
        "utm_campaign": "",
        "utm_medium": "",
        "utm_content": "",
        "utm_promoter": "",
        "utm_term": "",
        "alert_email": "",
        "_mkto_trk": "",
        "mkt_tok": "",
        "lookbook": "",
        "gclid": "",
        "country": "US",
        "region": "",
        "zip": "",
        "apps": [app_type],  # Set the application type dynamically
        "tempProductInterest": "Tenable Nessus " + ("Expert" if app_type == "expert" else "Professional"),
        "gtm": {"category": "Nessus " + ("Expert" if app_type == "expert" else "Pro") + " Eval"},
        "queryParameters": "",
        "referrer": ""
    }

    url = 'https://www.tenable.com/evaluations/api/v2/trials'
    response = requests.post(url, json=data)

    if response.status_code == 200:
        try:
            # Adjusted regex to correctly extract the activation code
            regex = r"\"code\":\"([A-Z0-9-]+)\""
            matches = re.search(regex, response.text)
            activation_code = matches.group(1)
            print(f"Please use the below mentioned Email for the Registration of Nessus {app_type.capitalize()}")
            print("--------------------------------------")
            print(f"Email: {email}")
            print(f"Nessus {app_type.capitalize()} Activation Code: {activation_code}")
            print("--------------------------------------")
            return activation_code
        except AttributeError:
            print("Failed to retrieve Nessus Activation Code. Response:", response.text)
    else:
        print("Request failed. Status code:", response.status_code)
        print("Response text:", response.text)

def register_nessus(os, key):
    if(os == 1):
        system("/opt/nessus/sbin/nessuscli fetch --register " + key)
        print("Nessus Registered Successfully")
    elif(os == 2):
        system('"C:\\Program Files\\Tenable\\Nessus\\nessuscli.exe" fetch --register ' + key)
        print("Nessus Registered Successfully")
def detect_os():
    system = platform.system().lower()
    if system == 'linux':
        return 1
    elif system == 'windows':
        return 2
    else:
        print(f"Unsupported operating system: {system}")
        exit(1)

def main():
    os_type = detect_os()
    print(f"Detected OS: {'Linux' if os_type == 1 else 'Windows'}")
    
    key = generate_nessus_key("expert")
    register_nessus(os_type, key) 

if __name__ == '__main__':
    main()
from bs4 import BeautifulSoup
import requests
import csv
import os

def scraper():
    URL = "https://cit30900.github.io/strawbridge/"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    root = soup.find(id="root")

    first_name = root.find_all("span", class_="emp_first_name")
    last_name = root.find_all("span", class_="emp_last_name")
    email = root.find_all("span", class_="emp_email")
    ssn = root.find_all("span", class_="secret")

    all_info = []

    for first, last, mail, s in zip(first_name, last_name, email, ssn):
        employee_info = {
            "first_name": first.get_text(strip=True),
            "last_name": last.get_text(strip=True),
            "email": mail.get_text(strip=True),
            "ssn": s.get_text(strip=True)
        }
        all_info.append(employee_info)

    return all_info

def api(all_info):
    risk_levels = []
    low_risk = []
    medium_risk = []
    high_risk = []

    for employee_ssn in all_info:
        ssn = employee_ssn["ssn"]
        try:
            response_API = requests.get(f'https://us-central1-cit-37400-elliott-dev.cloudfunctions.net/have-i-been-pwned?username=ndpumphr&ssn={ssn}')
            response_API.raise_for_status()
        except requests.exceptions.RequestException:
            print(f"SSN {ssn} does not exist")
            risk_level = "Not available"
        else:
            data = response_API.json()
            risk_level = data.get('exposure', 'Not available')

        if risk_level == "low":
            low_risk.append(risk_level)
        elif risk_level == "medium":
            medium_risk.append(risk_level)
        else:
            high_risk.append(risk_level)

        # print(f"SSN {ssn} has a risk level of: {risk_level}")
        risk_levels.append(risk_level)
        
    
    print(f"{len(low_risk)} low risk exposures detected")
    print(f"{len(medium_risk)} medium risk exposures detected")
    print(f"{len(high_risk)} high risk exposures detected")

    return risk_levels

def create_csv(all_info, risk_levels):
    csv_file = "employee_info.csv"

    with open(csv_file, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["first_name", "last_name", "email", "ssn", "risk_level"])

        writer.writeheader()

        for employee_info, risk_level in zip(all_info, risk_levels):
            employee_info["risk_level"] = risk_level
            writer.writerow(employee_info)

def high_exposures(all_info, risk_levels):
    high_risk = []

    for employee_info, risk_level in zip(all_info, risk_levels):
        if risk_level == "high":
            high_risk.append(employee_info)
    
    email_notifications = "high_risk_emails"
    os.makedirs(email_notifications, exist_ok=True)

    for employee in high_risk:
        first_name = employee["first_name"]
        last_name = employee["last_name"]
        email = employee["email"]

        file_path = os.path.join(email_notifications, f"{first_name}_{last_name}.txt")

        with open(file_path, "w") as text_file:
            text_file.write(f"Dear {first_name} {last_name},\n\n")
            text_file.write("Your personal data was accidentally exposed on the Strawbridge Industries website "
                            "and is at risk of being compromised. The company regrets this error and would "
                            "like to offer a credit monitoring service at no cost to you. Please contact HR "
                            "to establish this service.\n\n")
            text_file.write("Thank you,\n\nDick Strawbridge, CE")


def main():
    all_info = scraper()
    risk_levels = api(all_info)
    create_csv(all_info, risk_levels)
    high_exposures(all_info, risk_levels)

if __name__ == "__main__":
    main()
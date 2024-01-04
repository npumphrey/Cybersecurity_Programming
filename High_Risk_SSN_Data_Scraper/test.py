from bs4 import BeautifulSoup
import requests
import csv
import socket

def scraper():
    URL="https://cit30900.github.io/strawbridge/"
    page = requests.get(URL)

    # print(page)

    soup = BeautifulSoup(page.content, "html.parser")
    
    root = soup.find(id="root")

    first_name = root.find_all("span", class_="emp_first_name")
    last_name = root.find_all("span", class_="emp_last_name")
    email = root.find_all("span", class_="emp_email")
    ssn = root.find_all("span", class_="secret")

    # risk_level = 

    print(len(first_name), len(last_name), len(email), len(ssn))

    all_info = []

    for first_name, last_name, email, ssn, in zip(first_name, last_name, email, ssn):
        employee_info = {
            "first_name": first_name.get_text(strip=True),
            "last_name": last_name.get_text(strip=True),
            "email": email.get_text(strip=True),
            "ssn": ssn.get_text(strip=True)
        }
        all_info.append(employee_info)
    
    print(all_info)
    return all_info, ssn

def main():
    scraper()

if __name__ == "__main__":
    main()
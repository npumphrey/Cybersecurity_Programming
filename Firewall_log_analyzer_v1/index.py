from log_analyzer import LogEntry

from csv import DictReader

filename = 'firewall_logs_sample.csv'
logs = []

with open(filename, 'r') as f:
    # Create a DictReader object that will read the contents of the CSV file as dictionaries
    dict_reader = DictReader(f)
    # Create an iterable element that will hold the contents of the CSV file as a list
    # This will result in a LIST OF DICTIONARIES
    list_of_dict = list(dict_reader)
    # Loop through the list and view the contents of the file
    for d in list_of_dict:
        logs.append(d)
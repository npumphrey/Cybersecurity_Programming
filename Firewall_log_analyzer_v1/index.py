from log_analyzer import LogEntry
from csv import DictReader, DictWriter
import argparse
import pytz




def arg_accepter():
    parser = argparse.ArgumentParser(description='Accept CSV file and action')

    parser.add_argument('--CSVfile', '-f', required=True, help='CSV filename')
    parser.add_argument('--action', '-a', required=True, help='actions include `head`, `deny`, `source`, and `parse`')
    parser.add_argument('--country', '-c', required=False, help='2 letter country code for `source` action')
    parser.add_argument('--month', '-m', required=False, help='month for the `parse` action')
    args=parser.parse_args()

    return args

def print_head(logs):
    est_timezone = pytz.timezone("US/Eastern")
    for i in range(5):
        pytz_logs = est_timezone.localize(logs[i].event_time)
        print(f"{pytz_logs}, {logs[i].action}, {logs[i].source_ip}, {logs[i].ipv4_class}, {logs[i].country_name}")


def deny_count(logs):
    denied_list = [i for i in logs if i.action == 'Deny']
    print(f"{len(denied_list)} log entries were denied.")


def country_count(logs, args):
    country_list = [i for i in logs if i.country == args.country]
    print(f"{len(country_list)} log entries from {args.country} were recorded.")


def parse(logs, args):
    month_entries = [i for i in logs if i.event_time.month == int(args.month)]
    # this could also be written as 
    # month_entries = [i for i in logs if i.event_time.strftime("%m") == args.month]
    print(f"{len(month_entries)} log entries from month {args.month}.")
    if args.month and 1 <= int(args.month) <= 12:
                log_filename = f'2022_{args.month}_logs.csv'
                fieldnames = ['event_time', 'internal_ip', 'port_number', 'protocol', 'action', 'rule_id', 'country', 'country_name', 'source_ip']
                with open(log_filename, 'w', newline='') as log_file:
                    writer = DictWriter(log_file, fieldnames=fieldnames)
                    writer.writeheader()
                    for d in month_entries:
                        writer.writerow({'event_time': d.event_time, 'internal_ip': d.internal_ip, 'port_number': d.port_number, 'protocol': d.protocol, 'action': d.action, 'rule_id': d.rule_id, 'country': d.country, 'country_name': d.country_name, 'source_ip': d.source_ip})


def main():
    args = arg_accepter()
    print(args.CSVfile)
    
    logs = []
    with open(args.CSVfile, 'r', encoding="utf8") as f:
        
        dict_reader = DictReader(f)
        # Create an iterable element that will hold the contents of the CSV file as a list
        # This will result in a LIST OF DICTIONARIES
        list_of_dict = list(dict_reader)

        for d in list_of_dict:
            entry = LogEntry(d['event_time'], d['internal_ip'], d['port_number'], d['protocol'], d['action'], d['rule_id'], d['country'], d['country_name'], d['source_ip'])
            logs.append(entry)

        if args.action == 'head':
            print_head(logs)

        if args.action == 'deny':
            deny_count(logs)

        if args.action == 'source':
            country_count(logs, args)

        if args.action == 'parse':
            parse(logs, args)
            



    

if __name__ == '__main__':
    main()
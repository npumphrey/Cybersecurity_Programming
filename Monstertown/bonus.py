from datetime import datetime

def main():

    date_string = "12/15/2024"
    format_string = "%m/%d/%Y"

    datetime_obj = datetime.strptime(date_string, format_string)
    print("Date = ", datetime_obj)



if __name__ == '__main__':
    main()




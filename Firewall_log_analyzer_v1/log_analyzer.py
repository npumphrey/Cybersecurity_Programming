from datetime import datetime
    
class LogEntry():
    
    def __init__(self, event_time, internal_ip, port_number, protocol, action, rule_id, country, country_name, source_ip):
        
        self.event_time = event_time
        et_string = "2022-01-01 00:18:38 UTC"
        format_string = "%Y-%m-%d %H:%M:%S %Z"
        et = datetime.event_time(et_string, format_string)



    @property
    def ipv4_class():

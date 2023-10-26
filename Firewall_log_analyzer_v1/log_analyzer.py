from datetime import datetime
import re
    
class LogEntry():
    
    def __init__(self, event_time, internal_ip, port_number, protocol, action, rule_id, country, country_name, source_ip):
        
        format_string = "%Y-%m-%d %H:%M:%S %Z"
        self.event_time = datetime.strptime(event_time, format_string)
        self.internal_ip = internal_ip
        self.port_number = port_number
        self.protocol = protocol
        self.action = action
        self.rule_id = rule_id
        self.country = country
        self.country_name = country_name
        self.source_ip = source_ip


    @property
    def ipv4_class(self):
        group_octects = int(re.search(r"^(\d{1,3})", self.source_ip)[0])
        # first_octects = int(group_octects.groups())
        if group_octects <= 127:
            return 'A'
        elif group_octects >= 128 and group_octects <= 191:
            return 'B'
        elif group_octects >= 192 and group_octects <= 223:
            return 'C'
        elif group_octects >= 224 and group_octects <= 239:
            return 'D'
        else:
            return 'E'
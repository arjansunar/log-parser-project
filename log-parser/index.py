import re
from collections import Counter


def matcher(line,regex):
    return re.findall(regex,line)

def browser_used(line):
    result= matcher(line,r'"\w{4,}\/[\d.]+;*\s')
    if result: 
        return matcher(result[0], r'\w+')

def client_ip(line):
    return matcher(line, r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')  

def date_time(line):
    result = matcher(line, r'\d+\/\w+\/\d+')
    if result:
        return result  

def os_type(line):
    result = matcher(line, r'\([\w\d\s\.]*;\s[\w]*;\s[\w\s\d]*[;\s]*[\w\d:\.]*\)')
    if result:
        filter=matcher(result[0],r'[A-Za-z]{4,}') 
        if filter: return filter

def count(list):
    return Counter(list)

def getFile():
    log_file= open("access.log")
    return log_file

    
def main ():
    log_file= open("access.log")
    clients=[]
    browsers=[]
    dates=[]
    systems=[]
    for line in log_file:
        ip = client_ip(line)
        browser= browser_used(line)
        date = date_time(line)
        os = os_type(line)
        if ip: clients.append(ip[0])
        if browser: browsers.append(browser[0])
        if date: dates.append(date[0])
        if os: systems.append(os[0])
 
    print(dict(count(clients)))
    print(dict(count(browsers)))
    print(dict(count(dates)))
    print(dict(count(systems)))
    log_file.close()

if __name__ == '__main__':
    main()

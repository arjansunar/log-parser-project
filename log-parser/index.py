import re
from collections import Counter
import json
# import time
import concurrent.futures
import multiprocessing as mp

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

def parse_log(parser):
    file = open("access.log")
    result=[]
    for line in file: 
        res = parser(line)
        if res: result.append(res[0])
    return result

def main ():
    log_file= open("access.log")
    clients=[]
    browsers=[]
    dates=[]
    systems=[]
    # start= time.perf_counter()

    # using multiprocessing    
    with concurrent.futures.ProcessPoolExecutor() as executor: 
        f1=executor.submit(parse_log,client_ip)
        f2=executor.submit(parse_log,browser_used)
        f3=executor.submit(parse_log,date_time)
        f4=executor.submit(parse_log,os_type)
        clients= f1.result()
        browsers= f2.result()
        dates= f3.result()
        systems= f4.result()



    file= open("data/client_ip.json","w")
    file.write(json.dumps(dict(count(clients))))
    file.close()

    file= open("data/client_browser.json","w")
    file.write(json.dumps(dict(count(browsers))))
    file.close()
 
    file= open("data/client_os.json","w")
    file.write(json.dumps(dict(count(systems))))
    file.close()

    file= open("data/client_date.json","w")
    file.write(json.dumps(dict(count(dates))))
    file.close()
  
    log_file.close()

if __name__ == '__main__':
    main()

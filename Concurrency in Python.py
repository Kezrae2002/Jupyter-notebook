13.1:
import datetime 

#Get today's date
today = datetime.date.today()

with open('today.txt', 'w') as file:
    file.write(str(today))


13.2
# Read the contents of today.txt
with open('today.txt', 'r') as file:
    today_string = file.read()

print(today_string)  # optional, just to check

>> 2025-04-28

13.3
# Parse today_string back into a date object
parsed_date = datetime.datetime.strptime(today_string, '%Y-%m-%d').date()

print(parsed_date)  # optional, just to check

>>2025-04-28

15.1
import multiprocessing
import time
import random
from datetime import datetime

def worker():
    # Wait random time between 0 and 1 seconds
    wait_time = random.uniform(0, 1)
    time.sleep(wait_time)
    
    # Print the current time
    print(f'Process {multiprocessing.current_process().name} - Time: {datetime.now()}')

if __name__ == '__main__':
    # Create 3 processes
    processes = []
    for i in range(3):
        p = multiprocessing.Process(target=worker, name=f'Worker-{i+1}')
        processes.append(p)
        p.start()

    # Wait for all processes to finish
    for p in processes:
        p.join()

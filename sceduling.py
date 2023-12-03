
#Adding the available processes to the ready queue
def add_process(ready_queue, arrival_time, name, priority, burst_time):
    ready_queue.append([arrival_time, name, priority, burst_time])


#Executing the processes in the ready queue
def execute_process(ready_queue, time_elapsed, index):
    if not ready_queue:
        return None

    highest_priority_process = min(ready_queue, key=lambda x: x[2])
    arrival_time, name, priority, burst_time = highest_priority_process
    
    output = f"{name} (Priority: {priority})"
        
    print(f"Process Name : {name}, Priority : {priority}, Waiting Time : {time_elapsed - arrival_time}")    

    data_to_write = f"{index + 1}.{name} \n\tWaiting Time : {time_elapsed - arrival_time} mins"

    with open('./output.txt', 'a') as file:
        file.write(data_to_write)
        file.write("\n")
        
    ready_queue.remove(highest_priority_process)

    return burst_time


#Checking for processes that have arrived
def non_preemptive_priority_scheduler(processes):
    
    ready_queue = []
    time_elapsed = 0
    index = 0
    
    processes = sorted(processes)
    
    while processes or ready_queue:
        while processes and processes[0][0] <= time_elapsed:
            process = processes.pop(0)
            add_process(ready_queue, *process)

        burst_time = execute_process(ready_queue, time_elapsed, index)
        
        if not burst_time:
            time_elapsed += 1
        else:
            time_elapsed += burst_time
            
        if burst_time:
            index += 1


#Reading the inputs from the text file
def read_inputs(processes):
    
    with open('./data.txt', 'r') as file:
        data = file.read().split('\n')
    
    
    #Splitting the data and storing it in a variable
    for line in data[:-1]:
        temp = line.split(' ')
        
        temp[0] = int(temp[0])
        temp[2] = int(temp[2])
        temp[3] = int(temp[3])
        
        processes.append(temp)

if __name__ == "__main__":
    

    """
    Sample Input
    
    Input in the order of Arrival Time, Process Name, Priority, Burst Time
    
    processes = [
        [0, "p1", 2, 5],
        [1, "p1", 1, 2],
        [3, "p1", 1, 3],
        [5, "p1", 3, 1],
    ]
    
    """

    processes = []
    
    read_inputs(processes)
    
    non_preemptive_priority_scheduler(processes)

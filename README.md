# Module 2: streaming-02-multiple-processes
## Author: Prabha Sapkota Pokharel
## Github link: https://github.com/prabhasapkota/streaming-02-multiple-processes


## Overview

This example starts a shared database and multiple processes.

The processes represent multiple users, or locations, or programs 
hitting a shared database at the same time. 

## Task 1. Fork 

Fork this repository ("repo") into **your** GitHub account. 

## Task 2. Clone

Clone **your** new GitHub repo down to the Documents folder on your local machine. 

## Task 3. Explore

Explore your new project repo in VS Code on your local machine.

## Task 4. Execute Check Script

Execute 00_check_core.py to generate useful information.

## Task 5. Execute Multiple Processes Project Script

Execute multiple_processes.py.

Read the output. Read the code. 
Try to figure out what's going on. 

1. What libraries did we import?
1. Where do we set the TASK_DURATION_SECONDS?
1. How many functions are defined? 
1. What are the function names? 
1. In general, what does each function do? 
1. Where does the execution begin? Hint: generally at the end of the file.
1. How many processes do we start?
1. How many records does each process insert?

In this first run, we start 3 processes, 
each inserting 2 records into a shared database 
(for a total of 6 records inserted.)

In each case, the process gets a connection to the database, 
and a cursor to execute SQL statements.
It inserts a record, and exits the database quickly.

In general, we're successful and six new records get inserted. 

## Task 6. Execute Multiple Processes Script with Longer Tasks

For the second run, modify the task duration to make each task take 3 seconds. 
Hint: Look for the TODO.
Run the script again. 
With the longer tasks, we now get into trouble - 
one process will have the database open and be working on it - 
then when another process tries to do the same, it can't and 
we end up with errors. 

## Task 7. Document Results After Each Run

To clear the terminal, in the terminal window, type clear and hit enter or return. 

`clear`

To document results, clear the terminal, run the script, and paste all of the terminal contents into the output file.

Use out0.txt to document the first run. 

Use out3.txt to document the second run.


-----
## Task 8. Stream Processing Example
* copy process_streaming_0.py from the Module 1 repo.
* copy the other file you need to make it work. Hint: read the code. Look for the name of another (data) file to read from.

## Task 9. Custom Stream from CSV Script
* Create a new Python script in your repo named process_streaming_yourname.py
* Create a new CSV file in your repo using any data you like.
* Stream from your CSV file into a new file named out9.txt.
* Use the examples provided as the basis for your implementation. 
* Generate one record every 1-3 seconds. Let it run long enough to write ten or more records to out9.txt.

## Task 10. Learn About UDP and TCP
UDP
* UDP stands for User Datagram Protocol, and it is connectionless -  you just send the data without establishing a formal connection. 
* UDP is the easiest - just chunk up the data and send the chunks.
* UDP is somewhat casual - like getting multiple packages shipped from the Amazon warehouse to your porch. 
* UDP doesn’t guarantee delivery, order of the packets, or error checks.

TCP
* TCP (Transmission Control Protocol) is connection-oriented, ensuring data integrity, order, and delivery acknowledgment.
* TCP is used for many of the primary internet functions, including web browsing and email.
* TCP includes a more elaborate set of greeting protocols conducted before transmission begins - much like the bows, courtesies, and/or handshakes often followed when beginning important diplomatic conversations. 
* To learn more about the TCP protocol, see the quiz this module and do a bit of searching.


## Helpful Information

To get more help on the early tasks, see [streaming-01-getting-started](https://github.com/denisecase/streaming-01-getting-started).


### Database Is Locked Error

Do a web search on the sqlite3 'database is locked' error.

- What do you learn?
- Once a process fails, it crashes the main process and everything stops. 

### Deadlock

Deadlock is a special kind of locking issue where a process 
is waiting on a resource or process, that is waiting also. 

Rather than crashing, a system in deadlock may wait indefinitely, 
with no process able to move forward and make progress.

### Learn More

Check out Wikipedia's article on deadlock and other sources to learn how to prevent and avoid locking issues in concurrent processes. 

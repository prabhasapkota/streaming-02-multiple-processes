
# Import from Python Standard Library

import csv
import socket
import time
import random



# Declare program constants (typically constants are named with ALL_CAPS)

HOST = "localhost"
PORT = 9999
ADDRESS_TUPLE = (HOST, PORT)
INPUT_FILE_NAME = "netflix_titles.csv"
OUTPUT_FILE_NAME = "out9.txt"

# Define program functions (bits of reusable code)


def prepare_message_from_row(row):
    return f"{','.join(row)}\n".encode()


def stream_data(input_file_name, output_file_name, address_tuple):
    with open(input_file_name, "r") as input_file, open(output_file_name, "w") as output_file:
        reader = csv.reader(input_file, delimiter=",")
        
        header = next(reader)  # Skip header row
        output_file.write(','.join(header) + '\n')
        
        # Using my Contructor to make a socket obj
        # assigning variable name "sock_object"
        sock_object = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        
        for row in reader:
            message = prepare_message_from_row(row)
            sock_object.sendto(message, address_tuple)
            output_file.write(','.join(row) + '\n')
            time.sleep(random.uniform(1, 3))  # Random sleep between 1-3 seconds

# ---------------------------------------------------------------------------
# If this is the script we are running, then call some functions and execute code!
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    try:
        print("Starting data streaming.")
        stream_data(INPUT_FILE_NAME, OUTPUT_FILE_NAME, ADDRESS_TUPLE)
        print("Streaming complete!")
    except Exception as e:
        print(f"An error occurred: {e}")
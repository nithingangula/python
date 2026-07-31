import threading
import time


def download_files():
    for i in range(1, 6):
        print(f"Downloading file {i}...")
        time.sleep(1)
    print("Download completed!\n")


def upload_files():
    for i in range(1, 6):
        print(f"Uploading file {i}...")
        time.sleep(1)
    print("Upload completed!\n")


def process_data():
    for i in range(1, 6):
        print(f"Processing data {i}...")
        time.sleep(1)
    print("Processing completed!\n")


# Create threads
t1 = threading.Thread(target=download_files)
t2 = threading.Thread(target=upload_files)
t3 = threading.Thread(target=process_data)

# Start threads
t1.start()
t2.start()
t3.start()

# Wait for all threads to finish
t1.join()
t2.join()
t3.join()

print("All tasks completed successfully!")
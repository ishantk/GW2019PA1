import requests
import threading

print(">> App Started")

# Child Thread 1
class FetchNewsTask(threading.Thread):
    # What Child Thread should do will be written in the run function
    def run(self):
        url1 = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=7b950bb5fa384b3bb3b7b9b5d3b350cb"
        print("Fetching Data from URL1")
        response1 = requests.get(url1)
        print(response1.text)

# Child Thread 2
class FetchBooksTask(threading.Thread):
    # What Child Thread should do will be written in the run function
    def run(self):
        url2 = "http://www.json-generator.com/api/json/get/chQLxhBjaW?indent=2"
        print("Fetching Data from URL2")
        response2 = requests.get(url2)
        print(response2.text)

# Create Objects for Threads
newsTask = FetchNewsTask()
booksTask = FetchBooksTask()

# Execution on start will execute run function in thread
newsTask.start()
booksTask.start()

for i in range(1,11):
    print(">> i is:",i)

print(">> App Finished")

# Conclusion
# Create a thread when tasks in main thread are getting blocked !!
# Tasks maximum times will be related to internet connectivity which will take more time
# or reading some large data from system
# no bigger task should be written in the main thread ever
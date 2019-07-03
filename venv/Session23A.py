import threading
import time

# Lock Object
lock = threading.Lock()

class Printer:
    def printDocuments(self, docName, times):

        lock.acquire()

        for i in range(1, times+1):
            print(">> Printing {} Copy#{}".format(docName, i))
            time.sleep(1)

        lock.release()

class Desktop(threading.Thread):

    def attachPrinter(self, printer):
        self.printer = printer

    def run(self):
        self.printer.printDocuments("**LearningPython.pdf**", 10)

class Laptop(threading.Thread):

    def attachPrinter(self, printer):
        self.printer = printer

    def run(self):
        self.printer.printDocuments("##LearningJava.pdf##", 10)

# pRef = Printer()
printer = Printer()
# printer.printDocuments("LearningPython.pdf", 10)

desktop = Desktop()
desktop.attachPrinter(printer)

laptop = Laptop()
laptop.attachPrinter(printer)

desktop.start()
laptop.start()

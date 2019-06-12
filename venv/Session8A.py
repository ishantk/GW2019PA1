class Counter:

    ccount = 1

    def __init__(self):
        self.count = 1
        Counter.ccount = 1

    def incrementCount(self):
        self.count = self.count + 1
        Counter.ccount = Counter.ccount + 1

    def showCount(self):
        print("count is {} and ccount is {}".format(self.count, Counter.ccount))

c1 = Counter()
c2 = Counter()
c3 = c1

c1.incrementCount()
c2.incrementCount()
c3.incrementCount()

c1.incrementCount()
c2.incrementCount()
c3.incrementCount()

c4 = Counter()

c1.showCount()  # count is 5 and ccount 7 7 1
c3.showCount()  # count is 5 and ccount 7 7 1
c2.showCount()  # count is 3 and ccount 7 7 1
c4.showCount()  # count is 1 and ccount 1 7 1

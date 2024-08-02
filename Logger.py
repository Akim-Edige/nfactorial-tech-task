class Logger():
    def __init__(self):
        self.dateBase = {}
        self.currentTime = 0



    def shouldPrintMessage(self,timestamp, message):
        timestamp = int(timestamp)

        self.deleteOldMessages()


        # If there are more than 100 messages, deleting oldest message by timestamp
        if (self.loggerSize()>100):
            oldestMessageKey = min(self.dateBase, key=self.dateBase.get)
            del self.dateBase[oldestMessageKey]


        if (message in self.dateBase):
            if(self.dateBase[message]+10<=timestamp):
                self.dateBase[message] = timestamp

                if (self.currentTime < timestamp):
                    self.currentTime = timestamp
                return True
            else:
                return False
        else:
            if (self.currentTime < timestamp):
                self.currentTime = timestamp

            self.dateBase[message]=timestamp
            return True


    # Deleting all messages that are older than 10 seconds than the current time

    def deleteOldMessages(self):
        toDelete = []
        for key,value in self.dateBase.items():
            if value + 10 <= self.currentTime:
                toDelete.append(key)

        for key in toDelete:
            del self.dateBase[key]


    # Returns size of the messages' queue
    def loggerSize(self):
        return len(self.dateBase)


    # Return Boolean value if there is a message in this particular timestamp
    def clean(self, timestamp):
        timestamp = int(timestamp)

        try:
            key = list(self.dateBase.keys())[list(self.dateBase.values()).index(timestamp)]
        except:
            return True
        else:
            return False

    # Return value of a message if there is a message in this particular timestamp
    def findKeyByValue(self, timestamp):
        timestamp = int(timestamp)
        try:
            key = list(self.dateBase.keys())[list(self.dateBase.values()).index(timestamp)]
        except:
            return ''
        else:
            return key

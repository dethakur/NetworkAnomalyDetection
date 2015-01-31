__author__ = 'devashishthakur'

class IP:
    def __init__(self,ip):
        self.indegree = 0
        self.outdegree = 0
        self.name = ip
        self.connectedIps = []

    def connectIp(self,ip):
        self.connectedIps.append(ip)

    def getIndegree(self):
        return self.indegree

    def getOutdegree(self):
        return self.indegree

    def incrementIndegree(self):
        self.indegree += 1

    def decrementIndegree(self):
        self.indegree -= 1

    def incrementOutdegree(self):
        self.outdegree += 1

    def decrementOutdegree(self):
        self.outdegree -= 1

    def isOneDimension(self):
        return self.indegree == 0 or self.outdegree == 0

    def __str__(self):
        return "{} , Indegree = {} and Outdegree = {}".format(self.name,self.indegree,self.outdegree)


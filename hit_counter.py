# Interesting Friday Challenge for you all this week- an object-oriented challenge:
# Design a hit counter which counts the number of hits received in the past 5 minutes (i.e., the past 300 seconds).
# Your system should accept a timestamp parameter (in seconds), and you may assume that calls are being made to the system 
# in chronological order (i.e., timestamp is monotonically increasing). Several hits may arrive roughly at the same time.
# Implement the HitCounter class:
# HitCounter() Initializes the object of the hit counter system.
# hit(timestamp) Records a hit that happened at timestamp (in seconds). Several hits may happen at the same timestamp.
# getHits(timestamp) Returns the number of hits in the past 5 minutes from timestamp (i.e., the past 300 seconds).
# Example 1:
# Inputs/Calls Made:
# ["HitCounter", "hit", "hit", "hit", "getHits", "hit", "getHits", "getHits"]
# [[], [1], [2], [3], [4], [300], [300], [301]]
# Outputs:
# [null, null, null, null, 3, null, 4, 3]

# Explanation:
# HitCounter hitCounter = new HitCounter();
# hitCounter.hit(1);       // hit at timestamp 1.
# hitCounter.hit(2);       // hit at timestamp 2.
# hitCounter.hit(3);       // hit at timestamp 3.
# hitCounter.getHits(4);   // get hits at timestamp 4, return 3.
# hitCounter.hit(300);     // hit at timestamp 300.
# hitCounter.getHits(300); // get hits at timestamp 300, return 4.
# hitCounter.getHits(301); // get hits at timestamp 301, return 3.
# Skeleton Code:
        
# Constraints:
# 1 <= timestamp <= 2 * 109
# All the calls are being made to the system in chronological order (i.e., timestamp is monotonically increasing).
# At most 300 calls will be made to hit and getHits.
# Follow up: What if the number of hits per second could be huge? Does your design scale?


# Time: O(n) | Space: O(n)
class HitCounter:

    def __init__(self):
        self.hits_list = []
        self.hits_counter = 0


    def hit(self, timestamp: int) -> None:
        print("Hitting:", timestamp)
        self.hits_list.append(timestamp)
        self.hits_counter += 1
        return None
        
    def getHits(self, timestamp: int) -> int:
        self.remove_unused(timestamp)
        print("Hits in the past 300s:", self.hits_counter)
        return self.hits_counter


    def remove_unused(self, timestamp):
        for x in self.hits_list:
            if x <= timestamp - 300:
                print("Removing", x)
                self.hits_counter -= 1
            else:
                break


# Inputs/Calls Made:
# ["HitCounter", "hit", "hit", "hit", "getHits", "hit", "getHits", "getHits"]
# [[], [1], [2], [3], [4], [300], [300], [301]]
# Outputs:
# [null, null, null, null, 3, null, 4, 3]

hitC = HitCounter()
hitC.hit(1)
hitC.hit(1)
hitC.hit(1)
hitC.hit(1)
hitC.hit(2)
hitC.hit(3)
hitC.hit(3)
hitC.hit(3)
hitC.getHits(4)
hitC.hit(300)
hitC.hit(300)
hitC.hit(300)
hitC.hit(300)
hitC.hit(300)
hitC.getHits(300)
hitC.getHits(301)
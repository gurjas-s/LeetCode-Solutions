class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        Input: target = 10, position = [1,4], speed = [3,2]
        In this case:
            position 1 car: 1,4,7,10
            position 2 car: 4,6,8,10
        
        Input: target = 10, position = [4,1,0,7], speed = [2,2,1,1]
        In this case:
            position 4 car: 4,6,8,10
            position 7 car: 7,8,9,10
            position 1 car: 1,3,5,7,9,11
            position 0 car: 0,1,2,3,4,5,6,7,8,9,10

        If all cars never meet at a point, then the number of car fleets==# of cars
        How do figure out when two cars meet at a point?
            (target-initial)/speed = #num steps to reach destination
            car1: 1,4,7,10
            car2: 0,5,10
            if car1 initial > car2 initial and stepsCar2<=stepsCar1
                then +1 fleet
        
        target=12
        position=[10,8,0,5,3]
        speed=[2,4,1,1,3]

        """

        steps = []
        n = len(position)
        sorted_arr = sorted(zip(position,speed))
        
        for i in range(n):
            p = sorted_arr[i][0]
            s = sorted_arr[i][1]
            steps.append((target-p)/s) #(10-6)//3 = 4//3 = 1.333
        
        res = len(position) #assume initially 0 fleets formed i.e each car is a fleet
        cur = steps[n-1] 
        for i in range(n-2,-1,-1): #start at closest position 
            if cur >= steps[i]:
                res -= 1
            if cur < steps[i]:
                cur = steps[i] #steps[i] becomes new cur
        return res
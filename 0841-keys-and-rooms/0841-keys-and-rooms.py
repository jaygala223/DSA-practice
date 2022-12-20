class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        q = []                                      #to visit rooms
        visited = set()
        
        q.append(0)
        
        while q:
            curr_room = q[0]
            q.pop(0)
            visited.add(curr_room)
            
            for key in rooms[curr_room]:
                if key not in visited: q.append(key)
                    
        return len(visited) == len(rooms)
        
        
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:

        m = len(meetings)
        meetings.sort()
        available_rooms, cur_meetings = [i for i in range(n)], []
        heapify(available_rooms)
        freq = defaultdict(int)
        max_frequency = 0
        ans = n

        for i in range(m):

            while cur_meetings and cur_meetings[0][0] <= meetings[i][0]:
                heappush(available_rooms, cur_meetings[0][1])
                heappop(cur_meetings)

            if not available_rooms:
                prev_end, room = heappop(cur_meetings)
                heappush(cur_meetings, [prev_end + meetings[i][1]-meetings[i][0], room])
                freq[room] += 1
            else:
                room = heappop(available_rooms)
                heappush(cur_meetings, [meetings[i][1], room])
                freq[room] += 1
        
        for room in freq:
            if freq[room] > max_frequency:
                max_frequency = freq[room]
                ans = room
            elif freq[room] == max_frequency:
                ans = min(ans, room)

        return ans
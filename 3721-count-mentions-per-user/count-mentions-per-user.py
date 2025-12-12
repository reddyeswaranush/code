class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        events.sort(key=lambda e: (int(e[1]), 0 if e[0] == "OFFLINE" else 1))

        mentions = [0] * numberOfUsers
        online_time = [-1] * numberOfUsers
        all_mentions = 0

        for event in events:
            if event[0] == "MESSAGE":
                timestamp = int(event[1])
                mentions_string = event[2]

                if mentions_string == "ALL":
                    all_mentions += 1
                elif mentions_string == "HERE":
                    for j in range(numberOfUsers):
                        if online_time[j] <= timestamp:
                            mentions[j] += 1
                else:
                    ids = mentions_string.split(" ")
                    for id_str in ids:
                        ID = int(id_str[2:])
                        mentions[ID] += 1

            else:
                timestamp = int(event[1])
                id_ = int(event[2])
                online_time[id_] = timestamp + 60

        for i in range(numberOfUsers):
            mentions[i] += all_mentions

        return mentions
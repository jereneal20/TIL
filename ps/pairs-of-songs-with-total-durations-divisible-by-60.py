class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        song_end_sec = [0] * 60
        for song_time in time:
            song_end_sec[song_time % 60] += 1

        total = 0
        if song_end_sec[0] != 0:
            total += (song_end_sec[0] * (song_end_sec[0] - 1)) // 2
        if song_end_sec[30] != 0:
            total += (song_end_sec[30] * (song_end_sec[30] - 1)) // 2
        for i in range(1, 30):
            total += song_end_sec[i] * song_end_sec[60 - i]

        return total

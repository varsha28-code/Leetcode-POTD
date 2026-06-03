from bisect import bisect_right

class Solution:
    def earliestFinishTime(self, landStartTime, landDuration,
                           waterStartTime, waterDuration):

        INF = float('inf')

        def build(starts, durations):
            rides = sorted(zip(starts, durations))
            s = [x[0] for x in rides]
            d = [x[1] for x in rides]
            n = len(rides)

            # prefix minimum duration
            pref = [0] * n
            pref[0] = d[0]
            for i in range(1, n):
                pref[i] = min(pref[i - 1], d[i])

            # suffix minimum (start + duration)
            suff = [0] * n
            suff[-1] = s[-1] + d[-1]
            for i in range(n - 2, -1, -1):
                suff[i] = min(suff[i + 1], s[i] + d[i])

            return s, pref, suff

        waterS, waterPrefDur, waterSuffSum = build(
            waterStartTime, waterDuration
        )

        landS, landPrefDur, landSuffSum = build(
            landStartTime, landDuration
        )

        ans = INF

        # Land -> Water
        for ls, ld in zip(landStartTime, landDuration):
            A = ls + ld

            idx = bisect_right(waterS, A)

            best = INF

            if idx > 0:
                best = min(best, A + waterPrefDur[idx - 1])

            if idx < len(waterS):
                best = min(best, waterSuffSum[idx])

            ans = min(ans, best)

        # Water -> Land
        for ws, wd in zip(waterStartTime, waterDuration):
            B = ws + wd

            idx = bisect_right(landS, B)

            best = INF

            if idx > 0:
                best = min(best, B + landPrefDur[idx - 1])

            if idx < len(landS):
                best = min(best, landSuffSum[idx])

            ans = min(ans, best)

        return ans
        

class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        hour_angle = (hour + minutes / 60.0) * 30
        min_angle = minutes * 6

        diff = abs(hour_angle - min_angle)

        if diff > 180:
            return 360 - diff

        return diff

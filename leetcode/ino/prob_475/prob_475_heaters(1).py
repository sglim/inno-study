# time limit fail

class Solution(object):
    def find_far_btw(self, a, b, houses):
        target = a + (b - a) // 2
        # left = 0
        # right = len(houses) - 1
        #
        # while left < right:
        #     mid = left + (right - left) // 2 + 1
        #     if houses[mid] > target:
        #         right = mid - 1
        #     else:
        #         left = mid
        #
        # return min(houses[left] - a, b - houses[left])
        near = houses[0]
        for hs in houses:
            if abs(target - hs) < abs(target - near):
                near = hs

        return min(near - a, b - near)

    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.sort()

        radius = self.find_far_btw(heaters[0] * -1, heaters[0], houses)
        last_house = houses[len(houses) - 1]
        last_heater = heaters[len(heaters) - 1]
        if last_house > last_heater:
            heaters.append(2 * last_house - last_heater)

        for i in range(1, len(heaters)):
            a = heaters[i - 1]
            b = heaters[i]
            nearest = self.find_far_btw(a, b, houses)
            radius = max(radius, nearest)

        return radius


# houses = [1, 2, 3, 4]
# heaters = [7, 100]

houses = [282475249,622650073,984943658,144108930,470211272,101027544,457850878,458777923]
heaters = [823564440,115438165,784484492,74243042,114807987,137522503,441282327,16531729,823378840,143542612]

# houses = [28,45,47]
# heaters = [11,78,82]

obj = Solution()
# print(obj.find_far_btw(a, b, houses))
print(obj.findRadius(houses, heaters))




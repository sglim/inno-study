class Solution(object):
    def get_new_map(self, houses, heaters):
        i, j, k = 0, 0, 0
        result = []
        heater_idx = []

        while i < len(houses) and j < len(heaters):
            if houses[i] > heaters[j]:
                result.append(heaters[j])
                heater_idx.append(k)
                j += 1
            elif houses[i] < heaters[j]:
                result.append(houses[i])
                i += 1
            else:
                result.append(heaters[j])
                heater_idx.append(k)
                i += 1
                j += 1
            k += 1

        while i < len(houses):
            result.append(houses[i])
            k += 1
            i += 1

        while j < len(heaters):
            result.append(heaters[j])
            heater_idx.append(k)
            k += 1
            j += 1

        return result, heater_idx

    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.sort()

        new_map, heater_idx = self.get_new_map(houses, heaters)
        radius = 0
        if heater_idx[0] != 0:
            radius = new_map[heater_idx[0]] - new_map[0]

        new_map_len = len(new_map)
        heater_idx_len = len(heater_idx)

        for i in range(heater_idx_len - 1):
            cur_heater_idx = heater_idx[i]
            next_heater_idx = heater_idx[i + 1]

            mid = (new_map[cur_heater_idx] + new_map[next_heater_idx]) // 2
            near = new_map[cur_heater_idx]
            for j in range(cur_heater_idx + 1, next_heater_idx):
                if abs(new_map[j] - mid) < abs(near - mid):
                    near = new_map[j]

            section_rad = min(near - new_map[cur_heater_idx], new_map[next_heater_idx] - near)
            radius = max(radius, section_rad)

        if new_map_len - 1 != heater_idx[heater_idx_len - 1]:
            section_rad = new_map[len(new_map) - 1] - new_map[heater_idx[len(heater_idx) - 1]]
            radius = max(radius, section_rad)

        return radius


# houses = [1, 2, 3, 4]
# heaters = [7, 100]

# houses = [282475249,622650073,984943658,144108930,470211272,101027544,457850878,458777923]
# heaters = [823564440,115438165,784484492,74243042,114807987,137522503,441282327,16531729,823378840,143542612]

houses = [28,46,47]
heaters = [11,78,82]

obj = Solution()
# print(obj.find_far_btw(a, b, houses))
print(obj.findRadius(houses, heaters))


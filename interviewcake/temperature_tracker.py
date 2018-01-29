class TemperatureTracker:

    def __init__(self):
        # O(1) space
        self.__temp_count = [0] * 111

    def insert(self, temp): # O(1)
        self.__temp_count[temp] += 1

    def get_max(self): # O(1)
        max_temp = None
        for t, count in enumerate(self.__temp_count):
            if count == 0:
                continue
            max_temp = t
        return max_temp

    def get_min(self): # O(1)
        min_temp = None
        for t, count in enumerate(self.__temp_count):
            if count == 0:
                continue
            min_temp = t
            break
        return min_temp

    def get_mean(self): # O(1)
        sum_temp = 0
        samples_count = 0

        for t, count in enumerate(self.__temp_count):
            sum_temp += t * count
            samples_count += count

        if samples_count == 0:
            return None
        else:
            return sum_temp / samples_count

    def get_mode(self): # O(1)
        modes = []
        freq_count = 0
        for t, count in enumerate(self.__temp_count):
            if count == 0:
                continue

            if count == freq_count:
                modes.append(t)
            elif count > freq_count:
                modes = [t]

            freq_count = count

        return modes

tracker = TemperatureTracker()

print(tracker.get_max()) # should be None
print(tracker.get_min()) # should be None
print(tracker.get_mean()) # should be None
print(tracker.get_mode()) # should be empty list

tracker.insert(1)
tracker.insert(1)
tracker.insert(10)
tracker.insert(10)
tracker.insert(110)

print(tracker.get_max()) # should be 110
print(tracker.get_min()) # should be 1
print(tracker.get_mean()) # should be 26.4
print(tracker.get_mode()) # should be [1, 10]

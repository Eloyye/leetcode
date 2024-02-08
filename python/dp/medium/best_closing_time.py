import unittest


class Solution:
    def best_closing_time(self, customers: str) -> int:
        n = (len(customers) + 1)
        open_penal = [float('inf')] * n
        close_penal = [float('inf')] * n
        min_ind, min_val = 0, float('inf')
        for i in range(n):
            open_penal[i] = open_penal[i - 1] + (1 if customers[i - 1] == 'N' else 0) if i - 1 >= 0 else 0
            close_penal_ind = n - i - 1
            close_penal[close_penal_ind] = 1 if (close_penal_ind) < len(customers) and customers[close_penal_ind] == 'Y' else 0
            close_penal[close_penal_ind] += close_penal[close_penal_ind + 1] if (close_penal_ind + 1) < len(customers) else 0
            if i == close_penal_ind:
                sum_penalties = close_penal[i] + open_penal[i]
                if sum_penalties <= min_val:
                    min_ind, min_val = i, sum_penalties
            elif i > close_penal_ind:
                sum_penalties1 = close_penal[i] + open_penal[i]
                sum_penalties2 = close_penal[close_penal_ind] + open_penal[close_penal_ind]
                sum_penalties, ind = min(sum_penalties1, sum_penalties2), i if sum_penalties1 < sum_penalties2 else close_penal_ind
                if sum_penalties < min_val or (sum_penalties == min_val and ind < min_ind):
                    min_ind, min_val = ind, sum_penalties
        return min_ind

    def best_closing_time_opt(self, customers: str) -> int:
        bestTime, penaltyDiff = 0, 0

        for i in range(0, len(customers)):
            if customers[i] == 'Y':
                penaltyDiff -= 1
            else:
                penaltyDiff += 1

            if penaltyDiff < 0:
                penaltyDiff = 0
                bestTime = i + 1
        return bestTime

    def best_closing_time_naive(self, customers: str) -> int:
        def update_min(current_min, current_ind, new_min, new_ind):
            if new_min < current_min:
                current_min = new_min
                current_ind = new_ind
            return current_min, current_ind
        empty_penalty = 0
        closing_penalties = [0]*(len(customers) + 1)
        min_penalty, min_penalty_index = float('inf'), 0
        for i in range(len(customers)):
            for j in range(i, len(customers)):
                closing_penalties[i] += 1 if customers[j] == "Y" else 0
            closing_penalties[i] += empty_penalty
            min_penalty, min_penalty_index = update_min(min_penalty, min_penalty_index, closing_penalties[i], i)
            empty_penalty += 1 if customers[i] == "N" else 0
        closing_penalties[len(customers)] = empty_penalty
        min_penalty, min_penalty_index = update_min(min_penalty, min_penalty_index, empty_penalty, len(customers))
        return min_penalty_index

class StoreTest(unittest.TestCase):
    def test1(self):
        best_closing_time = Solution().best_closing_time
        customers = "NYNNNYYN"
        self.assertEquals(0, best_closing_time(customers))
    def test2(self):
        best_closing_time = Solution().best_closing_time
        customers = "YYYY"
        self.assertEquals(0, best_closing_time(customers))
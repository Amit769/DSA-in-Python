class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        a = b = c = False

        for triplet in triplets:

            if (triplet[0] <= target[0] and
                triplet[1] <= target[1] and
                triplet[2] <= target[2]):

                if triplet[0] == target[0]:
                    a = True

                if triplet[1] == target[1]:
                    b = True

                if triplet[2] == target[2]:
                    c = True

        return a and b and c
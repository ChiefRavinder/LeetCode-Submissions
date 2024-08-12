class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.stream = sorted(nums, reverse=True)  # Sort the initial stream in descending order

    def add(self, val: int) -> int:
        # Insert the new value in the correct position to maintain the descending order
        self.stream.append(val)
        self.stream.sort(reverse=True)  # Sort after adding the new value

        # Return the kth largest element
        return self.stream[self.k - 1]  # k-1 because list indices start from 0



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
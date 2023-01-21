class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        task_count = Counter(tasks)
        max_val = max(task_count.values())
        max_count = list(task_count.values()).count(max_val)
        return max((max_val - 1) * (n + 1) + max_count, len(tasks))
        
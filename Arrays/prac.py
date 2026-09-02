class Solution:
    def count_teams(self, employees, expected):
        employees.sort()

        team = 0
        current_team = 0

        for employee in employees:
            current_team += employee

            if current_team == expected:
                team += 1
                current_team = 0

        return team


# Taking input
employees = list(map(int, input("Enter employee values: ").split()))
expected = int(input("Enter expected condition: "))

solution = Solution()

result = solution.count_teams(employees, expected)

print("Teams:", result)
    
    
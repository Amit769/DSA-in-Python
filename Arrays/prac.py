class Solution:
    def count_teams(employees, expected):
    employees.sort()

    team = 0
    current_team = 0

    for employee in employees:
        current_team += employee

        if current_team == expected:
            team += 1
            current_team = 0

    return team
    
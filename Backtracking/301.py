class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:

        def is_valid(string):
            balance = 0

            for ch in string:
                if ch == '(':
                    balance += 1

                elif ch == ')':
                    balance -= 1

                    if balance < 0:
                        return False

            return balance == 0

        queue = [s]
        visited = {s}

        while queue:

            current = queue.pop(0)

            if is_valid(current):
                return [current] if current == s else result

            result = []

            for i in range(len(current)):
                if current[i] not in "()":
                    continue

                new_string = current[:i] + current[i + 1:]

                if new_string not in visited:
                    visited.add(new_string)
                    queue.append(new_string)

                    if is_valid(new_string):
                        result.append(new_string)

            if result:
                return result

        return [""]
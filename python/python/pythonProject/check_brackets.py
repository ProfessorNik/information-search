def check_brackets(sequence):
    stack = []
    for bracket in sequence:
        if bracket == '(':
            stack.append(bracket)
        elif bracket == ')':
            if not stack:
                return False
            stack.pop()
    return not stack

sequence = input("Введите скобочную последовательность: ")
if check_brackets(sequence):
    print("Правильная последовательность")
else:
    print("Неправильная последовательность")
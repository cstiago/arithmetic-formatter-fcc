def error_handlers(problems, operator, *operands):
    if len(problems) > 5:
        return "Error: Too many problems."
    
    if operator != '+' and operator != '-':
        return "Error: Operator must be '+' or '-'."

    if not all([operand.isdecimal() for operand in operands]):
        return "Error: Numbers must only contain digits."

    if any([len(operand) > 4 for operand in operands]):
        return "Error: Numbers cannot be more than four digits."
    
    return False

def space_calc(longest, second):
    return ' ' * (len(longest) - len(second)) + second

def problem_length(longest):
    return len(' ' * (2 + len(longest)))

def dash_calc(longest):
    return '-' * problem_length(longest)

def arithmetic_arranger(problems, display_answers=False):
    lines = [str() for line in range(4)]

    for count, problem in enumerate(problems):
        operands = [int()] * 2
        operands[0], operator, operands[1] = problem.split()

        error = error_handlers(problems, operator, *operands)

        if error:
            return error

        lines[0] += ' ' * 2
        lines[1] += f'{operator} '

        if len(operands[0]) >= len(operands[1]):
            longest = operands[0]
            second = operands[1]

            lines[0] += longest
            lines[1] += space_calc(longest, second)
        else:
            longest = operands[1]
            second = operands[0]

            lines[0] += space_calc(longest, second)
            lines[1] += longest
        
        lines[2] += dash_calc(longest)

        operands = [int(i) for i in operands]

        if operator == '+':
            answer = sum(operands)
        elif operator == '-':
            answer = operands[0] - operands[1]
        
        answer = str(answer)

        lines[3] += ' ' * (problem_length(longest) - len(answer)) + answer

        if count != len(problems) - 1:
            lines[0], lines[1], lines[2], lines[3] = [line + (' ' * 4) for line in lines]

    arranged_problems = '\n'.join(lines[:3])

    if display_answers:
        arranged_problems = '\n'.join([arranged_problems, lines[3]])

    return arranged_problems

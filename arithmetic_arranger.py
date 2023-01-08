def error_handlers(problems, operand_a, operand_b, operator):
    if len(problems) > 5:
        return "Error: Too many problems."
    
    if operator != '+' and operator != '-':
        return "Error: Operator must be '+' or '-'."

    if not operand_a.isnumeric() or not operand_b.isnumeric():
        return "Error: Numbers must only contain digits."

    if len(operand_a) > 4 or len(operand_b) > 4:
        return "Error: Numbers cannot be more than four digits."
    
    return False

def space_calc(longest, second):
    return ' ' * (len(longest) - len(second)) + second

def problem_length(longest):
    return len(' ' * (2 + len(longest)))

def dash_calc(longest):
    return '-' * problem_length(longest)

def arithmetic_arranger(problems, display_answers=False):
    line1 = line2 = line3 = line4 = ''
    space = ' '
    gap = space * 4
    skip = '\n'

    for count, problem in enumerate(problems):
        operand_a, operator, operand_b = problem.split()

        error = error_handlers(problems, operand_a, operand_b, operator)

        if error:
            return error

        line1 += space * 2
        line2 += operator + space

        if len(operand_a) >= len(operand_b):
            longest = operand_a
            second = operand_b

            line1 += longest
            line2 += space_calc(longest, second)
        else:
            longest = operand_b
            second = operand_a

            line1 += space_calc(longest, second)
            line2 += longest
        
        line3 += dash_calc(longest)

        operand_a = int(operand_a)
        operand_b = int(operand_b)

        if operator == '+':
            answer = operand_a + operand_b
        elif operator == '-':
            answer = operand_a - operand_b
        
        answer = str(answer)

        line4 += space * (problem_length(longest) - len(answer)) + answer

        if count != len(problems) - 1:
            text = line1, line2, line3, line4
            line1, line2, line3, line4 = [line + gap for line in text]

    arranged_problems = line1 + skip + line2 + skip + line3

    if display_answers:
        arranged_problems += skip + line4

    return arranged_problems

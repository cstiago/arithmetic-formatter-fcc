def space_calc(longest, second):
    return ' ' * (len(longest) - len(second)) + second

def problem_length(longest):
    return len(' ' * (2 + len(longest)))

def dash_calc(longest):
    return '-' * problem_length(longest)

def arithmetic_arranger(problems, display_answers=False):
    elements = []
    line1 = line2 = line3 = line4 = ''
    space = ' '

    for count, problem in enumerate(problems):
        elements.append(problem.split())

        operand_a, operator, operand_b = elements[count]
    
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

    arranged_problems = ''

    return arranged_problems

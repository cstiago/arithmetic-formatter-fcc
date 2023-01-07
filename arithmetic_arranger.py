def space_calc(longest, second):
    return ' ' * (len(longest) - len(second)) + second

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

    arranged_problems = ''

    return arranged_problems

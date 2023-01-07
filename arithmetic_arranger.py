def arithmetic_arranger(problems, display_answers=False):
    elements = []
    line1 = line2 = line3 = line4 = ''
    space = ' '

    for count, problem in enumerate(problems):
        elements.append(problem.split())

        operand_a, operator, operand_b = elements[count]
    
        line1 += space * 2
        line2 += operator + space

    arranged_problems = ''

    return arranged_problems

def error_handlers(problems, operator, operands):
    if len(problems) > 5:
        return "Error: Too many problems."

    if operator != '+' and operator != '-':
        return "Error: Operator must be '+' or '-'."

    if not all([operand.isdecimal() for operand in operands]):
        return "Error: Numbers must only contain digits."

    if any([len(operand) > 4 for operand in operands]):
        return "Error: Numbers cannot be more than four digits."

    return False

def arithmetic_arranger(problems, display_answers=False):
    lines = [str() for line in range(4)]

    for count, problem in enumerate(problems):
        operands = [int()] * 2
        operands[0], operator, operands[1] = problem.split()

        error = error_handlers(problems, operator, operands)

        if error:
            return error

        max_len = len(str(max([int(operand) for operand in operands])))

        lines[0] += operands[0].rjust(2 + max_len)
        lines[1] += operator.ljust(2) + operands[1].rjust(max_len)
        lines[2] += '-' * (2 + max_len)

        operands = [int(i) for i in operands]

        answer = sum(operands) if operator == '+' else operands[0] - operands[1]
        answer = str(answer)

        lines[3] += answer.rjust(2 + max_len)

        if count != len(problems) - 1:
            lines = [line + (' ' * 4) for line in lines]

    arranged_problems = '\n'.join(lines[:3])

    if display_answers:
        arranged_problems = '\n'.join([arranged_problems, lines[3]])

    return arranged_problems

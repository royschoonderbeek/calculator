def calculate(expression):
    try:
        numbers = []
        operators = []
        current_number = ""

        for char in expression:
            if char.isdigit() or char == ".":
                current_number += char

            elif char in "+-*/": 
                if not current_number:
                    return "Error"

                numbers.append(float(current_number))
                operators.append(char)
                current_number = ""

            else:
                return "Error"

        if not current_number:
            return "Error"
        
        numbers.append(float(current_number))
        
        i = 0
        
        while i < len(operators):
            if operators[i] in "*/":
                left = numbers[i]
                right = numbers[i + 1]

                if operators[i] == "*":
                    result = left * right
                
                else:
                    if right == 0:
                        return "Cannot divide by zero."
                    
                    result = left / right

                numbers[i] = result
                del numbers[i + 1]
                del operators[i]
            
            else:
                i += 1

        result = numbers[0]
        
        for i, operator in enumerate(operators):
            if operator == "+":
                result += numbers[i + 1]

            elif operator == "-":
                result -= numbers[i + 1]

        return result
    
    except (ValueError, IndexError):
        return "Error"

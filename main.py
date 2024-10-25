import re

class Node:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.type = node_type  # "operator" or "operand"
        self.left = left       # Left child node
        self.right = right     # Right child node
        self.value = value     # Value for the operand

def create_rule(rule_string):
    # Tokenize the rule string with regex to handle operators, parentheses, and operands
    tokens = re.findall(r'\(|\)|\w+|[><=]', rule_string)
    return parse(tokens)

def parse(tokens):
    # Helper function to parse tokens into an AST
    if not tokens:
        return None
    token = tokens.pop(0)
    if token == '(':
        left = parse(tokens)
        operator = tokens.pop(0) if tokens else None
        right = parse(tokens)
        tokens.pop(0)  # Discard closing ')'
        return Node("operator", left, right, operator)
    elif token in ['AND', 'OR']:
        return Node("operator", None, None, token)
    else:
        # Assume it's an operand if it's not a parenthesis or operator
        return Node("operand", None, None, token)

def evaluate_rule(node, data):
    if node.type == "operand":
        # Expect the operand to be in the form attribute, operator, value (e.g., "age > 30")
        match = re.match(r'(\w+)\s*([><=])\s*(\w+|\d+)', node.value)
        if match:
            attribute, operator, value = match.groups()
            value = int(value) if value.isdigit() else value.strip("'")

            if operator == ">":
                return data.get(attribute, 0) > value
            elif operator == "<":
                return data.get(attribute, 0) < value
            elif operator == "=":
                return data.get(attribute, "") == value
        else:
            print(f"Error: Invalid operand format in node value '{node.value}'")
            return False
    elif node.type == "operator":
        if node.value == "AND":
            return evaluate_rule(node.left, data) and evaluate_rule(node.right, data)
        elif node.value == "OR":
            return evaluate_rule(node.left, data) or evaluate_rule(node.right, data)
    return False

if __name__ == "__main__":
    rule_str1 = "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)"
    rule1 = create_rule(rule_str1)

    user_data = {"age": 35, "department": "Sales", "salary": 60000, "experience": 3}
    result = evaluate_rule(rule1, user_data)
    print(f"User eligibility: {result}")

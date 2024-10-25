# Rule Engine with Abstract Syntax Tree (AST)

## Overview

This application is a simple rule engine designed to evaluate user eligibility based on various attributes, such as age, department, income, and experience. It uses an Abstract Syntax Tree (AST) to represent complex conditional rules, allowing dynamic creation, modification, and combination of these rules.

## Objectives

- Build a 3-tier application: Simple UI, API, and Backend.
- Use AST for dynamic rule definition and evaluation.
- Support user eligibility checks based on user attributes and rule conditions.

## Features

- **Rule Creation**: Dynamically create rules using the `create_rule` function.
- **Rule Combination**: Merge multiple rules into a single AST structure.
- **Evaluation**: Assess eligibility using JSON data input.
- **Error Handling**: Manage errors related to data format and invalid rules.

## Installation

1. Clone the repository and navigate to the App1 directory:
    ```bash
    git clone https://github.com/unusualmold2003/abstract-syntax-tree.git
    cd App1
    ```

2. Ensure you have Python 3.x installed. No additional packages are required.

## Usage

1. Open `main.py` and define your user data and rule conditions.
2. Run the script:
    ```bash
    python main.py
    ```

## Code Structure

- **`create_rule(rule_string)`**: Parses a rule string and constructs the corresponding AST.
- **`combine_rules(rules)`**: Combines multiple rules into a single AST for evaluation efficiency.
- **`evaluate_rule(json_data)`**: Evaluates the rule using JSON user data to determine eligibility.

## Sample Rules

- **Rule 1**: `((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)`
- **Rule 2**: `((age > 30 AND department = 'Marketing')) AND (salary > 20000 OR experience > 5)`

## Example Execution

```python
# Example user data
user_data = {"age": 35, "department": "Sales", "salary": 60000, "experience": 3}

# Execute eligibility check
result = evaluate_rule(rule1, user_data)
print("User eligibility:", result)

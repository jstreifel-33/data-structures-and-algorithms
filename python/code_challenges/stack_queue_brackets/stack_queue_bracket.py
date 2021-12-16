from stacks_and_queues.stacks import Stack

def validate_brackets(test_str):
    brackets = Stack()
    for char in test_str:
        if char == "(":
            brackets.push(")")
        elif char == "[":
            brackets.push("]")
        elif char == "{":
            brackets.push("}")
        elif char == ")" or char =="]" or char == "}":
            if not char == brackets.pop():
                return False
    return True

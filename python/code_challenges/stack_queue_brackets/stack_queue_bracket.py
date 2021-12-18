from stacks_and_queues.stacks import Stack

def validate_brackets(test_str):
    bracket_map = {
        "}":"{",
        ")":"(",
        "]":"["
    }

    brackets = Stack()
    for char in test_str:
        if char in bracket_map.values():
            brackets.push(char)
        elif char in bracket_map:
            try:
                if not bracket_map[char] == brackets.pop():
                    return False
            except:
                return False

    if brackets.is_empty():
        return True
    else:
        return False

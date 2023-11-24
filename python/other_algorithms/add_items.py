def add_items(lst : list[int]) -> str:
    if len(lst) == 1:
        return str(lst[0])
    for item in lst:
        return f"(+ {str(item)} {add_items(lst[1:])})"

def nested_sub(lst):
    if len(lst) == 1:
        return lst[0]
    return lst[0] - nested_sub(lst[1:])

def nested_let(args, nums):
    if len(args) == 0:
        return "<here>"
    return f"(let (({args[0]} {nums[0]})) {nested_let(args[1:], nums[1:])})"

if __name__ == "__main__":

def strict(func):
    def wrapper(*args, **kwargs):

        annotations = func.__annotations__
        param_count = func.__code__.co_argcount
        param_names = func.__code__.co_varnames[:param_count]

        all_args = dict(zip(param_names, args))
        all_args.update(kwargs)

        for arg_name, arg_value in all_args.items():
            if arg_name in annotations:
                expected_type = annotations[arg_name]
                if not isinstance(arg_value, expected_type):
                    raise TypeError(
                        f"Argument '{arg_name}' must be {expected_type.__name__}, "
                        f"not {type(arg_value).__name__}"
                    )

        return func(*args, **kwargs)
    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


print(sum_two(1, 2))  # >>> 3
print(sum_two(1, 2.4))  # >>> TypeError

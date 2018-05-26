import re

some_text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut
    labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi
    ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum
    dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia
    deserunt mollit anim id est laborum."""


def censor(forbidden, substitution):
    def function_body_receiver(function_body):
        def func_arg_rec(function_args):
            result = function_body(function_args)
            reg_sep = "|"
            filtered = re.sub(reg_sep.join(forbidden), substitution,
                              result)  # Making string from tuple & filter using RegExp
            return filtered

        return func_arg_rec

    return function_body_receiver


@censor(forbidden=("ipsum", "quis"), substitution="[CENSORED]")
def text_producer(text):
    return text


p = text_producer(some_text)
print(p)

# Here is a function that is close to xrange in Python2 except it can also generate negative raw without step argument
# and/or take kwargs. It can take up to three arguments organized by the start, stop, step logic. Two arguments only:
# start, stop, abs(default_step) = 1. One argument - stop, default_start = 0, abs(default_step) = 1.


def arrange(*args, **kwargs):
    if 0 >= (len(args) + len(kwargs)) > 3:
        raise ValueError('arrange requires 1-3 integer arguments')
    elif (len(args) + len(kwargs)) == 1:
        if len(kwargs) == 0:
            if args[0] == 0:
                return
            elif args[0] > 0:
                current, stop, step = 0, args[0], 1
            else:
                current, stop, step = 0, args[0], -1
        else:
            if kwargs["stop"] == 0:
                return
            elif kwargs["stop"] > 0:
                current, stop, step = 0, kwargs["stop"], 1
            elif kwargs["stop"] < 0:
                current, stop, step = 0, kwargs["stop"], -1
            else:
                raise ValueError('Your dict kwarg must have "stop" key for generator to be engaged')
    elif (len(args) + len(kwargs)) == 2:
        if len(args) == 2:
            if args[1] > args[0]:
                current, stop, step = args[0], args[1], 1
            elif args[1] < args[0]:
                current, stop, step = args[0], args[1], -1
            else:
                raise ValueError('Input an existing range for generator')
        elif len(kwargs) == 1:
            if kwargs["stop"] > args[0]:
                current, stop, step = args[0], kwargs["stop"], 1
            elif kwargs["stop"] < args[0]:
                current, stop, step = args[0], kwargs["stop"], -1
            else:
                raise ValueError('Use keyword "stop" for your end-range argument')
        elif len(kwargs) == 2:
            if kwargs["stop"] > kwargs["start"]:
                current, stop, step = kwargs["start"], kwargs["stop"], 1
            elif kwargs["stop"] < kwargs["start"]:
                current, stop, step = kwargs["start"], kwargs["stop"], -1
            else:
                raise ValueError('Set an existing range: use keywords "start", "stop"')
    elif (len(args) + len(kwargs)) == 3:
        if len(args) == 3:
            if (args[1] > args[0] and args[2] > 0) or (args[1] < args[0] and args[2] < 0):
                current, stop, step = args[0], args[1], args[2]
            else:
                raise ValueError('Input the existing range for generator')
        if len(kwargs) == 3:
            if (kwargs["stop"] > kwargs["start"] and kwargs["step"] > 0) or (
                    kwargs["stop"] < kwargs["start"] and kwargs["step"] < 0):
                current, stop, step = kwargs["start"], kwargs["stop"], kwargs["step"]
            else:
                raise ValueError('Set an existing range: use keywords "start", "stop", "step" for your dict arguments')
        if len(kwargs) == 2:
            if (kwargs["stop"] > args[0] and kwargs["step"] > 0) or (kwargs["stop"] < args[0] and kwargs["step"] < 0):
                current, stop, step, = args[0], kwargs["stop"], kwargs["step"]
            else:
                raise ValueError('Set an existing range use keywords "stop", "step" for your dict arguments')
        if len(kwargs) == 1:
            if (args[1] > args[0] and kwargs["step"] > 0) or (args[1] < args[0] and kwargs["step"] < 0):
                current, stop, step = args[0], args[1], kwargs["step"]
            else:
                raise ValueError('Set an existing range: use keyword "step" for your dict argument')

    # # Generating part of the function

    if step > 0:
        while current < stop:
            yield current
            current += step
    else:
        while current > stop:
            yield current
            current += step


# Uncomment the last strings for different tests

# g = arrange(896, 8, **{'step': -101})
# g = arrange(**{'stop': -40, 'start': 50, "step": -12})
#
# print(list(g))

# for x in arrange(-78, **{"stop": 94, "step": -13}):
#     print(x)
for x in arrange(0):
    print(x)

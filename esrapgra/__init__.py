def esrapgra(*args, **kwargs):
    '''
    Convert function arguments to command-line arguments.
    '''

    _separator = kwargs.get('_separator', '-')
    _prefix = kwargs.get('_prefix', '--')
    _kwargs_last = kwargs.get('_kwargs_last', True)

    # remove special kwargs so they don't get turned into arguments
    for kw in ['_separator', '_prefix', '_kwargs_last']:
        if kw in kwargs:
            del kwargs[kw]

    final_arguments = []

    for k, v in kwargs.items():

        # handle --boolean flags
        if type(v) == bool:
            if v == True:
                final_arguments.append('{}{}'.format(_prefix, k.replace('_', _separator)))
            else:
                pass # skip argument if it's boolean and False
        else:
            # these are regular arguments
            final_arguments.append(
                    ('{}{}={}'.format(
                        _prefix,
                        k.replace('_', _separator),
                        v
                    )
                    )
                )

    # put in the non-flag arguments either at the beginning or end
    if _kwargs_last:
        [ final_arguments.append(arg) for arg in args ]
    else:
        [ final_arguments.insert(0, arg) for arg in args ]

    return final_arguments

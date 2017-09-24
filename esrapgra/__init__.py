def esrapgra(*args, **kwargs):
    '''
    Convert function arguments to command-line arguments.
    '''

    # copy dict so we can mess with it
    kwargs = dict(kwargs)

    _separator = kwargs.get('_separator', '-')
    _prefix = kwargs.get('_prefix', '--')
    _kwargs_first = kwargs.get('_kwargs_first', True)

    if '_separator' in kwargs:
        del kwargs['_separator']

    if '_prefix' in kwargs:
        del kwargs['_prefix']

    if '_kwargs_first' in kwargs:
        del kwargs['_kwargs_first']

    arg_word__separator = '_'

    final_arguments = []

    for k, v in kwargs.items():
        final_arguments.append(
                ('{}{}={}'.format(
                    _prefix,
                    k.replace(arg_word__separator, '-'),
                    v
                )
                )
            )

    if _kwargs_first:
        [ final_arguments.append(arg) for arg in args ]
    else:
        [ final_arguments.insert(0, arg) for arg in args ]

    return ' '.join(final_arguments)

def esrapgra(*args, **kwargs):
    '''
    Convert function arguments to command-line arguments.
    '''

    # copy dict so we can mess with it
    kwargs = dict(kwargs)

    _separator = kwargs.get('_separator', '-')
    _prefix = kwargs.get('_prefix', '--')
    _kwargs_last = kwargs.get('_kwargs_last', True)

    for kw in ['_separator', '_prefix', '_kwargs_last']:
      if kw in kwargs:
        del kwargs[kw]

    final_arguments = []

    for k, v in kwargs.items():
        final_arguments.append(
                ('{}{}={}'.format(
                    _prefix,
                    k.replace('_', _separator),
                    v
                )
                )
            )

    if _kwargs_last:
        [ final_arguments.append(arg) for arg in args ]
    else:
        [ final_arguments.insert(0, arg) for arg in args ]

    return ' '.join(final_arguments)

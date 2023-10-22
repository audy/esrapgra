from typing import List


class Esrapgra:
    def __init__(
        self,
        separator: str = "-",
        prefix: str = "--",
        kwargs_last: bool = False,
        quote_strings: bool = True,
        quote_char: str = '"',
    ):
        """
        Initializes the Esrapgra object with various configuration options.

        Args:
        separator (str): character(s) inserted between words in keyword
        arguments. By default, underscores are converted into hyphens. Default
        is "-".

        prefix (str): character(s) inserted at the beginning of keyword
        arguments. Default is "--".

        kwargs_last (bool): Determines whether to put keyword arguments before
        positional arguments. Default is False.

        quote_strings (bool): If True, quotes strings. Default is True.

        quote_char (str): The character used for quoting strings. Default is '"'.

        Examples:
        >>> Esrapgra(separator="_").lext_arguments(test_argument="test")
        [ '--test_argument="test"' ]

        >>> Esrapgra(separator="X").lext_arguments(test_argument="test")
        [ '--testXargument="test"' ]

        >>> Esrapgra(prefix="-").lext_arguments(test_argument="test")
        [ '-test_argument="test"' ]

        >>> Esrapgra(kwargs_last=False).lext_arguments("first_arg", test_argument="test")
        [ '-test_argument="test"', "first_arg" ]

        >>> Esrapgra(kwargs_last=True).lext_arguments("first_arg", test_argument="test")
        ["first_arg", '-test_argument="test"' ]

        """

        self.separator = separator
        self.prefix = prefix
        self.kwargs_last = kwargs_last
        self.quote_strings = quote_strings
        self.quote_char = quote_char

    def lex_arguments(self, *args, **kwargs) -> List[str]:
        """
        Convert args and kwargs into unix-style command-line arguments
        """

        final_arguments = []

        for key, value in kwargs.items():
            # handle --boolean flags
            keyword = key.replace("_", self.separator)

            if type(value) == bool:
                if value is True:
                    final_arguments.append(f"{self.prefix}{keyword}")
                else:
                    pass  # skip argument if it's boolean and False
            else:
                if type(value) == str and self.quote_strings:
                    value = f"{self.quote_char}{value}{self.quote_char}"
                # these are regular arguments
                final_arguments.append(f"{self.prefix}{keyword}={value}")

        # put in the non-flag arguments either at the beginning or end
        if self.kwargs_last:
            final_arguments = list(args) + final_arguments
        else:
            final_arguments = final_arguments + list(args)

        return final_arguments

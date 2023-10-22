# Esrapgra

[![Test](https://github.com/audy/esrapgra/actions/workflows/test.yml/badge.svg)](https://github.com/audy/esrapgra/actions/workflows/test.yml)

The opposite of argparse. Converts function arguments to command-line
arguments.

## Installation

```
pip install esrapgra
```

From source

```
pip install git+https://github.com/audy/esrapgra
```

## Overview

So you want to call `wget` from Python, mapping Python variables to
command-line arguments:

```sh
wget \
   http://example.com/file.zip \
   --directory-prefix=/path/to/directory \
   --retry-connrefused \
   --waitretry=5 \
   --tries=3
```

This often gets messy if you need to interpolate values into the arguments or
map Python logic into command logic:

```python
args = [
    "http://example.com/file.zip",
    "--directory-prefix",
    directory_prefix,
    f"--tries={tries}"
]

if retry_connrefused:
    args.append("--retry-connrefused")


subprocess.check_output(["wget"] + args)
```

With Esrapgra (if you can remember how to spell it), this becomes a nice
function invocation:

```python
es = Esrapgra(kwargs_last=True)

args = es.lex_arguments(
    "http://example.com/file.zip",
    directory_prefix="/path/to/directory",
    retry_connrefused=True,
    waitretry=5,
    tries=3
)

subprocess.check_output(["wget"] + args)
```

The following things are happening:

- String arguments are automatically escaped and quote to protect against
  shell-escape attacks
- Boolean arguments are automatically turned into boolean flags (e.g.,
  `retry_connrefused=True` turns into `--retry-connrefused` and
  `retry_connrefused=False` turns into nothing)
- Numeric flags are automatically converted into strings

## Examples

### Basic Initialization

You can initialize the `Esrapgra` object with default parameters:

```python
esrap = Esrapgra()
```

### Custom Separator

Customize the separator between words in keyword arguments:

```python
# Using underscores as separators
esrap = Esrapgra(separator="_")
```

```python
# Example usage
esrap.lex_arguments(test_argument="test")  # Output: ['--test_argument="test"']
```

### Custom Prefix

Define a custom prefix for the keyword arguments:

```python
# Using a single hyphen as a prefix
esrap = Esrapgra(prefix="-")
```

```python
# Example usage
esrap.lex_arguments(test_argument="test")  # Output: ['-test_argument="test"']
```

### Keyword Arguments Position

Control the position of keyword arguments relative to positional arguments:

```python
# Putting keyword arguments before positional arguments
esrap = Esrapgra(kwargs_last=False)
```

```python
# Example usage
esrap.lex_arguments(
    "first_arg",
    test_argument="test"
)
# Output: ['-test_argument="test"', 'first_arg']
```

### Quoting Strings

You can enable or disable the quoting of strings as per your needs:

```python
# Disabling quoting of strings
esrap = Esrapgra(quote_strings=False)
```

```python
# Example usage

# Adjust the expected output based on the implementation of `lex_arguments`
esrap.lex_arguments(test_argument="test")
```

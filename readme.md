# Esrapgra

The opposite of argparse. Converts function arguments to command-line
arguments.

## Why'd you make this?


Sometimes I have to write wrappers for command-line tools. I find myself often
writing code like:


```python

cmd = [
  '--some-argument', some_value,
  '--another-argument',
  'more',
  'arguments',
]

subprocess.run(cmd)

```

Now I can do

```python

subprocess.run(
  esrapgra(
    some_argument=some_value,
    another_argument=True,
    'more',
    'arguments'
  )
)
```

... which is a bit nicer :)


## Examples


```python
res = esrapgra(
        'bleep',
        'bloop',
        some_argument=21,
        another_argument=1000,
        bool_argument=True
        )

# returns:

['--some-argument=21', '--another-argument=1000', '--bool-argument', 'bleep', 'bloop']


# you can customize as well

esrapgra(
  'some',
  'arguments',
  test_parameter=5,
  bool_argument=True,
  _separator='_',
  _prefix='-',
  _kwargs_last=False
)

# returns:

['some', 'arguments', '-test_parameter=5', '-bool_argument']
```

## License

The MIT License (MIT)
Copyright (c) 2017 Austin Davis-Richardson

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

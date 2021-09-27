if __name__ == "__main__":
    sample_lower = "hello world, #hey, 123"
    sample_upper = "HELLO WORLD, #HEY, 123"
    sample_tabs = "hello\tworld,\t#hey,\t123"
    sample_format = "hello {name}"
    map_ = {'x': 1, 'y': 2}
    sample_format_map = "{x} {y}"
    sample_alnum = "helloworldhey123"
    sample_alpha = "helloworld"
    sample_ascii = "hello world # 123"
    sample_dec = "123"
    sample_digit = "⁰³⁸"
    sample_id = "hello"
    sample_numeric = "ⅠⅢⅧ"
    sample_spaces = "  "
    sample_title = "Hello World"
    sample_join = ["1", "2", "3"]
    sample_makestran1 = "abc"
    sample_makestran2 = "def"
    makestran = "abc"
    sample_splitline = "hello\nworld"
    sample_strip = "   hello world   "
    sample_swapcase = "Hello World"
    dict_ = {83: 80}
    sample_translate = "Hello Sam!"

    print(sample_lower.capitalize())  # Converts the first character to upper case => Hello world, #hey, 123
    print(sample_upper.casefold())  # Converts string into lower case => hello world, #hey, 123
    print(sample_lower.center(50, '*'))  # Returns a centered string
    # => **************hello world, #hey, 123**************
    print(sample_lower.count("123"))  # Returns the number of times a specified value occurs in a string => 1
    print(sample_lower.encode())  # Returns an encoded version of the string => b'hello world, #hey, 123'
    print(sample_lower.endswith("123"))  # Returns true if the string ends with the specified value => True
    print(sample_tabs.expandtabs(10))  # Sets the tab size of the string => hello     world,    #hey,     123
    print(sample_lower.find("l"))  # Searches the string for a specified value and returns the position of
    # where it was found => 2
    print(sample_format.format(name="Nhan"))  # Formats specified values in a string => hello Nhan
    print(sample_format_map.format_map(map_))  # Formats specified values in a string => 1 2
    print(sample_lower.index("h"))  # Searches the string for a specified value and returns the position of
    # where it was found => 0
    print(sample_alnum.isalnum())  # Returns True if all characters in the string are alphanumeric => True
    print(sample_alpha.isalpha())  # Returns True if all characters in the string are in the alphabet => True
    print(sample_ascii.isascii())  # Returns True if all characters in the string are ascii characters => True
    print(sample_dec.isdecimal())  # Returns True if all characters in the string are decimals (0 - 9 only) => True
    print(sample_digit.isdigit())  # Returns True if all characters in the string are digits => True
    print(sample_id.isidentifier())  # Returns True if the string is an identifier => True
    print(sample_lower.islower())  # Returns True if all characters in the string are lower case => True
    print(sample_numeric.isnumeric())  # Returns True if all characters in the string are numeric => True
    print(sample_lower.isprintable())  # Returns True if all characters in the string are printable => True
    print(sample_spaces.isspace())  # Returns True if all characters in the string are whitespaces => True
    print(sample_title.istitle())  # Returns True if the string follows the rules of a title => True
    print(sample_upper.isupper())  # Returns True if all characters in the string are upper case => True
    print(", ".join(sample_join))  # Joins the elements of an iterable to the end of the string => 1, 2, 3
    print(sample_lower.ljust(50, "*"))  # Returns a left justified version of the string
    # => hello world, #hey, 123****************************
    print(sample_upper.lower())  # Converts a string into lower case => hello world, #hey, 123
    print(sample_lower.lstrip("hello "))  # Returns a left trim version of the string => world, #hey, 123
    print(makestran.maketrans(sample_makestran1, sample_makestran2))  # Returns a translation table to be used
    # in translations => {97: 100, 98: 101, 99: 102}
    print(sample_lower.partition("l"))  # Returns a tuple where the string is parted into three parts
    # => ('he', 'l', 'lo world, #hey, 123')
    print(sample_lower.replace("hello", "HELLO"))  # Returns a string where a specified value is replaced with
    # a specified value => HELLO world, #hey, 123
    print(sample_lower.rfind("l"))  # Searches the string for a specified value and returns the last position of
    # where it was found => 9
    print(sample_lower.rindex("l"))  # Searches the string for a specified value and returns the last position of
    # where it was found => 9
    print(sample_lower.rjust(50, "*"))  # Returns a right justified version of the string
    # => ****************************hello world, #hey, 123
    print(sample_lower.rpartition("l"))  # Returns a tuple where the string is parted into three parts
    # => ('hello wor', 'l', 'd, #hey, 123')
    print(sample_lower.rsplit(" ", 1))  # Splits the string at the specified separator, and returns a list
    # => ['hello world, #hey,', '123']
    print(sample_lower.rstrip(" 123"))  # Returns a right trim version of the string => hello world, #hey,
    print(sample_lower.split(" ", 1))  # Splits the string at the specified separator, and returns a list
    # => ['hello', 'world, #hey, 123']
    print(sample_splitline.splitlines(False))  # Splits the string at line breaks and returns a list
    # => ['hello', 'world']
    print(sample_lower.startswith("hello"))  # Returns true if the string starts with the specified value => True
    print(sample_strip.strip(" "))  # Returns a trimmed version of the string => hello world
    print(sample_swapcase.swapcase())  # Swaps cases, lower case becomes upper case and vice versa => hELLO wORLD
    print(sample_lower.title())  # Converts the first character of each word to upper case => Hello World, #Hey, 123
    print(sample_translate.translate(dict_))  # Returns a translated string => Hello Pam!
    print(sample_lower.upper())  # Converts a string into upper case => HELLO WORLD, #HEY, 123
    print(sample_lower.zfill(50))  # Fills the string with a specified number of 0 values at the beginning
    # => 0000000000000000000000000000hello world, #hey, 123

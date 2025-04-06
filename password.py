import re

password = "Secure@123"
password_pattern = r"^(?=.[a-z])(?=.[A-Z])(?=.\d)(?=.[@#$%^&+=!]).{8,}$"

match = re.match(password_pattern, password)

if match:
    print("Valid password")
else:
    print("Invalid password")


url = "http://ww.google.com/"
url_pattern = r"^(https?:\/\/)?(www\.)?[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(\S*)?$"

match = re.match(url_pattern, url)

if match:
    print("Valid URL:", url)
else:
    print("Invalid URL")


# 1. ValueError
try:
    int("abc")
except ValueError as e:
    print("ValueError:", e)

# 2. TypeError
try:
    result = "5" + 3
except TypeError as e:
    print("TypeError:", e)

# 3. IndexError
try:
    lst = [1, 2, 3]
    print(lst[5])
except IndexError as e:
    print("IndexError:", e)


# 4. KeyError
try:
    d = {"name": "Rahman"}
    print(d["age"])
except KeyError as e:
    print("KeyError:", e)

# 5. NameError
try:
    print(unknown_var)
except NameError as e:
    print("NameError:", e)

# 6. ZeroDivisionError
try:
    print(10 / 0)
except ZeroDivisionError as e:
    print("ZeroDivisionError:", e)

# 7. FileNotFoundError
try:
    open("nonexistent_file.txt")
except FileNotFoundError as e:
    print("FileNotFoundError:", e)

# 8. AttributeError
try:
    num = 5
    num.append(10)
except AttributeError as e:
    print("AttributeError:", e)

# 9. ImportError
try:
    from math import cube
except ImportError as e:
    print("ImportError:", e)

# 10. ModuleNotFoundError
try:
    import fake_module
except ModuleNotFoundError as e:
    print("ModuleNotFoundError:", e)

# 11. SyntaxError - shown in comments since it breaks code parsing
# try:
#     eval("if True print('Hi')")
# except SyntaxError as e:
#     print("SyntaxError:", e)

# 12. IndentationError - not executable inside script
# def hello():
# print("Hi")

# 13. RuntimeError
try:
    raise RuntimeError("This is a runtime error")
except RuntimeError as e:
    print("RuntimeError:", e)

# 14. StopIteration
try:
    it = iter([1, 2])
    print(next(it))
    print(next(it))
    print(next(it))
except StopIteration as e:
    print("StopIteration:", e)

# 15. OverflowError
import math
try:
    print(math.exp(1000))
except OverflowError as e:
    print("OverflowError:", e)

# 16. AssertionError
try:
    assert 2 + 2 == 5, "Math error!"
except AssertionError as e:
    print("AssertionError:", e)

# 17. KeyboardInterrupt - can't simulate here safely

# 18. MemoryError - not run here, risky for system stability
# huge_list = [1] * (10**10)

# 19. NotImplementedError
try:
    raise NotImplementedError("This feature is not implemented yet")
except NotImplementedError as e:
    print("NotImplementedError:", e)
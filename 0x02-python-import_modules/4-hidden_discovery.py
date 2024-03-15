#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4
    attributes = [member for member in dir(hidden_4)
                  if not member.startswith("__")]
    for x in attributes:
        print(x)

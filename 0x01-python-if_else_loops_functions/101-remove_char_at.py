#!/usr/bin/python3

def remove_char_at(str, n):
    modif_str = None
    modif_str = str[:n] + str[n + 1:]
    return (modif_str)

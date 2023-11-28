#!/usr/bin/python3
""" print the  alphabet, in lowercase, not followed by a new line."""
for alpha_letters in range(ord('a'), ord('z')+1:
        if alpha_letters == 'e' or alpha_letters == 'q':
        continue
        print("{:c}".format(alpha_letters), end="")

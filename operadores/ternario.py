#!python3

lockdown = True

status = 'Em casa' if lockdown else 'Uhuuu'

print(status)

lockdown = False

print(status)

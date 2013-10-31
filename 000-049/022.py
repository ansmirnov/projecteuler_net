print sum(map(lambda x, y: x*y, [sum([ord(c) - 64 for c in list(line.strip())]) for line in sorted(open('names.txt', 'rt').readline().replace('"', '').split(','))], range(1, 5164)))

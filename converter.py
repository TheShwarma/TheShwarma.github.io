f = open("NoxcrewFactoryServerLogUpDown.txt", "w")
for line in reversed(list(open("NoxcrewFactoryServerLog.txt"))):
    f.write(line)
f.close()
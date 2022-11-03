file1 = open('case input', 'r')
count = 0
import re

# Using for loop
print("Using for loop")
processing = []
NEW = "new"
SAME_AS_SOMETHING = "same"
for line in file1:
    element = {}
    count += 1
    line = line.strip()
    print(count, end=" ")
    element["ind"] = count
    info = []
    if line.find("equals") > 0:
        element["type"] = SAME_AS_SOMETHING
        info = re.findall(r'[0-9]+', line.strip())
    else:
        element["type"] = NEW
        info = re.findall(r'{[^{}]+}', line.strip())
        info = [i[1:-1] for i in info]
    print(info)
    element["info"] = info
    processing.append(element)
print("adfasdfasdfasdfasdfasdfasf")
for p in processing:
    print(p)
print("adfasdfasdfasdfasdfasdfasf")
outputs = []

print("asdfasdfasfasdfasdfasdfasdfasdfasdf")
for e in processing:
    print(e)
    if e["type"] == NEW:
        i = e["info"]
        output = None
        if 'x' in i[0]:
            output = f"part(pre={'1'}, loc={'r' + i[4] + i[5]}, y_0={i[2]}, y_1={i[3]}, x_0={i[0].replace('x', 'y')}, " \
                     f"x_1={i[1]}, pi=m{i[6][-1]})"
        else:
            output = f"part(pre={'1'}, loc={'r' + i[4] + i[5]}, x_0={i[2]}, x_1={i[3]}, y_0={i[0]}, y_1={i[1]}, pi=m{i[6][-1]})"
        output = output.replace("0.25", "r14")
        output = output.replace("0.75", "r34")
        output = output.replace("2.25", "r94")
        output = output.replace("2b_v", "2*b_v")
        outputs.append([e["ind"], output])
    else:
        for o in outputs:
            if str(o[0]) == e["info"][0]:
                o[1] = o[1][:9] + "2" + o[1][10:]
    for o in outputs:
        print(',\n'+o[1], end="")

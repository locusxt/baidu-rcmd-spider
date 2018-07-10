# -*- coding: utf-8 -*-
import json

f = open("items.json")
ss = ""
for l in f:
    ss += l.strip()

data = json.loads(ss)

out = ""
for it in data:
    q = it['query']
    if u"您的访问出错了" in q:
        continue
    tops = filter(lambda x: x!=None, it['topic'])
    try:
        tmp = ",".join([q]+tops)
        out += tmp +"\n"
        # print tmp
    except Exception as e:
        print ">>>>"
        print e
        print q
        print tops
        print ">>>>"

wf = open("out.csv", "w")
wf.write(out.encode("utf-8"))
wf.close()
f.close()
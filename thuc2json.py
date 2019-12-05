#! -*- coding: utf-8 -*-
import json
import sys

def read_thuc(ff):
    f = open(ff)
    title = f.readline().strip()
    content = []
    for c in f.readlines():
        c = c.strip()
        if c is None or len(c) == 0:
            continue
        content.append(c)
    dic = {}
    dic['title'] = title
    dic['content'] = '\n'.join(content)
    return dic

import os
def thuc2json(pp, ff):
    val = os.listdir(pp)
    cnt = 0
    f = open(ff, 'w')
    for v in val:
        thuc = read_thuc('%s/%s' % (pp, v))
        f.write(json.dumps(thuc, ensure_ascii=False)+'\n')
        cnt +=1
        if cnt >100:
            break


if __name__ == '__main__':
    thuc2json(sys.argv[1], sys.argv[2])

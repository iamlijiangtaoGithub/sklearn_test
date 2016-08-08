#!/usr/bin/python
#coding=utf8
import pandas as pd
reader = pd.read_csv('/home/hdp_teu_search/ljt/sample/ershouche_sample.txt',header=None,delimiter="\t", iterator=True)
loop = True
chunkSize = 100000
chunks = []
while loop:
    try:
        chunk = reader.get_chunk(chunkSize)
        chunks.append(chunk)
    except StopIteration:
        loop = False
        print "Iteration is stopped."
df = pd.concat(chunks, ignore_index=True)

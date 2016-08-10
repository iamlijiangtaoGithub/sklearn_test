#!/usr/bin/python
#coding=utf8
import pandas as pd

def readBigData(filePath,delim,header=None):
    reader = pd.read_csv(filePath,header=None,delimiter=delim, iterator=True)
    loop = True
    chunkSize = 100000
    chunks = []
    while loop:
        print "read chunk "
        try:
            chunk = reader.get_chunk(chunkSize)
            chunks.append(chunk)
        except StopIteration:
            loop = False
            print "Iteration is stopped."
    df = pd.concat(chunks, ignore_index=True)
    print "read ok!"
    return df


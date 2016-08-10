
# coding: utf-8

# In[2]:

get_ipython().magic(u'matplotlib inline')
import numpy as np 
import pandas as pd 
import os 
import sys
sys.path.append("/home/me/xx/classify_cate")


# In[8]:

df = pd.read_csv('/home/me/xx/classify_cate/infoid_cate3.txt',header=0,delimiter=" ")


# In[12]:

df.columns= ['infoid','catePath3']
df.head()


# In[43]:

get_ipython().magic(u'matplotlib inline')
import numpy as np 
import pandas as pd 
import matplotlib.pylab as plt
x=np.arange(1,10000,1)
y=np.log2(x)
plt.plot(x,y,'o')


# In[57]:

import random 
import numpy as np
indexList=[]
#从index中随机抽取n个
#从index中随机抽取比率为rate的个数,

for cate ,group in df.groupby(by='catePath3'):
    print cate
    #print group 
    sampleCount=len(group.index)
    extractCount= sampleCount if np.log2(sampleCount) <8 else np.log2(sampleCount)
    
    print 'sample count:',sampleCount,";extract count:log2(sampleCount)",extractCount
    indexList.extend(random.sample(group.index.values,int(extractCount)))


#用分组，可以获取到index 索引号。这样可以从分组中，抽取样本。只需要写好抽取样本的函数即可。


# In[58]:

print 'original sample count',len(df.index),'after extract sample:', len(indexList)


# In[62]:

extractSample=df.iloc[indexList,:]
print extractSample.head()


# In[ ]:

#以上是 进行分层抽样，进行平滑，大类下的抽样，与小类下的抽样，抽样后，个数基本一致
#项目要求只将 大类下的数据去掉一小部分即可，尽量保留信息：方案：依然是log，将log后值作为需要去除的比率。


# In[117]:

import random 
import numpy as np
indexList=[]
#从index中随机抽取n个
#从index中随机抽取比率为rate的个数,

for cate ,group in df.groupby(by='catePath3'):
    print cate
    #print group 
    sampleCount=len(group.index)
    extractCount= sampleCount if  sampleCount <10000 else sampleCount* (1-np.log(sampleCount)/100)
    extractCount= extractCount/2 if extractCount>300*10000 else extractCount #发现离群点，对其进行约束
    print 'sample count:',sampleCount,";extract count:log2(sampleCount)",extractCount
    indexList.extend(random.sample(group.index.values,int(extractCount)))


# In[118]:

print 'original sample count',len(df.index),'after extract sample:', len(indexList)


# In[119]:

extractSample=df.iloc[indexList,:]
print extractSample.head()


# In[120]:

mapCate2Count={}
for cate ,group in df.groupby(by='catePath3'):
    mapCate2Count[cate]=len(group)


# In[121]:

mapCate2CountAfterExtract={}
for cate ,group in extractSample.groupby(by='catePath3'):
    mapCate2CountAfterExtract[cate]=len(group)
    


# In[122]:

df2 =pd.DataFrame.from_dict(mapCate2Count,orient='index').T


# In[123]:

df2.head()


# In[124]:

df1 =pd.DataFrame.from_dict(mapCate2Count,orient='index')


# In[135]:

plt.plot(mapCate2Count.keys(),mapCate2Count.values(),'b*',label="original")
plt.plot(mapCate2CountAfterExtract.keys(),mapCate2CountAfterExtract.values(),'ro',label="afterExtract")
plt.xlabel('cate')
plt.ylabel('count')
plt.legend('lower right')


# In[127]:

#有异常点，对离群点，进行特殊的处理——单独砍一半
extractSample.to_csv("/home/me/xx/classify_cate/extractSample.csv",sep='\t',columns=None, header=None, index=None, index_label=None)
df


# In[131]:

df = pd.read_csv('/home/me/xx/classify_cate/0501_0801.title',header=0,delimiter="\t")


# In[132]:

df.head()


# In[ ]:




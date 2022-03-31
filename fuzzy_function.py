import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

#Author :Nguyễn Bá Huy-19146194

#Hàm Liên Thuộc(membership function)
def mf(x,function="gaussmf",a=None,b=None,c=None,range=None):
  assert function in ["gbellmf","gaussmf","trapmf","trimf"]
  if function == "gbellmf":
    funct=fuzz.gbellmf(x,a,b,c)# range=fuzz.gbellmf(b1,10,20,30) 
  if function == "gaussmf":
    funct=fuzz.gaussmf(x,a,b) #gaussmf chi co 2 input a,b
  if function == "trimf":
    funct=fuzz.trimf(x,range)#range=[30,30,50] 
  if function == "trapmf":
    funct=fuzz.trapmf(x,range)#range=[30,30,50,60]
  return funct

#Visualize plot function
def plot_func(x,y,color='b',title="Tên biểu đồ",xlabel="tên trục x",ylabel="tên trục x",loc='upper center'):
  plt.figure()
  assert color in ['b','r','g','v']
  if color=='b':
    plt.plot(x,y,'b',linewidth=1.5,label=f'{y}')
  if color=='r':
    plt.plot(x,y,'r',linewidth=1.5,label=f'{y}')
  if color=='g':
    plt.plot(x,y,'g',linewidth=1.5,label=f'{y}')
  if color=='v':
    plt.plot(x,y,'v',linewidth=1.5,label=f'{y}')
  plt.title(name)
  plt.xlabel(xlabel)
  plt.ylabel(ylabel)
  assert loc in ['upper center','upper left','upper right','lower left']
  if loc =="upper center":
    plt.legend(loc,bbox_to_anchor=(1.5,2),ncol=1,shadow=True,fancybox=True)
  if loc =='right':
    plt.legend(loc,bbox_to_anchor=(1.5,2),ncol=1,shadow=True,fancybox=True)
  if loc =='upper left':
    plt.legend(loc,bbox_to_anchor=(1.5,2),ncol=1,shadow=True,fancybox=True)
  if loc =='upper right':
    plt.legend(loc,bbox_to_anchor=(1.5,2),ncol=1,shadow=True,fancybox=True)
  if loc =='lower left':
    plt.legend(loc,bbox_to_anchor=(1.5,2),ncol=1,shadow=True,fancybox=True)
    

def input_signal(x,y,xlabel='food',ylabel='tips'):
  input=ctrl.Antecedent(x,xlabel)
  output=ctrl.Consequent(y,ylabel)
  #Tạo hàm liên thuộc
  if y is not None:
    return input,output
  else:
    return input
  
 
def output_signal(output,funtion="trimf",contribute="less",range=None,a,b,c):
  assert function in ["trimf","trapmf","gaussmf","gbellmf"]
  if function=="trimf":#range=[30,30,50]
    output[f"{contribute}"]=fuzz.trimf(output.universe,range)
  if function=="trapmf":#range=[30,30,50,60]
    output[f"{contribute}"]=fuzz.trapmf(output.universe,range)
  if function=="gaussmf":#gaussmf chi co 2 input a,b
    output[f"{contribute}"]=fuzz.gaussmf(output.universe,a,b)
  if function=="gbellmf":# range=fuzz.gbellmf(b1,10,20,30) 
    output[f"{contribute}"]=fuzz.gbellmf(output.universe,a,b,c)
  return output[f"{contribute}"]  



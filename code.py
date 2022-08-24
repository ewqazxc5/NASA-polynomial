import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from scipy.interpolate import CubicSpline
import csv

# R - universal gas constant, 8.314510 J/(mol-K)
R=8.314510
data=pd.read_csv('table6.dat',sep='\t',header=None,low_memory=False)
row_number=len(data[0])
T=data[0][2]
T=T.split('   ')


x=[]
num=len(T)
for i in range(1,num):
    x+=[float(T[i])]
# set x axis temperature
x=np.array(x)


def get_Cp_parameter(row,IA,IB,start_number,save=1):  # start_number=2 or 1

    data_row=data[0][row].split('   ')
    name=data_row[(start_number-1)].lstrip()

    multiplier=(2*IA+1)*(2*IB+1)
    y=[]
    num=len(data_row)
    for i in range(start_number,num):
        y+=[multiplier*float(data_row[i])]

    #cubic spline interpolation
    cs = CubicSpline(x, y)
    #set x axis after using cubic spline method as xs
    xs = x
    fig = plt.figure(figsize=(15,6))

    ax1 = fig.add_subplot(131)
    ax2 = fig.add_subplot(132)
    ax3=fig.add_subplot(133)
    

    ax1.plot(x, y, 'o', label='data')
    ax1.plot(xs, cs(xs), label="Q-cubic_spline")
    #First two moments of partition function
    Q1=xs*cs(xs, 1)
    Q2=xs*xs*cs(xs, 2)+2*xs*cs(xs,1)
    ax2.plot(xs, Q1, label="Q'")
    ax2.plot(xs, Q2, label="Q''")

    ax1.set_xlim(0,10000)
    ax1.legend(loc='upper left', ncol=2)
    ax1.set_title(name)
    ax2.set_xlim(0,10000)
    ax2.legend(loc='upper left', ncol=2)
    ax2.set_title('derivative')

    #calculated specific heat
    Cp=R*(Q2/cs(xs)-(Q1/cs(xs))**2)+5*R/2


        


    ax3.plot(xs,Cp, label="Cp")
    
    
    CpT2_R=Cp*x*x/R
    #choose temperature in interval 298.15-6000K
    x1=x[28:32]
    #least square method
    z1=np.polyfit(x1,CpT2_R[28:32],6)
    p1=np.poly1d(z1)
    X1=xs = np.arange(300,1000,1)
    y_fit_part1=p1(X1)*R/X1/X1
    x2=x[31:38]
    z2=np.polyfit(x2,CpT2_R[31:38],6)
    p2=np.poly1d(z2)
    X2=xs = np.arange(1000,6000,1)
    y_fit_part2=p2(X2)*R/X2/X2
    
    y_fitted=np.array([])
    XX=np.array([])
  
    for i in range(28,37):
        
        z=np.polyfit(x[i:i+2],CpT2_R[i:i+2]*R/x[i:i+2]/x[i:i+2],1)
        xx=np.arange(x[i],x[i+1],1)
        XX=np.concatenate((XX,xx))

        p=np.poly1d(z)
        y_fit_part=p(xx)
        y_fitted=np.concatenate((y_fitted,y_fit_part))

    
    #get fitted y using least square coefficients
    y_fit=np.concatenate((y_fit_part1,y_fit_part2))
    #calculate residuals
    resd=y_fit-y_fitted
    #set another scale in the same graph
    ax32=ax3.twinx()
   
    ax32.plot(XX,resd, label="residual",color='k')
    ax32.set_ylabel(name+' residual-T')
    ax32.legend(loc='upper right')
    ax32.set_xlim(300,6000)
    
    ax3.plot(np.concatenate((X1,X2)),y_fit, label="Cp_fitted")
    ax3.set_ylabel(name+' Cp-T')
    ax3.legend(loc='upper left')
    ax3.set_xlim(300,6000)
    #choose save data or show data
    if save==1:
        with open('Cp0.csv','a',newline='') as w:
            writer=csv.writer(w,delimiter=',')
        
            writer.writerows([np.concatenate((np.array([name]),Cp[28:38],np.array([np.var(resd)])))])


        with open('coefficients.csv','a',newline='') as w:
            writer=csv.writer(w,delimiter=',')
        
            writer.writerows([np.concatenate((np.array([name]),p1))])
            writer.writerows([np.concatenate((np.array([name]),p2))])
        # os.mkdir('picture')
        file_name = './picture/'+name+'.png'
    
        plt.savefig(file_name, bbox_inches='tight')
    else:
        plt.show()
        print('Cp0')
        print(np.concatenate((np.array([name]),Cp[28:38])))

        print('variance')
        print(np.var(resd))
        print('coeff_300-1000K')
        print(np.concatenate((np.array([name]),p1)))
        print('coeff_1000-6000K')
        print(np.concatenate((np.array([name]),p2)))
    return p1,p2
 

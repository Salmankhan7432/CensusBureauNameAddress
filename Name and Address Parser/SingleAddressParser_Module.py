# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 00:06:20 2022

@author: onais
"""


import re
from tqdm import tqdm
import pandas as pd
import json 
import collections 
#Parsing 1st program
<<<<<<< Updated upstream
import re

=======
# import re
import os
import sys
import subprocess
>>>>>>> Stashed changes

from datetime import datetime,timedelta
today=datetime.today()

import os.path



file_dir = os.path.dirname(os.path.realpath('__file__'))



from pathlib import Path

root_folder = Path(__file__).parents[1]


<<<<<<< Updated upstream
def Address_Parser(line,initials):
=======
def throwException(originalInput,initials):
    ExceptionDict = {
        "INPUT": originalInput,
        str(Mask_1): FirstPhaseList
    }
    Exception_file_name = initials + "_Forced_ExceptionFile.json"
    Exception_file_name = re.sub(r'[^\w_. -]', '_', Exception_file_name)
    path = 'Exceptions/ForcedExceptions/' + Exception_file_name
    with open(path, 'w', encoding='utf-8') as g:
        json.dump(ExceptionDict, g, indent=4)
    return
def Address_Parser(line,initials,originalInput):
    global Result, Exception_file_name, FirstPhaseList, Mask_1
>>>>>>> Stashed changes
    Result={}
    Exception_file_name=""
    fileHandle = open('USAddressWordTable.txt', 'r',encoding="utf8")
    # Strips the newline character
    Observation=0
    Total=0
    Truth_Result={}
    dataFinal={}
    FirstPhaseList=[]
    Address=re.sub(',',' , ',line)
    Address=re.sub(' +', ' ',Address)
    Address=re.sub('[.]','',Address)
    #Address=re.sub('#','',Address)    
    Address=Address.upper()
    AddressList = re.split("\s|\s,\s ", Address)
    #del(AddressList[len(AddressList)-1])
    TrackKey=[]
    Mask=[]
    Combine=""
    LoopCheck=1
    for A in AddressList:
        FirstPhaseDict={}
        NResult=False
        try:
            Compare=A[0].isdigit()
        except:
            print()
        if A==",":
            Mask.append(Combine)
            Combine=""
            FirstPhaseList.append(",")
            #FirstPhaseList.append("Seperator")
        elif Compare:
            Combine+="N"
            TrackKey.append("N")
            FirstPhaseDict["N"]=A
            FirstPhaseList.append(FirstPhaseDict)
        else:
            for line in fileHandle:
                fields=line.split('|')
                if A==(fields[0]):
                    NResult=True
                    temp=fields[1]
                    Combine+=temp[0]
                    FirstPhaseDict[temp[0]] = A
                    FirstPhaseList.append(FirstPhaseDict)
                    TrackKey.append(temp[0])
            if NResult==False:
                Combine+="W"
                TrackKey.append("W")
                FirstPhaseDict["W"] = A
                FirstPhaseList.append(FirstPhaseDict)
        if LoopCheck==len(AddressList):
            Mask.append(Combine)
        fileHandle.seek(0)
        LoopCheck+=1
    Mask_1=",".join(Mask)
    FirstPhaseList = [FirstPhaseList[b] for b in range(len(FirstPhaseList)) if FirstPhaseList[b] != ","]
    data={}
    with open('JSONMappingDefault.json', 'r+', encoding='utf-8') as f:
        data = json.load(f)
    Found=False
    FoundDict={}
    for tk,tv in data.items():
        if(tk==Mask_1):
            FoundDict[tk]=tv
            Found=True
            break
    
    if Found:
        Observation+=1
        Mappings={}
        for K2,V2 in FoundDict[Mask_1].items():
            Temp=""
            for p in V2:
                for K3,V3 in FirstPhaseList[p-1].items():
                   Temp+=" "+V3
                   Temp=Temp.strip()
                   Mappings[K2]=[K3,Temp]       
        try:
<<<<<<< Updated upstream
            Result["Output"]=Mappings
        except:
=======
            Result["Input"]= originalInput
            Result["Output"]=Mappings
        except:
            Result["Input"]= originalInput
>>>>>>> Stashed changes
            Result["Output"]=Mappings
        
        
        
        Output_file_name=initials+'_Output_'+str(today)+".txt"
        Output_file_name=re.sub(r'[^\w_. -]', '_', Output_file_name)
        path= 'Output/'+Output_file_name
        with open(path,'w', encoding='utf-8') as g:
            g.seek(0)
            Stat=Mappings
            json.dump(Stat,g,indent=4)
            g.truncate
        
<<<<<<< Updated upstream
    else:  
        Exception_file_name=initials+'_ExceptionFile_'+str(today)+".txt"
        Exception_file_name=re.sub(r'[^\w_. -]', '_', Exception_file_name)
        path= 'Exceptions/SingleException/'+Exception_file_name
        with open(path,'w', encoding='utf-8') as g:
            g.seek(0)
            Stat={}
            Stat[Mask_1]=FirstPhaseList
            json.dump(Stat,g,indent=4)
            g.truncate
=======
    else:
        ExceptionDict = {
            "INPUT": originalInput,
            str(Mask_1): FirstPhaseList
        }
        Exception_file_name = initials + "_ExceptionFile.json"
        Exception_file_name = re.sub(r'[^\w_. -]', '_', Exception_file_name)
        path = 'Exceptions/SingleException/' + Exception_file_name
        with open(path, 'w', encoding='utf-8') as g:
            json.dump(ExceptionDict, g, indent=4)
            
        
        # Exception_file_name=initials+'_ExceptionFile_'+str(today)+".txt"
        # Exception_file_name=re.sub(r'[^\w_. -]', '_', Exception_file_name)
        # path= 'Exceptions/SingleException/'+Exception_file_name
        # with open(path,'w', encoding='utf-8') as g:
        #     g.seek(0)
        #     Stat={}
        #     # Stat=originalInput
        #     Stat[Mask_1]=originalInput,FirstPhaseList
        #     json.dump(Stat,g,indent=4)
        #     g.truncate
        
        
>>>>>>> Stashed changes
    Total+=1
    print(Result)
    return (Result, Mask_1,Exception_file_name)
# print("Final Correct Address Parsing Percentage",Count_of_Correct/Total_Count*100)
# print("Address Matching Report")
# print("Total=",Count)
# print("Matched Addresses=",Observation)
# print("Percentage of Matched",(Observation/Count)*100)
        # print("Mask Generated is ",Mask_1)
    # print("Index\tMaskToken\t\tAddress Token")
    # i=1
    # for k in FirstPhaseList:
    #     for key,value in k.items():
    #         print(i,"\t\t",key,"\t\t\t\t",value) 
    #     i+=1
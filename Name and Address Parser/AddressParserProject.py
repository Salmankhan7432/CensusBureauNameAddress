import re
from tqdm import tqdm
import pandas as pd
import json 
Address_4CAF50=open("S4G.txt","r")
Lines = Address_4CAF50.readlines()
DF=[]
ii=0
count = 0
FinalList=[]
fileHandle = open('USAddressWordTable.txt', 'r')
# Strips the newline character
Count=len(Lines)
DF=pd.DataFrame()
C=1
CC=1
AllAddress_Key_Value_As_MASK_Comp={}
for line in tqdm(Lines):
    MASK=[] #In String
    
    Old_Address=line.strip()
    USAD_Conversion_Dict={"USAD_SNO":"","USAD_SPR":"","USAD_SPR":"","USAD_SNM":"","USAD_SFX":"","USAD_SPT":"","USAD_ANM":"","USAD_ANO":"","USAD_CTY":"","USAD_STA":"","USAD_ZIP":"","USAD_ZP4":"","USAD_BNM":"","USAD_BNO":"","USAD_RNM":""}
    List=USAD_Conversion_Dict.keys()
    FirstPhaseList=[]
    Address=re.sub(',',' , ',line)
    Address=re.sub(' +', ' ',Address)
    Address=re.sub('[.]','',Address)
    #Address=re.sub('#','',Address)
    
    Address=Address.upper()
    AddressList = re.split("\s|\s,\s ", Address)
    del(AddressList[len(AddressList)-1])
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
            O=0
            Mask.append(Combine)
            Combine=""
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
    print("\n")
    print(Mask)
    USAD_Mapping={"USAD_SNO":[],"USAD_SPR":[],"USAD_SPR":[],"USAD_SNM":[],"USAD_SFX":[],"USAD_SPT":[],"USAD_ANM":[],"USAD_ANO":[],"USAD_CTY":[],"USAD_STA":[],"USAD_ZIP":[],"USAD_ZP4":[],"USAD_BNM":[],"USAD_BNO":[],"USAD_RNM":[]}
    Start=0
    Counts=0
    if "X" not in TrackKey:
        
        for R in USAD_Conversion_Dict:
            
            if R=="USAD_SNO":
                for j in range(Counts,len(TrackKey)):
                    Dictionary=FirstPhaseList[j]
                    Key=""
                    Value=""
                    for K,V in Dictionary.items():
                        Key=K
                        Value=V
                    if Key=="N":
                        USAD_Mapping["USAD_SNO"].append(j+1)
                        USAD_Conversion_Dict["USAD_SNO"]+=" "+Value.strip()
                        Counts+=1
                    if TrackKey[j+1]!="N":
                        USAD_Mapping["USAD_SNO"]=USAD_Mapping["USAD_SNO"]
                        USAD_Conversion_Dict["USAD_SNO"]=USAD_Conversion_Dict["USAD_SNO"].strip()
                        break
                    
                        
            elif R=="USAD_SPR":
                for j in range(Counts,len(TrackKey)):
                    Dictionary=FirstPhaseList[Counts]
                    Key=""
                    Value=""
                    for K,V in Dictionary.items():
                        Key=K
                        Value=V
                    if Key=="D":
                        USAD_Mapping["USAD_SPR"].append(j+1)
                        USAD_Conversion_Dict["USAD_SPR"]+=" "+Value.strip()
                        Counts+=1
                    if TrackKey[j+1]!="D":
                        USAD_Mapping["USAD_SPR"]=USAD_Mapping["USAD_SPR"]
                        USAD_Conversion_Dict["USAD_SPR"]=USAD_Conversion_Dict["USAD_SPR"].strip()
                        break

            elif R=="USAD_SNM":
                for j in range(Counts,len(TrackKey)):
                    Dictionary=FirstPhaseList[j]
                    Key=""
                    Value=""
                    for K,V in Dictionary.items():
                        Key=K
                        Value=V
                    if Key=="W" or Key=="N":
                        USAD_Conversion_Dict["USAD_SNM"]+=" "+Value.strip()
                        Counts+=1
                    if Key=="W":
                        if TrackKey[j+1]!="W":
                            USAD_Mapping["USAD_SNM"].append(j+1)
                            USAD_Conversion_Dict["USAD_SNM"]=USAD_Conversion_Dict["USAD_SNM"].strip()
                            break
                    else :
                        if TrackKey[j+1]!="N":
                            USAD_Mapping["USAD_SNM"]=USAD_Mapping["USAD_SNM"]

                            USAD_Conversion_Dict["USAD_SNM"]=USAD_Conversion_Dict["USAD_SNM"].strip()
                            break
            elif R=="USAD_SFX":
                for j in range(Counts,len(TrackKey)):
                    Dictionary=FirstPhaseList[j]
                    Key=""
                    Value=""
                    for K,V in Dictionary.items():
                        Key=K
                        Value=V
                    if Key=="F":   
                        USAD_Mapping["USAD_SFX"].append(j+1)
                        USAD_Conversion_Dict["USAD_SFX"]+=" "+Value.strip()
                        Counts+=1
                    if TrackKey[j+1]!="F":
                        USAD_Mapping["USAD_SFX"]=USAD_Mapping["USAD_SFX"]
                        USAD_Conversion_Dict["USAD_SFX"]=USAD_Conversion_Dict["USAD_SFX"].strip()
                        break
            elif R=="USAD_SPT":
                for j in range(Counts,len(TrackKey)):
                    Dictionary=FirstPhaseList[j]
                    Key=""
                    Value=""
                    for K,V in Dictionary.items():
                        Key=K
                        Value=V
                    if Key=="D":
                        USAD_Mapping["USAD_SPT"].append(j+1)
                        USAD_Conversion_Dict["USAD_SPT"]+=" "+Value.strip()
                        Counts+=1
                    if TrackKey[j+1]!="D":
                        USAD_Mapping["USAD_SPT"]=USAD_Mapping["USAD_SPT"]
                        USAD_Conversion_Dict["USAD_SPT"]=USAD_Conversion_Dict["USAD_SPT"].strip()
                        break
            elif R=="USAD_ANM":
                for j in range(Counts,len(TrackKey)):
                    Dictionary=FirstPhaseList[j]
                    Key=""
                    Value=""
                    for K,V in Dictionary.items():
                        Key=K
                        Value=V
                    if Key=="S":
                        USAD_Mapping["USAD_ANM"].append(j+1)
                        USAD_Conversion_Dict["USAD_ANM"]+=" "+Value.strip()
                        Counts+=1
                    try:
                        if TrackKey[j+1]!="N":
                            USAD_Mapping["USAD_ANM"]=USAD_Mapping["USAD_ANM"]
                            USAD_Conversion_Dict["USAD_ANM"]=USAD_Conversion_Dict["USAD_ANM"].strip()
                        break
                    except:
                        USAD_Conversion_Dict["USAD_ANM"]=USAD_Conversion_Dict["USAD_ANM"].strip()
                        break
            elif R=="USAD_ANO":
                for j in range(Counts,len(TrackKey)):
                    Dictionary=FirstPhaseList[j]
                    Key=""
                    Value=""
                    for K,V in Dictionary.items():
                        Key=K
                        Value=V
                    if Key=="N":
                        USAD_Mapping["USAD_ANO"].append(j+1)
                        USAD_Conversion_Dict["USAD_ANO"]+=" "+Value.strip()
                        Counts+=1
                    try:
                        if TrackKey[j+1]!="N":
                            USAD_Mapping["USAD_ANO"]=USAD_Mapping["USAD_ANO"]

                            USAD_Conversion_Dict["USAD_ANO"]=USAD_Conversion_Dict["USAD_ANO"].strip()
                        break
                    except:
                        USAD_Conversion_Dict["USAD_ANO"]=USAD_Conversion_Dict["USAD_ANO"].strip()
                        break
            elif R=="USAD_CTY":
                for j in range(Counts,len(TrackKey)):
                    Dictionary=FirstPhaseList[j]
                    Key=""
                    Value=""
                    for K,V in Dictionary.items():
                        Key=K
                        Value=V
                    if Key=="W":
                        USAD_Mapping["USAD_CTY"].append(j+1)
                        USAD_Conversion_Dict["USAD_CTY"]+=" "+Value.strip()
                        Counts+=1
                    if TrackKey[j+1]!="W":
                        USAD_Mapping["USAD_CTY"]=USAD_Mapping["USAD_CTY"]
                        USAD_Conversion_Dict["USAD_CTY"]=USAD_Conversion_Dict["USAD_CTY"].strip()
                        break
            elif R=="USAD_STA":
                for j in range(Counts,len(TrackKey)):
                    Dictionary=FirstPhaseList[j]
                    Key=""
                    Value=""
                    for K,V in Dictionary.items():
                        Key=K
                        Value=V
                    if Key=="T":
                        USAD_Mapping["USAD_STA"].append(j+1)
                        USAD_Conversion_Dict["USAD_STA"]+=" "+Value.strip()
                        Counts+=1
                    if TrackKey[j+1]!="T":
                        USAD_Mapping["USAD_STA"]=USAD_Mapping["USAD_STA"]

                        USAD_Conversion_Dict["USAD_STA"]=USAD_Conversion_Dict["USAD_STA"].strip()
                        break
            elif R=="USAD_ZIP":
                for j in range(Counts,len(TrackKey)):
                    Dictionary=FirstPhaseList[j]
                    Key=""
                    Value=""
                    for K,V in Dictionary.items():
                        Key=K
                        Value=V
                    if Key=="N":
                        USAD_Mapping["USAD_ZIP"].append(j+1)
                        USAD_Conversion_Dict["USAD_ZIP"]+=" "+Value.strip()
                        Counts+=1
                    try:
                        if TrackKey[j+1]!="N":
                            USAD_Mapping["USAD_ZIP"]=USAD_Mapping["USAD_ZIP"]

                            USAD_Conversion_Dict["USAD_ZIP"]=USAD_Conversion_Dict["USAD_ZIP"].strip()
                            break
                    except:
                            USAD_Mapping["USAD_ZIP"]=USAD_Mapping["USAD_ZIP"]
                            USAD_Conversion_Dict["USAD_ZIP"]=USAD_Conversion_Dict["USAD_ZIP"].strip()
        else:
            print()    
    Tempp=[]
    New_Mapping={}
    for i, kk in USAD_Mapping.items():
        if len(kk)!=0:
            New_Mapping[i]=kk
    Tempp.append(Old_Address)
    Tempp.append(Mask)
    Tempp.append(New_Mapping)
    AllAddress_Key_Value_As_MASK_Comp[CC]=Tempp
    USAD_Conversion_Dict["Old_Address"]=str(Old_Address)
    FinalList.append(USAD_Conversion_Dict)
    count += 1
    CC+=1
print(AllAddress_Key_Value_As_MASK_Comp)
DF=pd.DataFrame(FinalList)



DF.to_csv("OUTPUT_ADDRESSParse.csv", encoding='utf-8')
#print(DF)   
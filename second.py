import sys
import subprocess

DATA = [
  ['오백삼십조칠천팔백구십만천오백삼십구', '삼조사천이만삼천구'],
  ['육십사억삼천십팔만칠천육백구', '사십삼'],
  ['구백육십조칠천억팔천백삼십이만칠천일', '사십삼조오천이백억육천구백십만일'],
  ['이천구백육십조천오백칠십만삼천구백구십', '삼천사백오십조일억이천만육백사십삼'],
  ['사십오억삼천육십만오백구십', '칠십억천이백삼십오만칠천구십이'],
  ['천백십일', '구천오백구십구'],
  ['오억사천', '백십일'],
  ['만오천사백삼십', '십구만삼천오백'],
  ['일조', '삼'],
  ['일억', '만'],
]

def get_preprocessed_number(number):
    preprocess_dict = {
        "-":  "",
        ":":  "",
        ".":  "",
        "영":  "0",
        "공":  "0",
        "일":  "1",
        "하나": "1",
        "둘":  "2",
        "이":  "2",
        "셋":  "3",
        "삼":  "3",
        "사":  "4",
        "넷":  "4",
        "다섯": "5",
        "오":  "5",
        "육":  "6",
        "륙":  "6",
        "여섯": "6",
        "칠":  "7",
        "일곱": "7",
        "팔":  "8",
        "여덟": "8",
        "아홉": "9",
        "구":  "9",
    }
    
    for key, value in preprocess_dict.items():
        number = number.replace(key, value)
    
    return number

def get_processed_number(number):
    preprocess_dict = {
        "1":"일",
        "2":"이",
        "3":"삼",
        "4":"사",
        "5":"오",
        "6":"육",
        "7":"칠",
        "8":"팔",
        "9":"구",
    }
    
    for key, value in preprocess_dict.items():
        number = number.replace(key, value)
    
    return number


def find_jo(a) :
    if a ==1:
        return -1
    else:
        unit = a.find('조')
        return unit

def find_uk(a) :
    if a ==1:
        return -1
    else:
        unit = a.find('억')
        return unit

def find_man(a) :
    if a ==1:
        return -1
    else:        
        unit = a.find('만')
        return unit

def find_cheon(a) :
    if a==1 :
        return -1
    unit =a.find('천')
    return unit

def find_baek(a) :
    if a ==1:
        return -1
    else:
        unit =a.find('백')
        return unit

def find_sip(a) :
    if a ==1:
        return -1
    else:
        unit =a.find('십')
        return unit
    


def toInt(a) :
    if a==1:
        return 1
    if a=='no':
        return 0
    if len(a)==0:
        return 0
    if a==0:
        return 0
    cheon=find_cheon(a);
    if len(a)==0:
        result_baek=0
    else:
        if cheon ==0 :
            result_cheon=1
            a=a[1:]
        elif cheon>0 :
            result_cheon = a[0:cheon]
            a = a[cheon+1:]
        else:
            result_cheon = 0
    
    if len(a)==0:
        result_baek=0
    else:
        
        baek=find_baek(a)
        if baek ==0 :
            result_baek=1
            a=a[1:]
        elif baek>0 :
            result_baek = a[0:baek]
            a = a[baek+1:]
        else:
            result_baek = 0
            
    if len(a)==0:
        result_sip=0
    else:
        sip=find_sip(a)
        if sip==0 :
            result_sip=1
            a=a[1:]
        elif sip>0 :
            result_sip = a[0:sip]
            a = a[sip+1:]
        else:
            result_sip = 0
        
    if len(a)==0:
        remain=0
    else :
        remain=int(a)
        
    cheon =int(result_cheon)*1000
    baek = int(result_baek)*100
    sip = int(result_sip)*10
    result_some = cheon+baek+sip+remain

    return result_some
    
    

    

def final(a) :
    result=get_preprocessed_number(a)
    jo = find_jo(result)
    if jo>0 :
        result_jo = result[0:jo]
        result = result[jo+1:]
    else :
        result_jo = 'no'

    uk = find_uk(result)
    if uk>0 :
        result_uk = result[0:uk]
        result = result[uk+1:]
    else:
        result_uk = 'no' 

    man = find_man(result)    
    if man==0 :
        result_man = 1
        result = result[1:]
    elif man>0 :
        result_man = result[0:man]
        result = result[man+1:]
    else:
        result_man = 'no'
    jo = toInt(result_jo) *1000000000000
    uk = toInt(result_uk) *100000000
    man = toInt(result_man)*10000
    remain = toInt(result)
    final = jo+uk+man+remain
    
    return final


def Changing(jo):
    jo =str(jo)
    length=len(jo)
    jo =str(jo)
    length=len(jo)
    cm=''
    if length==4:
        
        if jo[0]=='1':
            cm='천'
        elif jo[0]=='0':
            cm=cm
        else:
            cm=jo[0]+'천'

        if jo[1]=='1':
            cm=cm+'백'
        elif jo[1]=='0':
            cm=cm
        else:
            cm=cm+jo[1]+'백'

        if jo[2]=='1':
            cm=cm+'십'
        elif jo[2]=='0':
            cm=cm;
        else:
            cm=cm+jo[2]+'십'

        if jo[3]=='0':
            cm=cm;
        else:
            cm=cm+jo[3]


    elif length==3:
        if jo[0]=='1':
            cm='백'
        elif jo[0]=='0':
            cm=cm
        else:
            cm=jo[0]+'백'

        if jo[1]=='1':
            cm=cm+'십'
        elif jo[1]=='0':
            cm=cm
        else:
            cm=cm+jo[1]+'십'
        if jo[2]=='0':
            cm=cm
        else:
            cm=cm+jo[2]

    elif length==2:
        if jo[0]=='1':
            cm='십'
        elif jo[0]=='0':
            cm=cm
        else:
            cm=jo[0]+'십'

        if jo[1]=='0':
            cm=cm
        else:
            cm=cm+jo[1]
            
    elif length==1:
        if jo[0]=='0':
            cm=cm
        else:
            cm=cm+jo[0]
                
    return cm
    
    




def finishfunction(tmp):
    str_tmp = str(tmp)
    length = len(str_tmp)
    if length>12:
        jo =str_tmp[0:length-12]
        str_tmp=str_tmp[len(jo):length]
        jo=int(jo)
        uk = int(str_tmp[0:4])
        str_tmp=str_tmp[4:length]
        man = int(str_tmp[0:4])
        str_tmp=str_tmp[4:length]
        remain = int(str_tmp)
    
    elif length>8:
        jo =0
        uk = str_tmp[0:length-8]
        str_tmp=str_tmp[len(uk):length]
        uk = int(uk)
        man = int(str_tmp[0:4])
        str_tmp=str_tmp[4:length]
        remain = int(str_tmp)
    
    elif length>4:
        jo =0
        uk = 0
        man =str_tmp[0:length-4]
        str_tmp=str_tmp[len(man):length]
        man=int(man)
        remain = int(str_tmp)
    
    elif length>4:
        jo =0
        uk =0
        man =0
        remain = int(str_tmp)

    jo=Changing(jo)
    uk=Changing(uk)
    man=Changing(man)
    remain=Changing(remain)
    if len(jo)>0:
        jo=jo+'조'
    if len(uk)>0:
        uk=uk+'억'
    if len(man)>0:
        man=man+'만'
    
    if len(jo)<1 and len(uk)<1 and len(man)>0:
        if man=='1만':
            man='만'
    
    if len(jo)<1 and len(uk)<1 and len(man)<1:
        length2 = len(remain)
        temp1 = remain[0:2]
        if temp1=='1천':
            remain='천'+remain[2:length2]
        elif temp1=='1백':
            remain='백'+remain[2:length2]
        elif temp1=='1십':
            remain='십'+remain[2:length2]
            
        
    result=jo+uk+man+remain        
    print(get_processed_number(result))
    
    
        

    


for pair in DATA:
    a, b = pair
    stri = final(a)+final(b)
    finishfunction(stri)

    

    
    
    



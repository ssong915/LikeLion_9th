#리스트 : 변할 수도 있는 데이터들
#list=[1,2,3] -> list[0]=1, list[0:2]=1,2

#튜플 : 변하면 안되는 데이터들
#tuple=(1,2,3)

#딕셔너리 : key,value 짝꿍 (2*N)
#dictionary={key1:value1,key2:value2}

#문자열실습
str="이 멋쟁이 사자처럼"
str2="은 좋은 동아리입니다"

print(str+str2)
print(str[4])
print(str[0:3]) #0~2인덱스까지
print(len(str)) #길이
print(str.count('이')) #특정 문자 몇번?
print(str.split()) #특정 문자 기준으로 split

print(str.find('사')) #특정 문자 몇번째?
print(str.find('가')) #없으므로 -1

print(str.index('사')) 
# print(str.index('가')) 없으므로 검색안됌

#리스트실습
list=[3,1,"배가",4,"고파요",5,1]
num=[3,2,4,5,1]
print(list[0:2]) #인덱싱 슬라이싱
print(len(list)) #길이
num.sort() #오름차순
print(num) 
print(list.count(1)) 
print(list.index("배가"))

#딕셔너리실습
pairs={'아이유':'라일락','잔나비':'뜨거운','폴킴':'비'}
pairs['스탠딩']='휴식'
print(pairs)
del pairs['잔나비']
print(pairs)
print(pairs.get('아이유')) #키로 value 검색
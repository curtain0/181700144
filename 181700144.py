import re
import json
imformation :{
    '姓名':'',
    '手机':'',
    '地址':[],
}
with open('address_query.txt','r')as file_obj:
	t1=file_obj.read()
	s1=t1.split('\n')
	cnt1=0
	data=dict()
	for i in s1:
		if(cnt1%3==0):
			list_add=s1[cnt1+2].split(' ')
			data[s1[cnt1+1]]=list_add
		cnt1=cnt1+1

def split_string(str):
    s = str.split(',')
    empty_dict = dict()
    empty_dict['name'] = s[0][2:]
    patten = re.compile(r'\d{11}')
    telephone = patten.findall(s[1])
    empty_dict['telephone'] = telephone[0]
    hh = s[1].split(telephone[0])
    hh = s[1].split(telephone[0])
    address = hh[0] + hh[1][0:-1]
    empty_dict['address'] = address
    return empty_dict

while 1:  # 循环直到读到END
	try:  # 尝试 然后捕获异常
		str = input();  # 读入input到inputraw
		if (str == "END"):  # 如果inputraw等于END退出while的循环
			break
	except EOFError:  # 如果有eoferror异常退出循环
		break
	tag = str[0]
	str1 = split_string(str)
	address = str1['address']
	add= dict()
	add['name'] = str1['name']
	add['telephone'] = str1['telephone']
	county = ['区', '市', '县']
	street = ['街道', '镇', '乡']
	road = ['路', '巷', '道', '街', '弄', '胡同']
	for i in data:
		lists = []
		cnt = 0
		for j in data[i]:
			if (j == ""):
				lists.append(cnt)
			cnt = cnt + 1
		for list in lists:
			data[i].pop((int)(list))
	for i in data:
		if (address.find(i) != -1):
			add['province'] = i
			if (i == '北京' or i == '上海' or i == '天津' or i == '重庆'):
				add['province'] = i
				add['city'] = i + '市'
				if (address.find('市') != -1):
					address = address[address.find('市') + 1:]
				else:
					address = address[2:]
			else:
				if (i != '广西壮族自治区' and i != '内蒙古自治区' and i != '新疆维吾尔自治区' and i != '宁夏回族自治区'):
					add['province'] = add['province'] + '省'
				for j in data[i]:
					city = j[0:-1]
					if (address.find(city) != -1):
						add['city'] = j
						if (address.find('市') != -1 and address[address.find('市') - 1] == city[-1]):
							address = address[address.find('市') + 1:]
						else:
							address = address[address.find(city[-1]) + 1:]
			break
		else:
			add['province'] = ""
			add['city'] = ""

	if (tag == '1'):
		for k in county:
			if (address.find(k) != -1):
				add['county'] = address[0:address.find(k) + 1]
				address = address[address.find(k) + 1:]
				break
			else:
				add['county'] = ""
		for y in street:
			if (y == '街道'):
				if (address.find(y) != -1):
					add['street'] = address[0:address.find(y) + 2]
					address = address[address.find(y) + 2:]
					break
				else:
					add['street'] = ""
			else:
				if (address.find(y) != -1):
					add['street'] = address[0:address.find(y) + 11]
					address = address[address.find(y) + 1:]
					break
				else:
					add['street'] = ""
		add['last'] = address
	if (tag == '2'):
		for k in county:
			if (address.find(k) != -1):
				add['county'] = address[0:address.find(k) + 1]
				address = address[address.find(k) + 1:]
				break
			else:
				add['county'] = ""
		for y in street:
			if (y == '街道'):
				if (address.find(y) != -1):
					add['street'] = address[0:address.find(y) + 2]
					address = address[address.find(y) + 2:]
					break
				else:
					add['street'] = ""
			else:
				if (address.find(y) != -1):
					add['street'] = address[0:address.find(y) + 11]
					address = address[address.find(y) + 1:]
					break
				else:
					add['street'] = ""
		for d in road:
			if (address.find(d) != -1):
				add['road'] = address[0:address.find(d) + 1]
				address = address[address.find(d) + 1:]
				break
			else:
				add['road'] = ""
		if (address.find('号') != -1):
			add['hao'] = address[0:address.find('号') + 1]
			address = address[address.find('号') + 1:]
		add['last'] = address

	result = []
	cnt=0
	for m in add:
		if(cnt>=2):
			result.append(add[m])
		cnt=cnt+1
	s1=dict()
	s1['姓名']=add['name']
	s1['电话']=add['telephone']
	s1['地址']=result

	json_str= json.dumps(s1, ensure_ascii=False)
	print(json_str)
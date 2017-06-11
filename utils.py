import json
from math import radians, cos, sin, asin, sqrt

def read_file(path):
	with open(path,'r') as json_data:
		d = json.load(json_data)
	return (d)
def save_file(data,path):
	with open(path,'w') as outfile:
		json.dump(data, outfile)
def clean_osm_file(path):
	data=open_json_file(path)
	try:
		d=data["geometries"][0]["coordinates"][0][0]
	except:
		return None
	f_data=[]
	for i in range(len(d)):
		f_data.append([d[i][1],d[i][0]])
	_save(f_data,path)
	return None
def haversine(lon1, lat1, lon2, lat2):
	"""
	Calculate the great circle distance between two points 
	on the earth (specified in decimal degrees) in meters
	"""
	# convert decimal degrees to radians 
	lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

	# haversine formula
	dlon = lon2 - lon1 
	dlat = lat2 - lat1 
	a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
	c = 2 * asin(sqrt(a)) 
	r = 6371000 # Radius of earth in meters. Use 3956 for miles
	return c*r
isLatin = lambda s: len(s) == len(s.encode())
def fotmat_phone_number(tel):
    '''
    takes a string and extracts a list of phone numbers in this string 
    InPut: str
    OutPut: list of strs
    '''
    non_decimal = re.compile(r'[^\d]+')
    all_digit=non_decimal.sub('',tel)
    if len(all_digit) in [9,10]:
        formated=[all_digit]
    else:
        local_tel=all_digit.replace('213','0',1)
        if len(local_tel) in [9,10]:
            formated= [local_tel]
        else:
            formated= [''.join(s) for s in re.findall(r'(02\d{7})|(0[567]\d{8})',local_tel)]
    if formated != []:
        return formated
    else:
        return []
def phone_number_matcher(tel1,tel2):
    '''
    cheks if there is a shared phone number between tel1 tel2 wich are lists
    InPut: 2 lists of strings 
    OutPut: set of common strings
    '''
    return set(tel1).intersection(set(tel2))
def format_name(text):
    # Remove punctuation and lowercase
    text=text.lower()
    punctuation=set(string.punctuation)
    temp=[]
    for letter in text:
        if letter in punctuation:
            temp.append(' ')
        else:
            temp.append(letter)
    text=''.join(temp)
    # Stopword removal
    words=text.split(" ")
    words2=[]
    for x  in words:
        if x not in stpwds:
            words2.append(x)
    return ' '.join(words2)
def cosine_similarity(vector1, vector2):
    top=vector1.dot(vector2)
    bottom=np.linalg.norm(vector1)*np.linalg.norm(vector2)
    if bottom==0: 
        return 0.0
    return top/bottom






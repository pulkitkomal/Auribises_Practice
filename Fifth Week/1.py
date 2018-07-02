import re

q = "Search the candle rather than the cursing darkness"

result= re.match(r"Search", q)
print(result)
print(result.start())
print(result.end())

result = re.search(r"the",q)
print(result.group(0))
print(result)
a = 'the'
print('----------')
result = re.findall(r"{}".format(a),q)
print(result)

result = re.split(r"the",q)
print(result)
print(type(result))

result = re.sub(r"the","a",q)
print(result)

pattern = re.compile("the")
print(type(pattern))
result = pattern.findall(q)
print(result)
print('--------------')

#Pattern Examples

q= 'Work hard and get luckier !!'
result = re.findall(r"\w",q)
print(result)
result = re.findall(r"\w*",q)
print(result)
result = re.findall(r"\w+",q)
print(result)

result = re.findall(r".",q)
print(result)

email = "a@example.com"
phone = "+919876543210"

#Split csv data using regex
# detect csv is correctly formed or not
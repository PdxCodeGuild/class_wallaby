import requests #https://www.geeksforgeeks.org/find-jokes-on-a-user-provided-topics-using-python/

term = input('joke keyword: ')
response = requests.get('http://icanhazdadjoke.com/search', headers = {'accept':'application/json'}, params={"term": term}).json() #headers={'Content-Encoding': 'gzip'}
#print(response.apparent_encoding)
results = response["results"]
#print(results)
for i in range(len(results)):
    print(results[i]['joke'],"\n")

# x = response.json()
# joke_1 = x
# print(joke_1)
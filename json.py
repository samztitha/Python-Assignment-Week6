import json
import requests

# -------------------------------
# 1. Convert a Python dictionary into JSON and save it in a file
# -------------------------------
data = {
    "name": "Samztitha",
    "age": 23,
    "city": "Chennai"
}

with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

print(" Dictionary saved to data.json\n")

# -------------------------------
# 2. Load data from a JSON file and print all values of a specific key
# -------------------------------
with open("data.json", "r") as f:
    loaded_data = json.load(f)

print("Loaded Name:", loaded_data.get("name"), "\n")

# -------------------------------
# 3. Parse a JSON string of multiple users and print names of users older than 25
# -------------------------------
users_json = '''
[
    {"name": "Ram", "age": 24},
    {"name": "Raj", "age": 30},
    {"name": "Chowmya", "age": 27},
    {"name": "David", "age": 22}
]
'''

users = json.loads(users_json)

print("Users older than 25:")
for user in users:
    if user["age"] > 25:
        print("-", user["name"])
print()

# -------------------------------
# 4. Fetch data from API and print titles of first 10 posts
# -------------------------------
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

if response.status_code == 200:
    posts = response.json()
    print("First 10 post titles:")
    for post in posts[:10]:
        print("-", post["title"])
else:
    print("Failed to fetch posts")
print()

# -------------------------------
# 5. Send a POST request with custom JSON data and print response
# -------------------------------
url = "https://jsonplaceholder.typicode.com/posts"
post_data = {
    "title": "My Custom Post",
    "body": "This is a test post",
    "userId": 101
}

response = requests.post(url, json=post_data)

print("POST Request Response:")
print("Status Code:", response.status_code)
print("Response JSON:", response.json(), "\n")

# -------------------------------
# 6. Check if a given website returns status code 200
# -------------------------------
website = "https://www.google.com"
resp = requests.get(website)

if resp.status_code == 200:
    print(f"{website} is UP ✅ (200 OK)")
else:
    print(f"{website} returned status code {resp.status_code}")

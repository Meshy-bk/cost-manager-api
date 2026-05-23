import requests
import sys

# =========================
# Cost Manager API Tester
# =========================

filename = input("filename=")

# Services
# a = logs service
# b = users service
# c = costs service
# d = admin service

a = "http://localhost:2003"
b = "http://localhost:2001"
c = "http://localhost:2002"
d = "http://localhost:2004"

# Redirect output to file
output = open(filename, "w", encoding="utf-8")
sys.stdout = output

print("a=" + a)
print("b=" + b)
print("c=" + c)
print("d=" + d)

print("\n==============================")
print("TESTING ADMIN /api/about")
print("==============================")

try:
    url = d + "/api/about"

    data = requests.get(url)

    print("url=" + url)
    print("status_code=" + str(data.status_code))
    print("content=" + str(data.content))
    print("text=" + data.text)
    print("json=" + str(data.json()))

except Exception as e:
    print("problem")
    print(e)

print("\n==============================")
print("TESTING REPORT - BEFORE ADD")
print("==============================")

try:
    url = c + "/api/report?id=123123&year=2026&month=5"

    data = requests.get(url)

    print("url=" + url)
    print("status_code=" + str(data.status_code))
    print("content=" + str(data.content))
    print("text=" + data.text)

except Exception as e:
    print("problem")
    print(e)

print("\n==============================")
print("TESTING ADD COST")
print("==============================")

try:
    url = c + "/api/add"

    data = requests.post(
        url,
        json={
            "userid": 123123,
            "description": "milk 9",
            "category": "food",
            "sum": 8
        }
    )

    print("url=" + url)
    print("status_code=" + str(data.status_code))
    print("content=" + str(data.content))
    print("text=" + data.text)

except Exception as e:
    print("problem")
    print(e)

print("\n==============================")
print("TESTING REPORT - AFTER ADD")
print("==============================")

try:
    url = c + "/api/report?id=123123&year=2026&month=5"

    data = requests.get(url)

    print("url=" + url)
    print("status_code=" + str(data.status_code))
    print("content=" + str(data.content))
    print("text=" + data.text)

except Exception as e:
    print("problem")
    print(e)

print("\n==============================")
print("TESTING USERS")
print("==============================")

try:
    url = b + "/api/users/123123"

    data = requests.get(url)

    print("url=" + url)
    print("status_code=" + str(data.status_code))
    print("content=" + str(data.content))
    print("text=" + data.text)

except Exception as e:
    print("problem")
    print(e)

print("\n==============================")
print("TESTING LOGS")
print("==============================")

try:
    url = a + "/api/logs"

    data = requests.get(url)

    print("url=" + url)
    print("status_code=" + str(data.status_code))
    print("content=" + str(data.content[:300]))
    print("text=" + data.text[:300])

except Exception as e:
    print("problem")
    print(e)

print("\n==============================")
print("ALL TESTS FINISHED")
print("==============================")

output.close()
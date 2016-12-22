import pyping

response = pyping.ping('google.com')

if response.ret_code == 0:
    print("reachable")
else:
    print("unreachable")

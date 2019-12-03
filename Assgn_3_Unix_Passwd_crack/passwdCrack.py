import crypt

def testPass(passwd):
    salt = passwd[:2]
    foo = open('dictionary.txt')
    for bar in foo.readlines():
        bar = bar.strip('\n')
        cryptpass = crypt.crypt(bar,salt)
        if cryptpass == passwd:
            print("[+] Found Password: " + bar  + "\n")
            return
    print("[+] Password Not Found\n ")
    return

fp = open('passwd.txt')
for foo in fp.readlines():
    if ':' in foo:
        bar = foo.strip('\n').split(':')
        user = bar[0]
        hashed_passwd = bar[1]
        print("Hashed Passwd: " + hashed_passwd)
        testPass(hashed_passwd)

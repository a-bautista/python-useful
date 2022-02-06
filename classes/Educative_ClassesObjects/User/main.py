from User import User
def main():
    u1 = User('James', '12345')
    res = u1.getUsername()
    print(res)
    u1.login('James', '12345')

main()

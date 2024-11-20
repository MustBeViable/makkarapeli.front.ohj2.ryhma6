def secret_black_sausage_chance(amount):
    secret_black_sausage_piece = 1
    if secret_black_sausage_piece== 1:
        amount+=1
        own_secret_black_sausage.append(amount)
        print("onnittelut löysit palan secret_black_sausagea. ")
        if own_secret_black_sausage==secret_black_sausage:
            own_makkaras.append("secret_black_sausage")
            print("Onnittelut löysit secret_black_sausagen!")
    return own_secret_black_sausage
amount=0
own_makkaras = []
secret_black_sausage = [1, 2, 3, 4, 5]
own_secret_black_sausage=[]

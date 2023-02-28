#********************************************************************************************ADMIN PART*************************************************************************************

import pickle
def adminChoice():
    while True:
        print('Select from the following options: ')
        print('1.Add new products')
        print('2.Update product quantity')
        print('3.Update product price')
        print('4.Update product description')
        print('5.Exit')
        choice=int(input("Enter choice: "))
        if choice==1:
            addProduct()
        elif choice==2:
            updateQ()
        elif choice==3:
            updateP()
        elif choice==4:
            updateDesc()
        else:
            print('Exiting admin mode...')
            print('*******************************************')
            return 'Exit'
            break
        
def addProduct():
    productCategory=input('Enter product category(FRUITS/COSMETICS/BOOKS): ')
    if productCategory.upper()=='FRUITS':
        addFruits()
    elif productCategory.upper()=='COSMETICS':
        addCosmetics()
    elif productCategory.upper()=='BOOKS':
        addBooks()
    else:
        print('Invalid input. Please re-enter your choice correctly.')
        return addProduct()
        
def addFruits():
    f=open(fruitsf,"ab")
    n=int(input("Enter no. of different types of fruits to be added: "))
    for i in range(n):
        batchNoF=int(input("Enter batch number: "))
        nameF=input("Enter name of fruit: ")
        priceF=float(input("Enter the price of the fruit per kg: "))
        quantityF=int(input("Enter the quantity of the fruit: "))
        descF=input("Enter description of the fruit: ")
        L=[batchNoF,nameF,priceF,quantityF,descF]
        pickle.dump(L,f)
        
    f.close()
    print('Fruit(s) added successfully.')
    print('*************************************')

def fruitsAdded():#for us
    fruitsList=[]
    f=open(fruitsf, 'rb')
    try:
        while True:
            p=pickle.load(f)
            fruitsList.append(p)
    except EOFError:
        pass
    f.close()
    return fruitsList


def addCosmetics():
    f=open(cosmeticsf,"wb")
    n=int(input("Enter no. of different types of cosmetics to be added:"))
    for i in range(n):
        batchNoC=int(input("Enter batch number: "))
        nameC=input("Enter name of cosmetic: ")
        priceC=float(input("Enter the price of the cosmetic: "))
        quantityC=int(input("Enter the quantity of the cosmetic: "))
        descC=input("Enter description of the cosmetic: ")
        L=[batchNoC,nameC,priceC,quantityC,descC]
        pickle.dump(L,f)
    f.close()  
    print('Cosmetic(s) added successfully.')
    print('*************************************')

def cosmeticsAdded():#for us
    cosmeticsList=[]
    f=open(cosmeticsf, 'rb')
    try:
        while True:
            p=pickle.load(f)
            cosmeticsList.append(p)
    except EOFError:
        pass
    f.close()
    return cosmeticsList

    
def addBooks():
    f=open(booksf,"wb")
    n=int(input("Enter no. of different types of books to be added:"))
    for i in range(n):
        batchNoB=int(input("Enter book id: "))
        nameB=input("Enter name of the book and its author: ")
        priceB=float(input("Enter the price of the book: "))
        quantityB=int(input("Enter the quantity of the book: "))
        descB=input("Enter description of the book: ")
        L=[batchNoB,nameB,priceB,quantityB,descB]
        pickle.dump(L,f)
    f.close()
        
    print('Book(s) added successfully.')
    print('*************************************')

def booksAdded():#for us
    booksList=[]
    f=open(booksf, 'rb')
    try:
        while True:
            p=pickle.load(f)
            booksList.append(p)
    except EOFError:
        pass
    f.close()
    return booksList


def updateQ():
    productCategory=input('Enter product category to be updated(FRUITS/COSMETICS/BOOKS): ')
    if productCategory.upper()=='FRUITS':
        updateFruitsQ()
    elif productCategory.upper()=='COSMETICS':
        updateCosmeticsQ()
    elif productCategory.upper()=='BOOKS':
        updateBooksQ()

def updateFruitsQ():
    f=open(fruitsf,"rb+")
    batchNoF=int(input("Enter batch number: "))
    try:
        while True:
            pos=f.tell()
            L=pickle.load(f)
            if L[0]==batchNoF:
                L[3]=int(input("Enter new stock quantity:"))
                f.seek(pos)
                pickle.dump(L,f)
                break
        print("Fruit(s) stock updated successfully")
        print('*************************************')
    except EOFError:
        print("Record not found")
    f.close()
    


def updateCosmeticsQ():
    f=open(cosmeticsf,"rb+")
    batchNoC=int(input("Enter batch number: "))
    try:
        while True:
            pos=f.tell()
            L=pickle.load(f)
            if L[0]==batchNoC:
                L[3]=int(input("Enter new stock quantity:"))
                f.seek(pos)
                pickle.dump(L,f)
                break
        print("Cosmetic(s) stock updated successfully")
        print('*************************************')
    except EOFError:
        print("Record not found")
    f.close()

def updateBooksQ():
    f=open(booksf,"rb+")
    batchNoB=int(input("Enter book id: "))
    try:
        while True:
            pos=f.tell()
            L=pickle.load(f)
            if L[0]==batchNoB:
                L[3]=int(input("Enter new stock quantity:"))
                f.seek(pos)
                pickle.dump(L,f)
                break
        print("Book(s) stock updated successfully")
        print('*************************************')
    except EOFError:
        print("Record not found")
    f.close()
    
def updateP():
    productCategory=input('Enter product category to be updated(FRUITS/COSMETICS/BOOKS): ')
    if productCategory.upper()=='FRUITS':
        updateFruitsP()
    elif productCategory.upper()=='COSMETICS':
        updateCosmeticsP()
    elif productCategory.upper()=='BOOKS':
        updateBooksP()

def updateFruitsP():
    f=open(fruitsf,"rb+")
    batchNoF=int(input("Enter batch number: "))
    try:
        while True:
            pos=f.tell()
            L=pickle.load(f)
            if L[0]==batchNoF:
                L[2]=input("Enter new price:")
                f.seek(pos)
                pickle.dump(L,f)
                break
        print("Fruit price updated successfully")
        print('*************************************')
    except EOFError:
        print("Record not found")
    f.close()
    


def updateCosmeticsP():
    f=open(cosmeticsf,"rb+")
    batchNoC=int(input("Enter batch number: "))
    try:
        while True:
            pos=f.tell()
            L=pickle.load(f)
            if L[0]==batchNoC:
                L[2]=input("Enter new price:")
                f.seek(pos)
                pickle.dump(L,f)
                break
        print("Cosmetic price updated successfully")
        print('*************************************')
    except EOFError:
        print("Record not found")
    f.close()


def updateBooksP():
    f=open(booksf,"rb+")
    batchNoB=int(input("Enter book id: "))
    try:
        while True:
            pos=f.tell()
            L=pickle.load(f)
            if L[0]==batchNoB:
                L[2]=input("Enter new price:")
                f.seek(pos)
                pickle.dump(L,f)
                break
        print("Book price updated successfully")
        print('*************************************')
    except EOFError:
        print("Record not found")
    f.close()

def updateDesc():
    productCategory=input('Enter product category to be updated(FRUITS/COSMETICS/BOOKS): ')
    if productCategory.upper()=='FRUITS':
        updateFruitsDesc()
    elif productCategory.upper()=='COSMETICS':
        updateCosmeticsDesc()
    elif productCategory.upper()=='BOOKS':
        updateBooksDesc()
        

def updateFruitsDesc():
    f=open(fruitsf,"rb+")
    batchNoF=int(input("Enter batch number: "))
    try:
        while True:
            pos=f.tell()
            L=pickle.load(f)
            if L[0]==batchNoF:
                L[4]=input("Enter new description:")
                f.seek(pos)
                pickle.dump(L,f)
                break
        print("Fruits description updated successfully")
        print('*************************************')
    except EOFError:
        print("Record not found")
    f.close()
    

def updateCosmeticsDesc():
    f=open(cosmeticsf,"rb+")
    batchNoC=int(input("Enter batch number: "))
    try:
        while True:
            pos=f.tell()
            L=pickle.load(f)
            if L[0]==batchNoC:
                L[4]=input("Enter new description:")
                f.seek(pos)
                pickle.dump(L,f)
                break
        print("Cosmetics description updated successfully")
        print('*************************************')
    except EOFError:
        print("Record not found")
    f.close()

def updateBooksDesc():
    f=open(booksf,"rb+")
    batchNoB=int(input("Enter book id: "))
    try:
        while True:
            pos=f.tell()
            L=pickle.load(f)
            if L[0]==batchNoB:
                L[4]=input("Enter new description:")
                f.seek(pos)
                pickle.dump(L,f)
                break
        print("Books description updated successfully")
        print('*************************************')
    except EOFError:
        print("Record not found")
    f.close()
    

#****************************************************************************************CUSTOMER PART***************************************************************************************

def customerChoice(cart):
    print('Following are the various products available from the categories- fruits, cosmetics and books: \n')
    print("%30s %30s %30s %30s %30s"%('Batch Number','Name of product','Price of product','Quantity available','Description'))
    print()
    fruitsBigList=fruitsAdded()
    cosmeticsBigList=cosmeticsAdded()
    booksBigList=booksAdded()
    for i in fruitsBigList:
        for j in i:
            print('%30s '%j, end='')
        print('\n')
    for i in cosmeticsBigList:
        for j in i:
            print('%30s '%j, end='')
        print('\n')
    for i in booksBigList:
        for j in i:
            print('%30s '%j, end='')
        print('\n')
                             
    
    while True:
        print('Select from the following options: ')
        print('1.Add products to the cart')
        print('2.Delete products from the cart')
        print('3.Display your cart')
        print('4.Go to checkout for payment')
        print('5.Exit')
        choice=int(input("Enter choice: "))
        print()
        if choice==1:
            addProductToCart()
        elif choice==2:
            if len(cart)==0:
                print('Your cart is empty!')
                print()
            else:
                deleteProductFromCart()
        elif choice==3:
            if len(cart)==0:
                print('Your cart is empty!')
            else:
                print(cart)
            print()
        elif choice==4:
            if len(cart)==0:
                print('0 products in cart. Payment not applicable.')
                print('Thank you for visiting! :)')
                break
            else:
                payment(cart)
                break
        else:
            print('Thank you for visiting! :)')
            break

def addProductToCart():
    productCategory=input('Enter category of product to be added(FRUITS/COSMETICS/BOOKS): ')
    if productCategory.upper()=='FRUITS':
        fruitsBigList=fruitsAdded()
        fruit=input('Enter fruit you want to add to the cart: ')
        try:
            while True:  
                fruitQ=int(input('Enter quantity required: '))
                try:
                    while True:
                        for i in fruitsBigList:
                            if i[1].lower()==fruit.lower():
                                if fruitQ<=i[3]:
                                    fruitSelected=i[:]
                                    fruitSelected[3]=fruitQ
                                    f=open(fruitsf,'wb')
                                    i[3]-=fruitQ
                                    print('Updated cart: ')
                                    cart.append(fruitSelected)
                                    print(cart)
                                    i=0
                                    while i<len(fruitsBigList):
                                        pickle.dump(fruitsBigList[i],f)
                                        i+=1
                                    print(fruitsBigList)
                                    f.close()
                                    break
                                else:
                                    print("Request exceeded existing stock quantity, enter another value")
                                    fruitQ=int(input('Enter quantity required: '))
                                    fruitSelected=i[:]
                                    fruitSelected[3]=fruitQ
                                    f=open(fruitsf,'wb')
                                    i[3]-=fruitQ
                                    print('updated cart: ')
                                    cart.append(fruitSelected)
                                    print(cart)
                                    i=0
                                    while i<len(fruitsBigList):
                                        pickle.dump(fruitsBigList[i],f)
                                        i+=1
                                    f.close()
                                    break
                        break
                    break
                except EOFError:
                    pass
        except EOFError:
            pass        
        
        print('Product added to cart.')
        print()
        
        
    elif productCategory.upper()=='COSMETICS':
        cosmeticsBigList=cosmeticsAdded()
        print('cosmeticsBigList: ',cosmeticsBigList)
        cosmetic=input('Enter cosmetic you want to add to the cart: ')
        try:
            while True:  
                cosmeticQ=int(input('Enter quantity required: '))
                try:
                    while True:
                        for i in cosmeticsBigList:
                            if i[1].lower()==cosmetic.lower():
                                if cosmeticQ<=i[3]:
                                    cosmeticSelected=i[:]
                                    cosmeticSelected[3]=cosmeticQ
                                    f=open(cosmeticsf,'wb')
                                    i[3]-=cosmeticQ
                                    print('Updated Cart: ')
                                    cart.append(cosmeticSelected)
                                    print(cart)
                                    i=0
                                    while i<len(cosmeticsBigList):
                                        pickle.dump(cosmeticsBigList[i],f)
                                        i+=1
                                    f.close()
                                    break
                                else:
                                    print("Request exceeded existing stock quantity, enter another value.")
                                    cosmeticQ=int(input('Enter quantity required: '))
                                    cosmeticSelected=i[:]
                                    cosmeticSelected[3]=cosmeticQ
                                    f=open(cosmeticsf,'wb')
                                    i[3]-=cosmeticQ
                                    print('Updated cart: ')
                                    cart.append(cosmeticSelected)
                                    print(cart)
                                    i=0
                                    while i<len(cosmeticsBigList):
                                        pickle.dump(cosmeticsBigList[i],f)
                                        i+=1
                                    f.close()
                                    break
                        break
                    break
                except EOFError:
                    pass
        except EOFError:
            pass        
        
        print('Product added to cart.')
        print()
        
    elif productCategory.upper()=='BOOKS':
        booksBigList=booksAdded()
        book=input('Enter book you want to add to the cart: ')
        try:
            while True:  
                bookQ=int(input('Enter quantity required: '))
                try:
                    while True:
                        for i in booksBigList:
                            if i[1].lower()==book.lower():
                                if bookQ<=i[3]:
                                    bookSelected=i[:]
                                    bookSelected[3]=bookQ
                                    f=open(booksf,'wb')
                                    i[3]-=bookQ
                                    print('Updated Cart: ')
                                    cart.append(bookSelected)
                                    print(cart)
                                    i=0
                                    while i<len(booksBigList):
                                        pickle.dump(booksBigList[i],f)
                                        i+=1
                                    f.close()
                                    break
                                else:
                                    print("Request exceeded existing stock quantity, enter another value.")
                                    bookQ=int(input('Enter quantity required: '))
                                    bookSelected=i[:]
                                    bookSelected[3]=bookQ
                                    f=open(booksf,'wb')
                                    i[3]-=bookQ
                                    print('Updated Cart: ')
                                    cart.append(bookSelected)
                                    print(cart)
                                    i=0
                                    while i<len(booksBigList):
                                        pickle.dump(booksBigList[i],f)
                                        i+=1
                                    f.close()
                                    break
                        break
                    break
                except EOFError:
                    pass
        except EOFError:
            pass        
        
        print('Product added to cart.')
        print()
    else:
        print('Invalid input. Please re-enter your choice correctly.')
        return addProductToCart()


def deleteProductFromCart():
    print(cart)
    productCategory=input('Enter category of product to be deleted(FRUITS/COSMETICS/BOOKS): ')
    if productCategory.upper()=='FRUITS':
        fruitsBigList=fruitsAdded()
        fruit=input('Enter fruit you want to delete from the cart: ')
        try:
            while True:  
                fruitQ=int(input('Enter quantity to be deleted: '))
                try:
                    while True:
                        for i in range(0,len(cart)):
                            if cart[i][1].lower()==fruit.lower():
                                while fruitQ>cart[i][3]:
                                    fruitQ=int(input('Quantity exceeded than cart quantity! Re-enter quantity to be deleted: '))
                                cart[i][3]-=fruitQ
                                if cart[i][3]==0:
                                    cart.remove(cart[i])
                                for k in fruitsBigList:
                                    if k[1].lower()==fruit.lower():
                                        f=open(fruitsf,'wb')
                                        k[3]+=fruitQ
                                        j=0
                                        while j<len(fruitsBigList):
                                            pickle.dump(fruitsBigList[j],f)
                                            j+=1
                                        print(fruitsBigList)
                                        f.close()
                                        break
                                print('Updated cart: ')
                                print(cart)
                                break
                            break
                        break
                    break
                except EOFError:
                    pass
        except EOFError:
            pass        
        
        print('Product deleted from cart.')
        print()
        
        
    elif productCategory.upper()=='COSMETICS':
        cosmeticsBigList=cosmeticsAdded()
        cosmetic=input('Enter cosmetic you want to delete from the cart: ')
        try:
            while True:  
                cosmeticQ=int(input('Enter quantity to be deleted: '))
                try:
                    while True:
                        for i in range(0,len(cart)):
                            if cart[i][1].lower()==cosmetic.lower():
                                while cosmeticQ>cart[i][3]:
                                    cosmeticQ=int(input('Quantity exceeded than cart quantity! Re-enter quantity to be deleted: '))
                                cart[i][3]-=cosmeticQ
                                if cart[i][3]==0:
                                    cart.remove(cart[i])
                                for k in cosmeticsBigList:
                                    if k[1].lower()==cosmetic.lower():
                                        f=open(cosmeticsf,'wb')
                                        k[3]+=cosmeticQ
                                        j=0
                                        while j<len(cosmeticsBigList):
                                            pickle.dump(cosmeticsBigList[j],f)
                                            j+=1
                                        print(cosmeticsBigList)
                                        f.close()
                                        break
                                print('Updated cart: ')
                                print(cart)
                                break
                            break
                        break
                    break
                except EOFError:
                    pass
        except EOFError:
            pass                
        
        print('Product deleted from cart.')
        print()
        
    elif productCategory.upper()=='BOOKS':
        booksBigList=booksAdded()
        book=input('Enter book you want to delete from the cart: ')
        try:
            while True:  
                bookQ=int(input('Enter quantity to be deleted: '))
                try:
                    while True:
                        for i in range(0,len(cart)):
                            if cart[i][1].lower()==book.lower():
                                while bookQ>cart[i][3]:
                                    bookQ=int(input('Quantity exceeded than cart quantity! Re-enter quantity to be deleted: '))
                                cart[i][3]-=bookQ
                                if cart[i][3]==0:
                                    cart.remove(cart[i])
                                for k in booksBigList:
                                    if k[1].lower()==book.lower():
                                        f=open(booksf,'wb')
                                        k[3]+=bookQ
                                        j=0
                                        while j<len(booksBigList):
                                            pickle.dump(booksBigList[j],f)
                                            j+=1
                                        print(booksBigList)
                                        f.close()
                                        break
                                print('Updated cart: ')
                                print(cart)
                                break
                            break
                        break
                    break
                except EOFError:
                    pass
        except EOFError:
            pass
        print('Product deleted from cart.')
        print()  
        
    else:
        print('Invalid input. Please re-enter your choice correctly.')
        return deleteProductFromCart()
    


def payment(cart):
    print('***********************************************************  RECEIPT *********************************************************************')
    print("%30s %30s %30s %30s"%('Name of product','Quantity','Price of product','Total'))
    print()
    total=0
    billAmt=0
    for i in cart:
        totalCost=i[3]*i[2]
        total+=totalCost
        tax=totalCost*5/100
        billAmt+=totalCost+tax
        
    for i in cart:
        print('%30s %30s %30s %30s'%(i[1],i[3],i[2],i[3]*i[2]))

    print('Total amount: ',total)
    print('Total amount required to be paid inclusive of tax: ',billAmt)
    print('Thankyou for shopping with us. Your products will be delivered soon. ')



    
#*************************************************************************************LOGIN AND SIGN UP*************************************************************************************

def loginCustomer():
    print('Please enter your login details: ')
    customerUsername=input('Enter your username: ')
    customerPw=input('Enter your password: ')
    f=open(fn,'rb')
    try:
        while True:
            l=pickle.load(f)
            if l[0]==customerUsername:
                if l[1]==customerPw:
                    print('Login successful')
                    f.close()
                    print('*************************************')
                    break
                else:
                    print('Login Unsuccessful, please re-enter your password: ')
                    customerPw=input('Enter your password: ')
                    try:
                        while True:
                            if l[1]==customerPw:
                                print('Login successful')
                                f.close()
                                print('*************************************')
                                break
                            else:
                                print('Login Unsuccessful')
                                print('*************************************')
                                f.close()
                                break
                    except EOFError:
                        pass
                    break
    except EOFError:
        pass

    
                
def appendCustomer():
    f=open(fn, 'ab+')
    print('Please enter your details: ')
    customerUsername=input('Enter username: ')
    customerPw=input('Enter password: ')
    customerEmail=input('Enter your email: ')
    customerContact=input('Enter your contact number: ')
    customerAddress=input('Enter your delivery address: ')
    l=[customerUsername, customerPw, customerEmail, customerContact, customerAddress]
    pickle.dump(l,f)
    f.close()
    print('Customer account added successfully')
    print('*************************************')
    cart=[]


    
def loginAdmin():
    print('Please enter your login details: ')
    adminUsername=input('Enter your username: ')
    adminPwEntered=input('Enter admin password: ')
    if adminPwEntered!=adminPw:
        print('Login Unsuccessful.')
        loginAdmin()
    else:
        print('Login successful.')
        print('*************************************')


adminPw='comp123'
filename='DynamicShopping.dat'
fn='Customer.dat'
fruitsf='fruits.dat'
cosmeticsf='cosmetics.dat'
booksf='books.dat'
cart=[]

while True:
    print('Welcome to Dynamic Shopping!')
    userType=input('Are you an admin or customer?(a/c): ')
    if userType.lower()=='a':
        loginAdmin()
        val=adminChoice()
        if val=='Exit':
            break
    elif userType.lower()=='c':
        accountExists=input('Do you have an existing account?(y/n): ')
        if accountExists.lower()=='n':
            appendCustomer()
            customerChoice(cart)
            break
        elif accountExists.lower()=='y':
            loginCustomer()
            customerChoice(cart)
            break
        else:
            print('Please re-enter your choice(y/n)')
            accountExists=input('Do you have an existing account?(y/n): ')
            print()
            if accountExists.lower()=='n':
                appendCustomer()
                customerChoice(cart)
                break
            elif accountExists.lower()=='y':
                loginCustomer()
                customerChoice(cart)
                break
    else:
        print('Invalid input. Exiting Dynamic Shopping.')
        break

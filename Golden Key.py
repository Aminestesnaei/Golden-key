import csv
from hashlib import sha224 , sha384 , sha512 , md5 , sha256


def num_gen():
    x = int(input("0000 to "))
    with open('hashpass/Num Hashed.csv', 'a',newline='', encoding='UTF8') as f:
        writer = csv.writer(f,delimiter=':')
        passhash = ["Pass","Hash"]
        writer.writerow(passhash)
        for i in range(x):
            pas = str(i)
            in_pass = pas.encode()
            out_pass = sha256(in_pass).hexdigest()
            out_pass.rstrip()
            to_csv = [i,out_pass]
            
            writer.writerow(to_csv)
            print(i, out_pass)

    print("Done")
    main()


def hash_gen():
       
    print("Select one of this option \n (1) Generate number password \n (2) Generate my password's to hash  ")
    option = input("")

    if option == "1":
        num_gen()
    elif option == "2":
        sha_gen()

    else:
        print("just insert number and press Enter")
        pass


def pass_to_hash_256():
    fin = input("Insert File Path \n")

    with open(fin,'r') as paslist:
        reader = csv.reader(paslist)
        for row in reader:
            if row:

                word = row[0]

                hash_obj = sha256(word.encode())
                hex_dig = hash_obj.hexdigest()
                out_put = [[word,hex_dig]]
                print(out_put)
                with open("hashpass/pass hashed 256.csv" , mode='a' ,newline='') as f:
                    writer = csv.writer(f,delimiter=':')
                    for inner_pass in out_put:
                        writer.writerow(inner_pass)




                    f.close()
        main()               


def pass_to_hash_224():

    fin = input("Insert File Path \n")

    with open(fin,'r') as paslist:
        reader = csv.reader(paslist)
        for row in reader:
            if row:

                word = row[0]

                hash_obj = sha224(word.encode())
                hex_dig = hash_obj.hexdigest()
                out_put = [[word,hex_dig]]
                print(out_put)
                with open("hashpass/pass hashed 224.csv" , mode='a' ,newline='') as f:
                    writer = csv.writer(f,delimiter=':')
                    for inner_pass in out_put:
                        writer.writerow(inner_pass)

                    f.close()
        main()


def pass_to_hash_384():
    fin = input("Insert File Path \n")

    with open(fin,'r') as paslist:
        reader = csv.reader(paslist)
        for row in reader:
            if row:

                word = row[0]

                hash_obj = sha384(word.encode())
                hex_dig = hash_obj.hexdigest()
                out_put = [[word,hex_dig]]
                print(out_put)
                with open("hashpass/pass hashed 384.csv" , mode='a' ,newline='') as f:
                    writer = csv.writer(f,delimiter=':')
                    for inner_pass in out_put:
                        writer.writerow(inner_pass)

                    f.close()
        main()


def pass_to_hash_512():
    fin = input("Insert File Path \n")

    with open(fin,'r') as paslist:
        reader = csv.reader(paslist)
        for row in reader:
            if row:

                word = row[0]

                hash_obj = sha512(word.encode())
                hex_dig = hash_obj.hexdigest()
                out_put = [[word,hex_dig]]
                print(out_put)
                with open("hashpass/pass hashed 512.csv" , mode='a' ,newline='') as f:
                    writer = csv.writer(f,delimiter=':')
                    for inner_pass in out_put:
                        writer.writerow(inner_pass)

                    f.close()
        main()


def pass_to_hash_md5():
    fin = input("Insert File Path \n")

    with open(fin,'r') as paslist:
        reader = csv.reader(paslist)
        for row in reader:
            if row:

                word = row[0]

                hash_obj = md5(word.encode())
                hex_dig = hash_obj.hexdigest()
                out_put = [[word,hex_dig]]
                print(out_put)
                with open("hashpass/pass hashed md5.csv" , mode='a' ,newline='') as f:
                    writer = csv.writer(f,delimiter=':')
                    for inner_pass in out_put:
                        writer.writerow(inner_pass)

                    f.close()
        main()


def sha_gen():
    s = input("Choose one of these methods\n (1) sha256\n (2) sha224\n (3) sha384\n (4) sha512\n (5) md5\n")

    if s == "1":
        pass_to_hash_256()

    elif s == "2":
        pass_to_hash_224()

    elif s == "3":
        pass_to_hash_384()

    elif s =="4":
        pass_to_hash_512()

    elif s == "5":
        pass_to_hash_md5()
    

def read_hash():
    fin = input("Insert File Path \n")
    with open(fin, 'r') as f:
        pass_hash = csv.reader(f, delimiter=':', quotechar='|')
        for row in pass_hash:
            print(':'.join(row))
    main()


def find_hash():
    fin = input("Insert The dictionary Path \n")

    search = input("Insert The Hash \n")
    
    with open(fin , 'r') as csvfile :
        reader = csv.reader(csvfile)

        for line in reader:
            if search in line[0]:
                print(line[0])
        main()


print("wellcome to has pass \n just select a option :)")
def main():
    print("(1) hash generator\n(2) read dictionary\n(3) find pass from dictionary")
    sel = input("")
    if sel == "1":
        hash_gen()
    elif sel == "2":
        read_hash()
    elif sel == "3":
        find_hash()
    else:
        print("just type the number then touch Enter :)")
        main()


main()

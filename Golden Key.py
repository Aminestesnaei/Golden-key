import csv
from hashlib import sha256


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




def pass_to_hash():
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
                with open("hashpass/pass hashed.csv" , mode='a' ,newline='') as f:
                    writer = csv.writer(f,delimiter=':')
                    for inner_pass in out_put:
                        writer.writerow(inner_pass)




                    f.close()





def hash_gen():
       
    print("Select one of this option \n (1) Generate number password \n (2) Generate my password's to hash  ")
    option = input("")

    if option == "1":
        num_gen()
    elif option == "2":
        pass_to_hash()

    else:
        print("just insert number and press Enter")
        pass




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
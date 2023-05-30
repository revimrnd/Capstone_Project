import sys
import pyinputplus as pps


# Menu menampilkan material
def display():
    while True:
    #  Sub menu display
        titleD = f'\n--- Display Material\n'
        menuDisplay = ['All','Material','Distribution','Back']
        prompt1 = pps.inputMenu(
        prompt=titleD, choices=menuDisplay, numbered=True)
        if prompt1 == 'All': 
            print('\n Available Material')
            template()
        elif prompt1 == 'Material':
            findM = input('Find the material: ')
            if findM.lower() not in listMaterial.keys():
                print('Material does not exist')
            for key in listMaterial.keys():
                if findM.lower() in listMaterial[key]['Material'].lower():
                    print('\nCode \t|Material \t |Inventory |Distribution |Supplier\n')
                    print('{} \t|{} \t\t |{} \t    |{}   \t  |{}'.format(listMaterial[key]['Code'],listMaterial[key]['Material'],
                        listMaterial[key]['Inventory'],listMaterial[key]['Distribution'],listMaterial[key]['Supplier']))
                else:
                    continue
        elif prompt1 == 'Distribution':
            findD = input('Find the distribution: ')
            if findD.lower() not in listMaterial.keys():
                print('Material does not exist')
            for key in listMaterial.keys():
                if findD.lower() in listMaterial[key]['Distribution'].lower():
                    print('\nCode \t|Material \t |Inventory |Distribution |Supplier\n')
                    print('{} \t|{} \t\t |{} \t    |{}   \t  |{}'.format(listMaterial[key]['Code'],listMaterial[key]['Material'],
                        listMaterial[key]['Inventory'],listMaterial[key]['Distribution'],listMaterial[key]['Supplier']))
                else:
                    continue
        elif prompt1 == 'Back':
            main()
                 
   
# Menu penambahan data   
def add():
    while True:
        # Sub menu add
        titleA = f'\n--- Add Material\n'
        menuAdd = ['Adding', 'Back']
        prompt2 = pps.inputMenu(
        prompt=titleA, choices=menuAdd, numbered=True)
        if prompt2 == 'Adding':
            inputMaterial = (input('Enter the material: '))
            newInputM = inputMaterial.replace(' ','')
            if newInputM.lower() not in listMaterial.keys():
                print('Please fill in the new data')
                newCode = str(input('Enter the code: '))
                newMaterial = str(input('Enter the material: '))
                newInventory = int(input('Enter the inventory amount: '))
                newDistribution = str(input('Enter the distribution plant: '))
                newSupplier = str(input('Enter the supplier: '))
                check = input(f'Are you sure want to add the new data = {newCode}, {newMaterial}, {newInventory}, {newDistribution}, {newSupplier} (Y/N): ')
                if check != 'Y':
                    print('New data has denied')
                    continue
                else:
                    listMaterial[newInputM.lower()] = {'Code':newCode,'Material':newMaterial,'Inventory':newInventory,'Distribution':newDistribution,'Supplier':newSupplier}
                    template()
                    print('New data has saved')
                    continue
            else:
                print('Data already exist')
        elif prompt2 == 'Back':
            main()


# Menu memperbarui data
def renew():
    # Sub menu renew
    titleR = f'\n--- Renew Material\n'
    menuRenew = ['Update', 'Back']
    prompt3 = pps.inputMenu(
        prompt=titleR, choices=menuRenew, numbered=True)
    if prompt3 == 'Update':
        template()
        updateM = str(input('Please, enter the material you want to update: '))
        newUpdate = updateM.replace(' ','')
        while newUpdate.lower() in listMaterial.keys():
            # Pilihan menu update berdasarkan kategori
            titleU = f'\n- Update Category\n'
            askCategory = ['Code','Material','Inventory','Distribution','Supplier','Back']
            prompt4 = pps.inputMenu(
                prompt=titleU, choices=askCategory, numbered=True)
            if prompt4 == 'Code':
                inpNewCode = str(input('Update the code: '))
                checkCode = str(input('Are you want to update?(Y/N)'))
                if checkCode != 'Y':
                    continue
                else:
                    listMaterial[newUpdate.lower()]['Code'] = inpNewCode
                    template()
                    print('Code has been updated')
                    continue
            elif prompt4 == 'Material':
                inpNewMaterial = str(input('Update the material: '))
                newMatUpdate = inpNewMaterial.replace(' ','')
                while newMatUpdate.lower() in listMaterial.keys():
                    print('Material already exist')
                    inpNewMaterial = str(input('Update the material: '))
                    newMatUpdate = inpNewMaterial.replace(' ','')
                checkMaterial = str(input('Are you want to update?(Y/N)'))
                if checkMaterial != 'Y':
                    continue
                else:
                    listMaterial[newMatUpdate] = listMaterial[newUpdate.lower()]
                    del listMaterial[newUpdate.lower()]
                    listMaterial[newMatUpdate]['Material'] = inpNewMaterial
                    template()
                    print('Material has been updated')
                    continue
            elif prompt4 == 'Inventory':
                inpNewInventory = int(input('Update the inventory: '))
                checkInventory = str(input('Are you want to update?(Y/N)'))
                if checkInventory != 'Y':
                    continue
                else:
                    listMaterial[newUpdate.lower()]['Inventory'] = inpNewInventory
                    template()
                    print('Inventory has been updated')
                    continue
            elif prompt4 == 'Distribution':
                inpNewDistribution = str(input('Update the distribution: '))
                checkDistribution = str(input('Are you want to update?(Y/N)'))
                if checkDistribution != 'Y':
                    continue
                else:
                    listMaterial[newUpdate.lower()]['Code'] = inpNewDistribution
                    template()
                    print('Distribution has been updated')
                    continue
            elif prompt4 == 'Supplier':
                inpNewSupplier = str(input('Update the supplier: '))
                checkSupplier = str(input('Are you want to update?(Y/N)'))
                if checkSupplier != 'Y':
                    continue
                else:
                    listMaterial[newUpdate.lower()]['Supplier'] = inpNewSupplier
                    template()
                    print('Supplier has been updated')
                    continue
            elif prompt4 == 'Back':
                renew()
    elif prompt3 == 'Back':
        main()


# Menu penghapusan data
def clear():
    # Sub menu clear
    while True:
        titleC = f'\n--- Clear Material\n'
        menuClear = ['Delete', 'Back']
        prompt5 = pps.inputMenu(
            prompt=titleC, choices=menuClear, numbered=True)
        if prompt5 == 'Delete':
            template()
            delMaterial = str(input('Enter the material you wish to delete: '))
            newDelMat = delMaterial.replace(' ','')
            while newDelMat.lower() not in listMaterial.keys():
                print('Material does not exist')
                break
            else:
                checkClear = str(input(f'Are you sure wish to delete {delMaterial}?(Y/N)'))
                while checkClear != 'Y':
                    print('Failed to delete')
                    break
                else:
                    del listMaterial[newDelMat.lower()]
                    template()
                    print('Success for deleting')
        elif prompt5 == 'Back':
            main()


# Menu penjadwalan 
def schedule():
    # Sub menu schedule
    while True:
        titleS = f'\n--- Schedule Material\n'
        menuSchedule = ['Production','Purchasing','Back']
        prompt6 = pps.inputMenu(
            prompt=titleS, choices=menuSchedule, numbered=True)
        if prompt6 == 'Production':
            print('Please input the data for scheduling')
            matP = str(input('Material: '))
            invP = int(input('Inventory: '))
            disP = str(input('Distribution: '))
            schP = str(input('Date: '))
            print(f'\nHere is your production schedule\n{matP}\n{invP}\n{disP}\n{schP}')
            checkPd = str(input('Are you sure want to confirm the schedule?(Y/N)'))
            while checkPd != 'Y':
                print('Failed to confirm')
                continue
            else:
                print('Success for confirming')
        elif prompt6 == 'Purchasing':
            print('Please input the data for scheduling')
            matPur = str(input('Material: '))
            invPur = int(input('Inventory: '))
            supPur = str(input('Supplier: '))
            schPur = str(input('Date: '))
            print(f'\nHere is your purchasing schedule\n{matPur}\n{invPur}\n{supPur}\n{schPur}')
            checkPur = str(input('Are you sure want to confirm the schedule?(Y/N)'))
            while checkPur != 'Y':
                print('Failed to confirm')
                continue
            else:
                print('Success for confirming')
        elif prompt6 == 'Back':
            main()


# Fungsi template daftar material
def template():
    if len(listMaterial) == 0:
        print('\n Material unavailable')
    else:
        print('\n______________________ List Material _____________________\n')
        print('Code \t|Material \t |Inventory |Distribution |Supplier\n')
        for key in listMaterial.keys():
            print('{} \t|{} \t\t |{} \t    |{}   \t  |{}'.format(listMaterial[key]['Code'],listMaterial[key]['Material'],
                listMaterial[key]['Inventory'],listMaterial[key]['Distribution'],listMaterial[key]['Supplier']))


# Menu utama sistem
def main():
    while True:
        # Tampilan title
        titleM = f'\nMaterial Management System\n'
        # Pilihan menu utama 
        menu = ['Display','Add','Renew','Clear','Schedule','Exit']
        user = pps.inputMenu(
            prompt=titleM, choices=menu, numbered=True)
        # Untuk menampilkan data
        if user == 'Display':
            display()
        # Untuk menambah data 
        elif user == 'Add':
            add()
        # Untuk mengupdate data baru
        elif user == 'Renew':
            renew()
        # Untuk menghapus data
        elif user == 'Clear':
            clear()
        # Untuk mengupdate data baru
        elif user == 'Schedule':
            schedule()
        # Untuk keluar dari sistem
        sys.exit()


if __name__ == "__main__":
    listMaterial = {
    'pipe' : {'Code':'A01','Material':'Pipe','Inventory':333,'Distribution':'Plant A','Supplier':'Pipecorp'},
    'fluid' : {'Code':'B02','Material':'Fluid','Inventory':666,'Distribution':'Plant B','Supplier':'Fluidline'},
    'wire' : {'Code':'C03','Material':'Wire','Inventory':999,'Distribution':'Plant B','Supplier':'Wirego'},
    'steel' : {'Code':'D04','Material':'Steel','Inventory':369,'Distribution':'Plant C','Supplier':'Histeel'},
    'paint' : {'Code':'E05','Material':'Paint','Inventory':963,'Distribution':'Plant D', 'Supplier':'Thecoat'}
    }
    main()










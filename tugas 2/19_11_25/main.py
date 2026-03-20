import pandas as pd
import os
import inquirer

def cls():
    os.system('cls || clear')

def choises():
    menu = [
        'angkatan dan prodi',
        'angkatan dan fakultas',
        'aggregate',
        'count',
        'size',
        'quit'
    ]
    questions = [
        inquirer.List(
            'menu',
            message="Pilih Menu:",
            choices=menu,
            carousel=True
        ),
    ]
    answers = inquirer.prompt(questions)
    return answers['menu']

def search_angkatan():
    cls()
    angkatan = [
        2022,
        2023,
        2024,
        2025
    ]
    questions = [
        inquirer.List(
            'search',
            message="Pilih Angkatan:",
            choices=angkatan,
            carousel=True
        ),
    ]
    answers = inquirer.prompt(questions)
    return answers['search']

def search_fakultas():
    cls()
    fakultas = [
        'teknik',
        'ekonomi'
    ]
    questions = [
        inquirer.List(
            'search',
            message="Pilih fakultas:",
            choices=fakultas,
            carousel=True
        ),
    ]
    answers = inquirer.prompt(questions)
    return answers['search']


def search_prodi():
    cls()
    prodi = [
        'informatika',
        'sistem informasi',
        'elektro',
        'manajemen',
        'akuntansi'
    ]
    questions = [
        inquirer.List(
            'search',
            message="Pilih Prodi:",
            choices=prodi,
            carousel=True
        ),
    ]
    answers = inquirer.prompt(questions)
    return answers['search']

def main():
    while True:
        cls()
        df = pd.read_csv(r'D:\Kuliah\matkul\APD\tugas\19_11_25\data.csv')
        choise = choises()
        if choise == 'angkatan dan prodi':
            angkatan = search_angkatan()
            prodi = search_prodi()
            group = df.groupby(['angkatan', 'prodi'])
            grouped_data = {name : data for name, data in group}
            cls()
            print(grouped_data[(angkatan, prodi)])
            input('< kembali(enter)')

        elif choise == 'angkatan dan fakultas':
            angkatan = search_angkatan()
            fakultas = search_fakultas()
            group = df.groupby(['angkatan', 'fakultas'])
            grouped_data = {name : data for name, data in group}
            cls()
            print(grouped_data[(angkatan, fakultas)])
            input('< kembali(enter)')
        elif choise == 'aggregate':
            cls()
            group = df.groupby(['angkatan','prodi'])
            print(group.agg({'ipk' : ['mean', 'max', 'min', 'sum', 'count']}))
            input('< kembali(enter)')
        elif choise == 'count':
            cls()
            group = df.groupby(['angkatan','prodi'])
            print(group.count())
            input('< kembali(enter)')
        elif choise == 'size':
            cls()
            group = df.groupby(['angkatan','prodi'])
            print(group.size())
            input('< kembali(enter)')
        elif choise == 'quit':
            break
        else:
            input('input tidak valid')

if __name__ == "__main__":
    main()
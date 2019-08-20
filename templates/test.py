import datetime
a=[{'nom': 'rtgh', 'prenom': 'feggeh', 'email': 'fgszgvjhknlfgharr@gmail.com', 'date_naissance': datetime.date(1995, 12, 2), 'id': 12}, 
{'id_clas': 7, 'montant_ins': '50000', 'mensualite': '30000', 'id_filiere': 3}, 
{'filiere': 'data_artisan'},[{'id_clas': 7, 'nom_classe': 'l1 art'}, {'id_clas': 8, 'nom_classe': 'l2 art'}, {'id_clas': 9, 'nom_classe': 'l3 art'}]]




for j,i in  enumerate(a):
    # print(i)
    if j==3:
        s=a[j]
        for j in s:
            print(j)
    else:
        print(i)
        [{'id': 1, 'libelle': 'l1 dev'}, {'id': 2, 'libelle': 'l2 dev'}, {'id': 3, 'libelle': 'l3 dev'}]
        [{'id_clas': 1, 'nom_classe': 'l1 dev'}, {'id_clas': 2, 'nom_classe': 'l2 dev'}, {'id_clas': 3, 'nom_classe': 'l3 dev'}]


# print(a[3])

# c={"a":"{'id_clas': 7, 'nom_classe': 'l1 art'}, {'id_clas': 8, 'nom_classe': 'l2 art'}, {'id_clas': 9, 'nom_classe': 'l3 art'}"}
#print(c['a'])
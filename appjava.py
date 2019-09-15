from flask import Flask,render_template,request,redirect,url_for,flash,session,jsonify,json
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
# from wtforms import SelectField
# from flask_wtf import FlaskForm
import datetime
import random
 

app = Flask(__name__)
# .
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Diop1957+@localhost/flaskalchemy'
app.config['SECRET_KEY'] = 'secret'
db = SQLAlchemy(app)
############################################  creation des tables#####################s#####################s#####################
                    ####################### etudiant#####################
class Etudiant(db.Model):
    __tablename__ = 'Etudiant'
    id= db.Column(db.Integer, primary_key=True,autoincrement=True)
    matricule = db.Column(db.String(100), unique=True,nullable = False)
    prenom = db.Column(db.String(200),nullable = False)
    nom = db.Column(db.String(200),nullable = False)
    email = db.Column(db.String(200),nullable = False)
    date_naiss = db.Column(db.Date)
     
    def __init__(self,matricule,prenom,nom,email,date_naiss):
        self.matricule =  matricule
        self.prenom = prenom
        self.nom = nom
        self.email = email
        self.date_naiss = date_naiss

    def __repr__(self):
        return '<Etudiant %r,%r,%r,%r,%r>'%(self.matricule,self.prenom,self.nom,self. email,self.date_naiss)  
####################### filiere#####################
class Filiere(db.Model):
    __tablename__ = 'Filiere'
    id= db.Column(db.Integer, primary_key=True,autoincrement=True)
    libelle = db.Column(db.String(200))

    def __init__(self,libelle):
        self.libelle =   libelle


    def __repr__(self):
        return '<Filiere %r>'% self.libelle     
#######################classe#####################       
class Classe(db.Model):
    __tablename__ = 'Classe'
    id= db.Column(db.Integer, primary_key=True,autoincrement=True)
    libelle = db.Column(db.String(200))
    montant_ins = db.Column(db.String(200))
    mensualite = db.Column(db.String(200))
    filiere_id=db.Column(db.Integer, db.ForeignKey('Filiere.id'))
    

    def __init__(self,libelle,montant_ins, mensualite,filiere_id):
        self.libelle = libelle
        self.montant_ins = montant_ins
        self.mensualite =  mensualite
        self.filiere_id =  filiere_id
        

    def __repr__(self):
        return '<Classe %r,%r,%r,%r>'% (self.libelle,self.montant_ins,self.mensualite,self.filiere_id)

#######################inscription#####################       
class Inscription(db.Model):
    __tablename__ = 'Inscription'
    id= db.Column(db.Integer, primary_key=True,autoincrement=True)
    annee_acade = db.Column(db.String(200))
    date_ins = db.Column(db.Date)
    classe_id=db.Column(db.Integer, db.ForeignKey('Classe.id'))
    Etudiant_id=db.Column(db.Integer, db.ForeignKey('Etudiant.id'),autoincrement=True) 
    

    def __init__(self,annee_acade,date_ins,classe_id,Etudiant_id):
        self.annee_acade = annee_acade
        self.date_ins = date_ins
        self.classe_id =  classe_id
        self.Etudiant_id =Etudiant_id
        

    def __repr__(self):
        return '<Inscription %r,%r,%r,%r>'% (self.annee_acade,self.classe_id,self.date_ins,self.Etudiant_id)      
############################################ formulaire ###############################################################
# class TestForm(FlaskForm):
#     Filiere = SelectField(u'', choices=())
#     Classe = SelectField(u'', choices=())

 
@app.route('/')
def accueil(): 
    #filiere
    posts_fili=Filiere.query.all()
    db.session.commit()

    # posts_clas=Classe.query.join(Filiere).all()
    # db.session.commit()
    # b=db.session.query(Classe.libelle,Filiere.id).outerjoin(Filiere,Filiere.id==Classe.filiere_id).all()
    # posts_clas=Classe.query.all()
    # db.session.commit()
    
    a=Etudiant.query.count()+1
    db.session.commit()
    #la requete pour la matricule
    
    resultat=db.session.query(func.max(Etudiant.id)).one()
    db.session.commit()

    date_actu=datetime.datetime.today().strftime("%d-%m-%Y")

    if resultat[0] == None:
        m = 1
        matricule="SA-"+str(date_actu)+"-"+str(m)
    else :
        m = resultat[0] +1
        matricule = "SA-"+str(date_actu)+"-"+str(m)

############################la requete pour la matricule autre methode

    # chaine="azertyxrtcuyiu12587902vyuQDEPMLIOYRZAVGFS"  
    # taille=10
    # matricule=""
    # while len(matricule)<taille:
    #     if len(matricule)==5:
    #         matricule=matricule+"-"
    #     else:
    #         matricule=matricule+random.choice(chaine)

    
    #la generation annne academique 
    mois_actu=int(datetime.datetime.today().strftime("%m"))
    année1=0
    année2=0
    annee_academy=None
    if mois_actu >= 8:
        année1 = int(datetime.datetime.today().strftime("%Y"))
        année2 = année1+1
        annee_academy = str(année1)+"-"+str(année2)
    else:
        année1=int(datetime.datetime.today().strftime("%Y"))
        année2=année1-1
        annee_academy=str(année2)+"-"+str(année1)


    return  render_template('formulaire.html',posts_fili=posts_fili,matricule=matricule,a=a,date_actu=date_actu,annee_academy=annee_academy)
 


@app.route('/insert',methods= ['POST'])
def insert():
    #controle_email
    email_requet=db.session.query(Etudiant.email).all()
    db.session.commit()
     
    Etudiant_id=request.form['etudiant_id']
    matricule=request.form['matricule']
    prenom=request.form['prenom'] 
    nom=request.form['nom'] 
    email=request.form['email']
    datenaissance = request.form['date']
    date_ins=request.form['date_ins']
    annee_acade=request.form['Annén']
    classe_id=int(request.form['classe'])
        
    # pour controler si l'email de l'apprenant existe deja

    control_promo=False
    for row in email_requet:
        if row[0].lower() == email.lower():
            control_promo =True
            break

    if control_promo == True  :
        flash("apprenant existe deja ")
        return redirect(url_for('accueil'))
    else:    
            
        post1 = Etudiant(matricule=matricule,prenom=prenom,nom=nom,email=email,date_naiss=datenaissance)

        db.session.add(post1)
        db.session.commit()

        post2 = Inscription(annee_acade=annee_acade,date_ins=date_ins,classe_id=classe_id,Etudiant_id=Etudiant_id)

        db.session.add(post2)
        db.session.commit()

        flash("SUCCESS : Apprenant ajouté avec succès!!!")
        return redirect(url_for('accueil'))
        
#---------------------------------- Relation entre filiére et classe -----------------------------------
@app.route('/listfiliere/<id>', methods = ['GET','POST'])
def listfiliere(id):
    # lister = db.session.query(Filiere.id,Classe.id,Classe.libelle,Filiere.libelle).outerjoin(Filiere,id == Classe.id).all()
    # lister=db.session.query(Classe.libelle,Filiere.id).outerjoin(Filiere,Filiere.id==Classe.filiere_id).all()
    lister=Classe.query.filter_by(filiere_id = id).all()

    tab = []
    # print(lister)
    for i in lister:
        cl = {}
        cl['id'] = i.id
        cl['libelle'] = i.libelle
        tab.append(cl)
        print(tab)
             
    return jsonify({'classe':tab})
    #print(classe)
#----------- Relation entre classe et les champs montant, mensualité et total inscription------------
@app.route('/listclasse/<id>', methods = ['GET','POST'])
def listclasse(id):
    lister_classe = Classe.query.filter_by(id = id).all()
    tab = []
    # print(lister_classe)
    for i in lister_classe:
        clsse = {"id":i.id, "montant_ins":i.montant_ins , "mensualite":i.mensualite }
        tab.append(clsse)
    print(tab)
       
    return jsonify({'classe':tab})
     

@app.route('/rechermat/<id_mat>')
def recherchemat(id_mat):
    # ###########jointure entre les quatres tables

    # jointure=db.session.query(Etudiant.id,Etudiant.matricule,Etudiant.nom,Etudiant.prenom,Classe.libelle,Filiere.libelle).j
    # oin(Inscription,Inscription.Etudiant_id==Etudiant.id).join(Classe,Classe.id==Inscription.classe_id).
    # join(Filiere,Filiere.id==Classe.filiere_id).filter(Etudiant.matricule== id_mat).all()

    # print(id_mat)
    lister= db.session.query(Etudiant).filter_by(matricule=id_mat).all()
    tab = []
    # print(lister)
    for i in lister:
        cl = {"nom":i.nom,"prenom":i.prenom , "email":i.email, "date_naissance":i.date_naiss,"id":i.id}
        tab.append(cl)
        # print(i.id)

        a=db.session.query(Inscription.classe_id).filter_by(Etudiant_id= i.id).all()
        # print(a)
        id_classe=a[0].classe_id
        # print(id_classe)    
        
        # requete pour afficher  tous dans la table classe \nom de la claase
        b=db.session.query(Classe).filter_by(id= id_classe).all()
        id_filiere=b[0].filiere_id
        id_clas=b[0].id
        montant_ins=b[0].montant_ins
        mensualite=b[0].mensualite
        nom_class=b[0]. libelle
        # print(id_filiere,id_clas,montant_ins,mensualite,nom_class)
        list_clas = {"id_clas":id_clas,"montant_ins":montant_ins, "mensualite":mensualite,"id_filiere":id_filiere}
        tab.append(list_clas)
        
        # requete pour afficher les classes correspondantes a cette filiere
        # z = db.session.query(Classe.libelle,Classe.id).join(Filiere).filter(Filiere.id==id_filiere).all()
        # tab1=[]
        # # print(z)
        # for o in z:
        #     caclas={"id_clas":o.id,"nom_classe":o.libelle}
        #     tab1.append(caclas)
        # print(tab1)
         
            
        # tab.append(tab1)

        # # requete pour afficher le nom de la filiere 
        c=db.session.query(Filiere.id,Filiere.libelle).filter_by(id= id_filiere).all()
        id_filiere=c[0].id
        nom_filiere=c[0].libelle
        cal = {"id_fil":id_filiere,"filiere": nom_filiere}
        # # print(cal)
        tab.append(cal)
        # tab.append(tab1)
        # print(tab)
    #     tab3=[]
    #     for j,i in  enumerate(tab):
    #         # print(i)
    #         if j==3:
    #             s=tab[j]
    #             for j in s:
    #                 # print(j)
    #                 tab3.append(j)
    # print(tab3)           
    # return jsonify({'classes':tab3})
            # else:
            #     print(i)

    # print(type(tab),type(tab[0]),type(tab[1]))
    # tab.append(tab1)
    # print(tab[3][1]['nom_classe'])

        lister=Classe.query.filter_by(filiere_id = id_filiere).all()
        # print(lister)
        
        # print(lister)
        for i in lister:
            cl = {}
            cl['id_cl'] = i.id
            cl['libelle'] = i.libelle
            tab.append(cl)
        print(tab)
    return jsonify({'etudiant':tab})    
 

if __name__ == '__main__':
    app.run(debug=True)


     
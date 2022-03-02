#------------------------------------------------------------
#        Script MySQL.
#------------------------------------------------------------


#------------------------------------------------------------
# Table: Compte
#------------------------------------------------------------

CREATE TABLE Compte(
        id          Int  Auto_increment  NOT NULL ,
        nom         Varchar (100) NOT NULL ,
        type        Varchar (50) NOT NULL ,
        email       Varchar (100) NOT NULL ,
        tel         Varchar (10) NOT NULL ,
        description Varchar (500) ,
        domaine     Varchar (50) NOT NULL ,
        video       Varchar (100) ,
        logo        Varchar (100) ,
        lien        Varchar (100) ,
        vu          Int
	,CONSTRAINT Compte_PK PRIMARY KEY (id)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: Contenu
#------------------------------------------------------------

CREATE TABLE Contenu(
        id          Int  Auto_increment  NOT NULL ,
        titre       Varchar (100) NOT NULL ,
        description Varchar (600) ,
        type        Varchar (50) NOT NULL ,
        image       Varchar (100),
        fichier     Varchar (100),
        domaine     Varchar (50),
        vu          Int(11) ,
        id_Compte   Int(10) NOT NULL
	,CONSTRAINT Contenu_PK PRIMARY KEY (id)

	,CONSTRAINT Contenu_Compte_FK FOREIGN KEY (id_Compte) REFERENCES Compte(id)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: Public
#------------------------------------------------------------

CREATE TABLE Public(
        user_id Varchar (20) NOT NULL ,
        action  Varchar (50) ,
        temp    Varchar (100)
	,CONSTRAINT Public_PK PRIMARY KEY (user_id)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: Consultation
#------------------------------------------------------------

CREATE TABLE Consultation(
        user_id Varchar (20) NOT NULL ,
        id      Int NOT NULL ,
        Date    Date NOT NULL
	,CONSTRAINT CONSULTER_PK PRIMARY KEY (user_id,id)

	,CONSTRAINT CONSULTER_Public_FK FOREIGN KEY (user_id) REFERENCES Public(user_id)
	,CONSTRAINT CONSULTER_Contenu0_FK FOREIGN KEY (id) REFERENCES Contenu(id)
)ENGINE=InnoDB;


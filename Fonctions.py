# acronymes
    # QVA: Quantité de Volaille Achetée


# fonctions
def verification(QVA):
    poulets_de_chair = QVA["poulets_de_chair"]
    poules_pondeuses = QVA["poules_pondeuses"]
    dindons = QVA["dindons"]
    annee = QVA["annee_actuelle"]

    justification = "\n ⚠️ Une/les valeur(s) rentrée(s) est/sont invalide(s) car:"
    passed = True

    if poulets_de_chair > 300:
        justification = justification + "\n - Le nombre de poulets_de_chair surpasse la valeur maximale (300)"
        passed = False
    if poulets_de_chair < 0:
        justification = justification + "\n - Le nombre de poulets_de_chair est négatif"
        passed = False
    if dindons > 99:
        justification = justification + "\n - le nombre de dindons surpasse la valeur maximale (99)"
        passed = False
    if dindons < 0:
        justification = justification + "\n - le nombre de dindons est négatif"
        passed = False
    if poules_pondeuses > 25:
        justification = justification + "\n - le nombre de poules_pondeuses surpasse la valeur maximale (25)"
        passed = False
    if poules_pondeuses < 0:
        justification = justification + "\n - le nombre de poules_pondeuses est négatif"
        passed = False
    if annee < 2000:
        justification = justification + "\n - l'année entrée n'est pas réaliste"
        passed = False
    if annee > 2035:
        justification = justification + "\n - l'année entrée n'est pas réaliste"
        passed = False

    # si il y a une erreure, print le message de justification
    if(passed == False): print(justification)

    return passed


# trouver QVA
def trouver_QVA ():

    passed = False
    QVA = []

    while(passed == False):
        QVA = {
         "poulets_de_chair":int(input('Entrez le nombres de poulets_de_chair achetées: ')),
         "poules_pondeuses":int(input('Entrez le nombres de poules_pondeuses achetées: ')),
         "dindons":int(input('Entrez le nombres de dindons achetés: ')),
         "annee_actuelle":int(input('Entrez l\'année actuelle: ')),
        }
        passed = verification(QVA)

    return QVA


# trouver PVA
def trouver_PVA(QVA):

    poulets_de_chair = QVA["poulets_de_chair"]
    poules_pondeuses = QVA["poules_pondeuses"]
    dindons = QVA["dindons"]

    prix_poulets_de_chair = poulets_de_chair * 2.25
    prix_poules_pondeuses = poules_pondeuses * 15
    prix_dindons = dindons * 4.75

    total = prix_poulets_de_chair + prix_poules_pondeuses + prix_dindons

    return total


# trouver QVR_pRpP
def trouver_QVR_pRpP(QVA):

    n_poulets_de_chair_initiales = QVA["poulets_de_chair"]
    n_poules_pondeuses_initiales = QVA["poules_pondeuses"]
    n_dindons_initiales = QVA["dindons"]

    QVR_pRpP = {
        "P1":{
            "n_poulets_de_chair":n_poulets_de_chair_initiales,
            "n_poules_pondeuses":n_poules_pondeuses_initiales,
            "n_dindons":n_dindons_initiales,
        },
        "P2":{
            "n_poulets_de_chair": n_poulets_de_chair_initiales * (2/3),
            "n_poules_pondeuses": n_poules_pondeuses_initiales,
            "n_dindons": n_dindons_initiales,
        },
        "P3":{
            "n_poulets_de_chair": n_poulets_de_chair_initiales * (1/3),
            "n_poules_pondeuses": n_poules_pondeuses_initiales,
            "n_dindons": n_dindons_initiales,
        },
        "P4":{
            "n_poulets_de_chair": 0,
            "n_poules_pondeuses": n_poules_pondeuses_initiales,
            "n_dindons": n_dindons_initiales,
        }
    }

    return QVR_pRpP

# trouver QMC_pRpP
def trouver_QMC_pRpP(QVR_pRpP):

    # P1 = QVR_pRpP["P1"]
    # P2 = QVR_pRpP["P2"]
    # P3 = QVR_pRpP["P3"]
    # P4 = QVR_pRpP["P4"]

    QMC_pRpP = {
        "P1":{
            "poulets_de_chair":(QVR_pRpP["P1"]["n_poulets_de_chair"]) * 2,
            "dindons":(QVR_pRpP["P1"]["n_dindons"]) * 3,
            "poules_pondeuses": (QVR_pRpP["P1"]["n_poules_pondeuses"]) * 3,
        },
        "P2":{
            "poulets_de_chair": (QVR_pRpP["P2"]["n_poulets_de_chair"]) * 4,
            "dindons": (QVR_pRpP["P2"]["n_dindons"]) * 5,
            "poules_pondeuses": (QVR_pRpP["P2"]["n_poules_pondeuses"]) * 3,
        },
        "P3":{
            "poulets_de_chair": (QVR_pRpP["P3"]["n_poulets_de_chair"]) * 4,
            "dindons": (QVR_pRpP["P3"]["n_dindons"]) * 5,
            "poules_pondeuses": (QVR_pRpP["P3"]["n_poules_pondeuses"]) * 6,
        },
        "P4":{
            "poulets_de_chair": (QVR_pRpP["P4"]["n_poulets_de_chair"]) * 0,
            "dindons": (QVR_pRpP["P4"]["n_dindons"]) * 11,
            "poules_pondeuses": (QVR_pRpP["P4"]["n_poules_pondeuses"]) * 6,
        }
    }

    return QMC_pRpP

# trouver QMC_pTM
def trouver_QMC_pTM(QMC_pRpP):
    QMC_pTM = {
        "P1":{
            "poulets":(
                QMC_pRpP["P1"]["poulets_de_chair"] +
                QMC_pRpP["P1"]["poules_pondeuses"]
            ),
            "dindons":QMC_pRpP["P1"]["dindons"],
        },
        "P234":{
            "poulets":(
                QMC_pRpP["P2"]["poulets_de_chair"] +
                QMC_pRpP["P2"]["poules_pondeuses"] +
                QMC_pRpP["P3"]["poulets_de_chair"] +
                QMC_pRpP["P3"]["poules_pondeuses"] +
                QMC_pRpP["P4"]["poulets_de_chair"] +
                QMC_pRpP["P4"]["poules_pondeuses"]
            ),
            "dindons":(
                QMC_pRpP["P2"]["dindons"] +
                QMC_pRpP["P3"]["dindons"] +
                QMC_pRpP["P4"]["dindons"]
            ),
        },
    }
    return QMC_pTM

# trouver QSMC_pTM
def trouver_QSMC_pTM(QMC_pTM):
    QSMC_pTM = {
        "P1": {
            "poulets": QMC_pTM["P1"]["poulets"] / 25,
            "dindons": QMC_pTM["P1"]["dindons"] / 25,
        },
        "P234": {
            "poulets": QMC_pTM["P234"]["poulets"] / 25,
            "dindons": QMC_pTM["P234"]["dindons"] / 25,
        },
    }
    return QSMC_pTM


# trouver PMC_pTM
def trouver_PMC_pTM(QSMC_pTM):
    PMC_pTM = {
        "P1": {
            "poulets": QSMC_pTM["P1"]["poulets"] * 20,
            "dindons": QSMC_pTM["P1"]["dindons"] * 22,
        },
        "P234": {
            "poulets": QSMC_pTM["P234"]["poulets"] * 21,
            "dindons": QSMC_pTM["P234"]["dindons"] * 23,
        },
    }
    return PMC_pTM

# The rest
def calcul_moulee():
    print("A")

def trouver_PMC_Total(PMC_pTM):
    return(
        PMC_pTM["P1"]["poulets"] +
        PMC_pTM["P1"]["dindons"] +
        PMC_pTM["P234"]["poulets"] +
        PMC_pTM["P234"]["dindons"]
    )

def calcul_rip(QVR_pRpP):
    # Premiere periode de semaines
    n_poulets_P1 = QVR_pRpP["P1"]["n_poulets_de_chair"]
    n_poulesP_P1 = QVR_pRpP["P1"]["n_poules_pondeuses"]
    n_dindons_P1 = QVR_pRpP["P1"]["n_dindons"]

    prix_sacs_P1 = (1.25 * (9 * (n_poulets_P1 * 1))) + (3 * (9 * (n_dindons_P1 * 1))) + (3 * (n_poulesP_P1 * (1/3)))


    n_poulets_P2 = QVR_pRpP["P2"]["n_poulets_de_chair"]
    n_poulesP_P2 = QVR_pRpP["P2"]["n_poules_pondeuses"]
    n_dindons_P2 = QVR_pRpP["P2"]["n_dindons"]

    prix_sacs_P2 = (1.25 * (9 * (n_poulets_P2 * 1))) + (3 * (9 * (n_dindons_P2 * 1))) + (3 * (n_poulesP_P2 * (1/3)))


    n_poulets_P3 = QVR_pRpP["P3"]["n_poulets_de_chair"]
    n_poulesP_P3 = QVR_pRpP["P3"]["n_poules_pondeuses"]
    n_dindons_P3 = QVR_pRpP["P3"]["n_dindons"]

    prix_sacs_P3 = (1.25 * (9 * (n_poulets_P3 * 1))) + (3 * (9 * (n_dindons_P3 * 1))) + (3 * (n_poulesP_P3 * (1/3)))


    n_poulets_P4 = QVR_pRpP["P4"]["n_poulets_de_chair"]
    n_poulesP_P4 = QVR_pRpP["P4"]["n_poules_pondeuses"]
    n_dindons_P4 = QVR_pRpP["P4"]["n_dindons"]

    prix_sacs_P4 = (1.25 * (9 * (n_poulets_P4 * 1))) + (3 * (9 * (n_dindons_P4 * 1))) + (3 * (n_poulesP_P4 * (1/3)))

    prix_T = prix_sacs_P3 + prix_sacs_P2 + prix_sacs_P4 + prix_sacs_P1
    return prix_T

def calcul_total():
    print("A")

def jours_par_annee(annee):
    return 366 if est_bissextile(annee) else 365

def oeufs_pondus(QVA):
    n_poulesP = QVA["poules_pondeuses"]
    annee = QVA["annee_actuelle"]
    print("L'année actuelle est", annee)

    # prix par oeuf
    prix_oeuf = 3.75 / 12

    # nombre d'oeufs par semaine
    nb_oeufs_s = n_poulesP * 7 * 1

    # nombre d'oeufs vendus par semaine
    nb_oeufs_v_s = nb_oeufs_s * 0.8
    if nb_oeufs_v_s % 1 != 0:
        nb_oeufs_v_s = int(nb_oeufs_s) + 1

    # revenu brut par semaine
    rev_oeufs_s = nb_oeufs_v_s * prix_oeuf

    # revenu brut par mois (en moyenne)
    rev_oeuf_m = rev_oeufs_s * 4

    # nombre d'oeufs annuel (première année)
    nb_oeufs = n_poulesP * jours_par_annee(annee)
    deuxieme_annee = annee + 1

    # nombre d'oeufs annuel (deuxième année)
    nb_oeufs_2 = n_poulesP * jours_par_annee(deuxieme_annee)

    # nombre total d'oeufs (deux ans réunis)
    nb_T_oeufs = nb_oeufs_2 + nb_oeufs

    # quantité d'oeufs à vendre
    qt_oeufs_vendre = nb_T_oeufs * 0.8

    # reste après la division par 12 pour vendre les oeufs
    qt_oeufs_vendre_reste = qt_oeufs_vendre % 12

    # quantité d'oeufs arrondie (soustrayant le reste) divisible par 12
    qt_oeufs_vendre_arr = qt_oeufs_vendre - qt_oeufs_vendre_reste

    # revenu total des oeufs (un an)
    prix_1an_oeufs = (nb_oeufs * 0.8) * prix_oeuf
    print("revenu des oeufs en 1 an", prix_1an_oeufs)

    # revenu total des oeufs (deux ans)
    prix_total_oeufs = prix_oeuf * qt_oeufs_vendre_arr
    print("Le revenu total des oeufs sera de", prix_total_oeufs, "$")
    return prix_total_oeufs

def est_bissextile(annee):
    if annee % 4 == 0:
        if annee % 100 == 0:
            if annee % 400 == 0:
                return True
            return False
        return True
    return False

def calcul_dernier_jour_elevage_poulets(jour_achat, mois_achat, poulets_de_chair):
    """
    Calcule la dernière journée d'élevage des poulets en fonction des périodes d'abattage.
    """
    # Abattage des poulets à la 4ème, 8ème et 10ème semaine
    abattage_4_semaines = 4 * 7  # 4 semaines en jours
    abattage_8_semaines = 8 * 7  # 8 semaines en jours
    abattage_10_semaines = 10 * 7  # 10 semaines en jours

    # Dernier abattage des poulets : 10 semaines (dernier abattage)
    dernier_jour_poulets = abattage_10_semaines

    # Calcul de la date de fin d'élevage des poulets
    jours_dans_mai = 31
    mois_fin = mois_achat
    jour_fin = jour_achat + dernier_jour_poulets

    # Gestion des mois
    while jour_fin > jours_dans_mai:
        jour_fin -= jours_dans_mai
        mois_fin += 1
        if mois_fin == 2:  # Février
            jours_dans_mai = 28 + est_bissextile(annee)  # 28 ou 29 jours en fonction de l'année
        elif mois_fin in [4, 6, 9, 11]:  # Mois avec 30 jours
            jours_dans_mai = 30
        else:  # Mois avec 31 jours
            jours_dans_mai = 31

    return f"{jour_fin:02d}-{mois_fin:02d}-{annee}"


def calcul_dernier_jour_elevage_dindons(jour_achat, mois_achat):
    """
    Calcule la dernière journée d'élevage des dindons, prévue à la 19ème semaine.
    """
    # Abattage des dindons à la 19ème semaine
    abattage_19_semaines = 19 * 7  # 19 semaines en jours

    # Calcul de la date de fin d'élevage des dindons
    jours_dans_mai = 31
    mois_fin = mois_achat
    jour_fin = jour_achat + abattage_19_semaines

    # Gestion des mois
    while jour_fin > jours_dans_mai:
        jour_fin -= jours_dans_mai
        mois_fin += 1
        if mois_fin == 2:  # Février
            jours_dans_mai = 28 + est_bissextile(annee)  # 28 ou 29 jours en fonction de l'année
        elif mois_fin in [4, 6, 9, 11]:  # Mois avec 30 jours
            jours_dans_mai = 30
        else:  # Mois avec 31 jours
            jours_dans_mai = 31

    return f"{jour_fin:02d}-{mois_fin:02d}-{annee}"

QVA = trouver_QVA()

# Durées des périodes d'élevage en semaines
durees_periodes = {
    "Période 1 (0-4 semaines)": 4,  # 0 à 4 semaines
    "Période 2 (4-8 semaines)": 4,  # 4 à 8 semaines
    "Période 3 (8-10 semaines)": 2,  # 8 à 10 semaines
    "Période 4 (10-14 semaines)": 4  # 10 à 14 semaines
}

# Variables
annee = QVA["annee_actuelle"]
jour_achat = 27
mois_achat = 5  # Mai

# Calculer la dernière journée d'élevage des poulets
date_dernier_jour_poulets = calcul_dernier_jour_elevage_poulets(jour_achat, mois_achat, QVA["poulets_de_chair"])

# Calculer la dernière journée d'élevage des dindons
date_dernier_jour_dindons = calcul_dernier_jour_elevage_dindons(jour_achat, mois_achat)

def tableau_de_choix(QVR_pRpP, QVA, PVA, PMC_Total, PrixRip, oeufs_pondus):
    while True:
        n_poulets_P1 = QVR_pRpP["P1"]["n_poulets_de_chair"]
        n_poulesP_P1 = QVR_pRpP["P1"]["n_poules_pondeuses"]
        n_dindons_P1 = QVR_pRpP["P1"]["n_dindons"]

        n_poulets_P2 = QVR_pRpP["P2"]["n_poulets_de_chair"]
        n_poulesP_P2 = QVR_pRpP["P2"]["n_poules_pondeuses"]
        n_dindons_P2 = QVR_pRpP["P2"]["n_dindons"]

        n_poulets_P3 = QVR_pRpP["P3"]["n_poulets_de_chair"]
        n_poulesP_P3 = QVR_pRpP["P3"]["n_poules_pondeuses"]
        n_dindons_P3 = QVR_pRpP["P3"]["n_dindons"]

        n_poulets_P4 = QVR_pRpP["P4"]["n_poulets_de_chair"]
        n_poulesP_P4 = QVR_pRpP["P4"]["n_poules_pondeuses"]
        n_dindons_P4 = QVR_pRpP["P4"]["n_dindons"]

        # fonction sur les litières
        prix_sacs_P1 = (1.25 * (9 * (n_poulets_P1 * 1))) + (3 * (9 * (n_dindons_P1 * 1))) + (3 * (n_poulesP_P1 * (1/3)))
        prix_sacs_P2 = (1.25 * (9 * (n_poulets_P2 * 1))) + (3 * (9 * (n_dindons_P2 * 1))) + (3 * (n_poulesP_P2 * (1/3)))
        prix_sacs_P3 = (1.25 * (9 * (n_poulets_P3 * 1))) + (3 * (9 * (n_dindons_P3 * 1))) + (3 * (n_poulesP_P3 * (1/3)))
        prix_sacs_P4 = (1.25 * (9 * (n_poulets_P4 * 1))) + (3 * (9 * (n_dindons_P4 * 1))) + (3 * (n_poulesP_P4 * (1/3)))

        # les frais initiales d’investissement
        FII = PVA + PMC_Total + PrixRip

        # fonction des oeufs
        n_poulesP = QVA["poules_pondeuses"]
        annee = QVA["annee_actuelle"]
        prix_oeuf = 3.75 / 12
        nb_oeufs_s = n_poulesP * 7 * 1
        nb_oeufs_v_s = nb_oeufs_s * 0.8
        if nb_oeufs_v_s % 1 != 0:
            nb_oeufs_v_s = int(nb_oeufs_s) + 1
        rev_oeufs_s = nb_oeufs_v_s * prix_oeuf
        rev_oeuf_m = rev_oeufs_s * 4
        nb_oeufs = n_poulesP * jours_par_annee(annee)
        prix_1an_oeufs = (nb_oeufs * 0.8) * prix_oeuf
        deuxieme_annee = annee + 1
        nb_oeufs_2 = n_poulesP * jours_par_annee(deuxieme_annee)
        prix_1an_oeufs_2 = (nb_oeufs_2 * 0.8) * prix_oeuf
        nb_T_oeufs = nb_oeufs_2 + nb_oeufs
        qt_oeufs_vendre = nb_T_oeufs * 0.8
        qt_oeufs_vendre_reste = qt_oeufs_vendre % 12
        qt_oeufs_vendre_arr = qt_oeufs_vendre - qt_oeufs_vendre_reste



        entree_1 = int(input("Sélectionnez ce que vous voulez accéder:"
        "\n - 1. Informations sur les frais initiales d’investissement (1):"
        "\n - 2. Informations sur les poulets, les dindons et les poules pondeuses à travers des semaines (2):"
        "\n - 3. Quantité de rip (litière) à travers des semaines (3):"
        "\n - 4. Prix (dépendamment de la période) de la rip (litière) (4):"
        "\n - 5. Informations sur les oeufs (brut) (5):"
        "\n - 6. Informations sur les oeufs (net) (6):"
        "\n - 7. Informations sur les dernières dates d'élevage (7):"
        "\n - 8. Quitter (8):"
        "\n entrez la valeur ici:"))
        print("*" * 100)

        if entree_1 == 1:
            entree_2 = int(input("Sélectionnez ce que vous voulez accéder:"
            "\n - 1. Les frais initiales d'investissement (1):"
            "\n entrez la valeur ici:"))
            print("*" * 100)

            if entree_2 == 1:
                print("Les frais initiales d'investissement sont de", FII,"$")

        if entree_1 == 2:
            entree_2 = int(input("Sélectionnez ce que vous voulez accéder:"
            "\n - 1. Quantité pendant 0 à 4 semaines (1):"
            "\n - 2. Quantité pendant 4 à 8 semaines (2):"
            "\n - 3. Quantité pendant 8 à 10 semaines (3):"
            "\n - 4. Quantité pendant 10 à 14 semaines (4):"
            "\n - 5. Prix total payé pour les volailles (5):"
            "\n entrez la valeur ici:"))
            print("*" * 100)

            if entree_2 == 1:
                print("La quantité de poulets de chair est de",n_poulets_P1,
                "\nde dindons de chair est de", n_dindons_P1,
                "\net de poules pondeuses est de", n_poulesP_P1)
            elif entree_2 == 2:
                print("La quantité de poulets de chair est de",int(n_poulets_P2),
                "\nde dindons de chair est de", n_dindons_P2,
                "\net de poules pondeuses est de", n_poulesP_P2)
            elif entree_2 == 3:
                print("La quantité de poulets de chair est de",int(n_poulets_P3),
                "\nde dindons de chair est de", n_dindons_P3,
                "\net de poules pondeuses est de", n_poulesP_P3)
            elif entree_2 == 4:
                print("La quantité de poulets de chair est de",n_poulets_P4,
                "\nde dindons de chair est de", n_dindons_P4,
                "\net de poules pondeuses est de", n_poulesP_P4)
            elif entree_2 == 5:
                print("Le prix total payé pour les volailles est de",trouver_PVA(QVA),"$")

        elif entree_1 == 3:
            entree_2 = int(input("Sélectionnez ce que vous voulez accéder:"
            "\n - 1. Quantité pendant 0 à 4 semaines (1):"
            "\n - 2. Quantité pendant 4 à 8 semaines (2):"
            "\n - 3. Quantité pendant 8 à 10 semaines (3):"
            "\n - 4. Quantité pendant 10 à 14 semaines (4):"
            "\n entrez la valeur ici:"))
            print("*" * 100)

            if entree_2 == 1:
                resultat1 = (9 * (n_poulets_P1 * 1)) + (9 * (n_dindons_P1 * 1)) + (n_poulesP_P1 * (1/3))
                if resultat1 % 1 != 0:
                    resultat1 = int(resultat1) + 1
                print("La quantité de rip pendant 0 à 4 semaines est de", resultat1)
            elif entree_2 == 2:
                resultat2 = (9 * (n_poulets_P2 * 1)) + (9 * (n_dindons_P2 * 1)) + (n_poulesP_P2 * (1/3))
                if resultat2 % 1 != 0:
                    resultat2 = int(resultat2) + 1
                print("La quantité de rip pendant 4 à 8 semaines est de", resultat2)
            elif entree_2 == 3:
                resultat3 = (9 * (n_poulets_P3 * 1)) + (9 * (n_dindons_P3 * 1)) + (n_poulesP_P3 * (1/3))
                if resultat3 % 1 != 0:
                    resultat3 = int(resultat3) + 1
                print("La quantité de poulets de chair est de", resultat3)
            elif entree_2 == 4:
                resultat4 = (9 * (n_poulets_P4 * 1)) + (9 * (n_dindons_P4 * 1)) + (n_poulesP_P4 * (1/3))
                if resultat4 % 1 != 0:
                    resultat4 = int(resultat4) + 1
                print("La quantité de poulets de chair est de", resultat4)

        elif entree_1 == 4:
            entree_2 = int(input("Sélectionnez ce que vous voulez accéder:"
            "\n - 1. Prix à la fin de la 4ième semaine (1):"
            "\n - 2. Prix à la fin de la 8ième semaine (2):"
            "\n - 3. Prix à la fin de la 10ième semaine (3):"
            "\n - 4. Prix à la fin de la 14ième semaine (4):"
            "\n - 5. Prix total de la rip (litière) (5):"
            "\n entrez la valeur ici:"))
            print("*" * 100)

            if entree_2 == 1:
                print("Le prix à la fin de la 4ième semaine est de,", prix_sacs_P1,"$")
            elif entree_2 == 2:
                print("Le prix à la fin de la 8ième semaine est de,", prix_sacs_P2, "$")
            elif entree_2 == 3:
                print("Le prix à la fin de la 10ième semaine est de,", prix_sacs_P3, "$")
            elif entree_2 == 4:
                print("Le prix à la fin de la 14ième semaine est de,", prix_sacs_P4, "$")
            elif entree_2 == 5:
                print("Le prix total de la rip (litière) est de,",calcul_rip(QVR_pRpP),"$")

        elif entree_1 == 5:
            entree_2 = int(input("Sélectionnez ce que vous voulez accéder:"
            "\n - 1. Revenu brut généré par semaine, mois et année (première année) (1):"
            "\n - 2. Revenu brut généré par semaine, mois et année (deuxième année) (2):"
            "\n - 3. Quantité total d'oeufs (3):"
            "\n - 4. Revenu total des oeufs (4):"
            "\n entrez la valeur ici:"))
            print("*" * 100)
            if entree_2 == 1:
                print("Le revenu brut généré pour la première année sont:"
                "\nLe revenu par semaine:", rev_oeufs_s,"$"
                "\nLe revenu par mois:", rev_oeuf_m,"$"
                "\nLe revenu par an:", prix_1an_oeufs,"$")
            elif entree_2 == 2:
                print("Le revenu brut généré pour la deuxième année sont:"
                "\nLe revenu par semaine:", rev_oeufs_s,"$"
                "\nLe revenu par mois:", rev_oeuf_m,"$"
                "\nLe revenu par an:", prix_1an_oeufs_2,"$")
            elif entree_2 == 3:
                print("La quantité total d'oeufs à vendre (deux ans) est:", qt_oeufs_vendre_arr,"$")
            elif entree_2 == 4:
                print("Le revenu brut total des oeufs (deux ans) est:", oeufs_pondus, "$")

        elif entree_1 == 6:
            entree_2 = int(input("Sélectionnez ce que vous voulez accéder:"
            "\n - 1. Revenu net généré par semaine, mois et année (première année) (1):"
            "\n - 2. Revenu net généré par semaine, mois et année (deuxième année) (2):"
            "\n - 3. Revenu net total des oeufs (3):"
            "\n entrez la valeur ici:"))
            if entree_2 == 1:
                print("Le revenu net généré pour la première année sont:"
                "\nLe revenu net par semaine:", rev_oeufs_s - (FII / 52),"$"
                "\nLe revenu net par mois:", rev_oeuf_m - (FII / 12),"$"
                "\nLe revenu net par an:", prix_1an_oeufs - FII,"$")
            elif entree_2 == 2:
                print("Le revenu net généré pour la deuxième année sont:"
                "\nLe revenu net par semaine:", rev_oeufs_s - (FII / 52),"$"
                "\nLe revenu net par mois:", rev_oeuf_m - (FII / 12),"$"
                "\nLe revenu net par an:", prix_1an_oeufs_2 - FII,"$")
            elif entree_2 == 3:
                print("Le revenu net des achats et des ventes (deux ans) est:", oeufs_pondus - (2 * FII),"$")

        elif entree_1 == 7:
            entree_2 = int(input("Sélectionnez ce que vous voulez accéder:"
            "\n - 1. La date de fin d'élevage des poulets (1):"
            "\n - 2. La date de fin d'élevage des dindons (2):"
            "\n entrez la valeur ici:"))
            print("*" * 100)

            if entree_2 == 1:
                print("Date de fin d'élevage des poulets:", date_dernier_jour_poulets)
            if entree_2 == 2:
                print("Date de fin d'élevage des dindons:", date_dernier_jour_dindons)

        elif entree_1 == 8:
            print("Merci de votre visite!")
            break  # Exit the loop and end the program

        else:
            print("Option non valide. Veuillez entrer un choix valide.")

            # Ask the user if they want to continue
        continue_choice = input("\nVoulez-vous continuer? (oui/non): ").lower()
        if continue_choice != 'oui':
            print("Merci de votre visite!")
            break  # Exit the loop if the user does not want to continue
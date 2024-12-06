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
         "annee_actuelle":int(input('Entrez l\'année actuelle')),
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

def calcul_rip(QVR_pRpP):
    # Premiere periode de semaines
    n_poulets_P1 = QVR_pRpP["P1"]["n_poulets_de_chair"]
    n_poulesP_P1 = QVR_pRpP["P1"]["n_poules_pondeuses"]
    n_dindons_P1 = QVR_pRpP["P1"]["n_dindons"]
    print(n_dindons_P1, n_poulesP_P1, n_poulets_P1)
    prix_sacs_P1 = (1.25 * (9 * (n_poulets_P1 * 1))) + (3 * (9 * (n_dindons_P1 * 1))) + (3 * (n_poulesP_P1 * (1/3)))
    print(prix_sacs_P1)

    n_poulets_P2 = QVR_pRpP["P2"]["n_poulets_de_chair"]
    n_poulesP_P2 = QVR_pRpP["P2"]["n_poules_pondeuses"]
    n_dindons_P2 = QVR_pRpP["P2"]["n_dindons"]
    print(n_dindons_P2, n_poulesP_P2, n_poulets_P2)
    prix_sacs_P2 = (1.25 * (9 * (n_poulets_P2 * 1))) + (3 * (9 * (n_dindons_P2 * 1))) + (3 * (n_poulesP_P2 * (1/3)))
    print(prix_sacs_P2)

    n_poulets_P3 = QVR_pRpP["P3"]["n_poulets_de_chair"]
    n_poulesP_P3 = QVR_pRpP["P3"]["n_poules_pondeuses"]
    n_dindons_P3 = QVR_pRpP["P3"]["n_dindons"]
    print(n_dindons_P3, n_poulesP_P3, n_poulets_P3)
    prix_sacs_P3 = (1.25 * (9 * (n_poulets_P3 * 1))) + (3 * (9 * (n_dindons_P3 * 1))) + (3 * (n_poulesP_P3 * (1/3)))
    print(prix_sacs_P3)

    n_poulets_P4 = QVR_pRpP["P4"]["n_poulets_de_chair"]
    n_poulesP_P4 = QVR_pRpP["P4"]["n_poules_pondeuses"]
    n_dindons_P4 = QVR_pRpP["P4"]["n_dindons"]
    print(n_dindons_P4, n_poulesP_P4, n_poulets_P4)
    prix_sacs_P4 = (1.25 * (9 * (n_poulets_P4 * 1))) + (3 * (9 * (n_dindons_P4 * 1))) + (3 * (n_poulesP_P4 * (1/3)))
    print(prix_sacs_P4)

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

    nb_oeufs = n_poulesP * jours_par_annee(annee)
    print("et son nombre de jours est", jours_par_annee(annee))
    deuxieme_annee = annee + 1
    print("L'année prochaine sera", deuxieme_annee)

    nb_oeufs_2 = n_poulesP * jours_par_annee(deuxieme_annee)
    print("et son nombre de jours est", jours_par_annee(deuxieme_annee))
    nb_T_oeufs = nb_oeufs_2 + nb_oeufs
    print("La quantité d'oeufs produite en deux ans est de", nb_T_oeufs,"oeufs")

    qt_oeufs_vendre = nb_T_oeufs * 0.8
    qt_oeufs_vendre_reste = qt_oeufs_vendre % 12
    qt_oeufs_vendre_arr = qt_oeufs_vendre - qt_oeufs_vendre_reste
    prix_total_oeufs = 3.75 * (qt_oeufs_vendre_arr / 12)
    return print("Le revenu total des oeufs sera de", prix_total_oeufs,"$")

def est_bissextile(annee):
    if annee % 4 == 0:
        if annee % 100 == 0:
            if annee % 400 == 0:
                return True
            return False
        return True
    return False
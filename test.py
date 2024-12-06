def jours_par_annee(annee):
    return 366 if est_bissextile(annee) else 365
def oeufs_pondus(QVR_pRpP):
    n_poulesP_P4 = QVR_pRpP["P4"]["n_poules_pondeuses"]
    annee = QVA["annee_actuelle"]

    nb_oeufs = n_poulesP_P4 * jours_par_annee(annee)
    deuxieme_annee = annee + 1

    nb_oeufs_2 = n_poulesP_P4 * jours_par_annee(deuxieme_annee)
    nb_T_oeufs = nb_oeufs_2 + nb_oeufs
    print(nb_T_oeufs)
    reste_T_oeufs = nb_T_oeufs % 12
    print(reste_T_oeufs)
    nb_oeufs_div_12 = nb_T_oeufs - reste_T_oeufs
    prix_total_oeufs = 3.75 * (nb_oeufs_div_12 / 12)
    return prix_total_oeufs

def est_bissextile(annee):
    if annee % 4 == 0:
        if annee % 100 == 0:
            if annee % 400 == 0:
                return True
            return False
        return True
    return False

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

print(oeufs_pondus(QVR_pRpP))
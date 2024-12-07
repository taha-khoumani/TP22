# Organized Dictionary Print (delete before submit)
import json
def C(D): # C: see
    return json.dumps(D, indent=4)


# Noms et Prenoms
    # e6321570, Taha Khoumani
    # eXXXXXXX, Yahya Silva


# Importation des fonctions:
from Fonctions import *


# QVA: Quantité de Volaille Achetée
    #QVA = trouver_QVA()

# PVA: Prix des Volaille Achetée
PVA = trouver_PVA(QVA)
print(f'PVA: {PVA}')


# QVR_pRpP: Quantite de Volaille Restants par Race par Periode
QVR_pRpP = trouver_QVR_pRpP(QVA)
print(f'QVR_pRpP: {C(QVR_pRpP)}')


# QMC_pRpP(kg): Quantite de Moulée Consommé par Race par Periode
QMC_pRpP = trouver_QMC_pRpP(QVR_pRpP)
print(f'QMC_pRpP: {C(QMC_pRpP)}')

# QMC_pTM(kg): Quantite de Moulée Consommé par Type de Moulée
QMC_pTM = trouver_QMC_pTM(QMC_pRpP)
print(f'QMC_pTM: {C(QMC_pTM)}')


# QSMC_pTM(sacs): Quantite de Sacs de Moulée Consommé par Type de Moulée
QSMC_pTM = trouver_QSMC_pTM(QMC_pTM)
print(f'QSMC_pTM: {C(QSMC_pTM)}')

# PMC_pTM: Prix de Moulée Consommé par Type de Moulée
PMC_pTM = trouver_PMC_pTM(QSMC_pTM)
print(f'PMC_pTM: {C(PMC_pTM)}')

# PMC-Total: Prix de Moulée Consommé Total
PMC_Total = trouver_PMC_Total(PMC_pTM)
print(f'\nPrix de Moulée Total: {C(PMC_Total)}')

# PrixRip
PrixRip = calcul_rip(QVR_pRpP)
print(f'\nPrixRip: {PrixRip}')

# Frais Initiales d'investisement
FII = PVA + PMC_Total + PrixRip
print(f"\nFrais Initiale d'Investissement: {FII}")

oeufs_pondus(QVA)

tableau_de_choix(QVR_pRpP, QVA, PVA, PMC_Total, PrixRip, oeufs_pondus(QVA))

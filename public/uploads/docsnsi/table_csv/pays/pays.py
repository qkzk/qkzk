import csv


def charger(fichier: str, delimiter=';') -> list:
    '''charge un fichier csv et renvoie une table'''
    with open(fichier) as fichiercsv:
        lecteur_csv = csv.DictReader(fichiercsv, delimiter=delimiter)
        return [dict(enregistrement) for enregistrement in lecteur_csv]


def caster_pays(table: list):
    '''renvoie une copie de la table avec les bons types'''
    return [{
        'ISO': pays['ISO'],
        'Country': pays['Country'],
        'Capital': pays['Capital'],
        'Area': float(pays['Area(in sq km)']),
        'Population': int(pays['Population']),
        'CurrencyCode': pays['CurrencyCode'],
        'CurrencyName': pays['CurrencyName'],
    } for pays in table]


def recup_pays(table: list, iso: str) -> dict:
    '''renvoie l'enregistrement d'un pays de la table depuis son code iso'''
    return [enregistrement for enregistrement in table
            if enregistrement['ISO'] == iso][0]


def capitale(table: list, iso: str) -> str:
    '''renvoie la capitale d'un pays depuis son code iso'''
    return recup_pays(table, iso)['Capital']


def project(table: list, liste_champs: list):
    '''projette la table et ne garde que les colonnes de liste_champs'''
    return [{champ: enregistrement[champ] for champ in liste_champs}
            for enregistrement in table]


def trier_critere(table: list, champ: str, reverse=False):
    '''renvoie une copie triée de la table selon un critère'''
    return sorted(table, key=lambda pays: pays[champ], reverse=reverse)


def tester():
    table_pays = charger("./countries.csv")
    table_pays = caster_pays(table_pays)
    france = recup_pays(table_pays, "FR")
    assert capitale(table_pays, 'FR') == 'Paris'
    champs = list(table_pays[0].keys())
    iso_pays_capitale = project(table_pays, ['ISO', 'Country', 'Capital'])
    assert list(iso_pays_capitale[0].keys()) == ['ISO', 'Country', 'Capital']
    surface_croissante = trier_critere(table_pays, 'Area')
    assert surface_croissante[-1]['ISO'] == 'RU'
    pop_decroissante = trier_critere(table_pays, 'Population', reverse=True)
    assert pop_decroissante[0]['ISO'] == 'CN'
    print(project(pop_decroissante[:5], ['Country']))


if __name__ == "__main__":
    tester()

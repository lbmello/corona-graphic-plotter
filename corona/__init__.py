from .Country import Country, Day
from .RequestJson import RequestJson

# Cria conjunto dos territórios
set_dt = set()

for reg in RequestJson.json_request:
    set_dt.add(reg['countriesAndTerritories'])

# Instancia objetos para os territórios
list_country = list()

for country in set_dt:
    list_country.append(Country(country=country))

# Aciona o metóro set_day de cada país e grava na lista days
for obj_country in list_country:
    print(f'==== Processando registros de {obj_country.country} ====')

    for registry in RequestJson.json_request:
        if registry['countriesAndTerritories'] == obj_country.country:
            #print(f" - Registro do pais {obj_country.country} para o dia {registry['dateRep']} - ")

            obj_country.set_day(population = registry['popData2018'], 
                                date = f"{registry['day']}/{registry['month']}/{registry['year']}",
                                cases = registry['cases'],
                                deaths = registry['deaths'])

    obj_country.plot()
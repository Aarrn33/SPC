#L'objectif est de trouver la liste des pays contenants un string (stringToFind)
def main(stringToFind):
    ### Ne pas toucher ###
    with open("Seance 1/country_list.txt", "r", encoding="utf-8") as file:
        allCountries = file.read()
    allCountries = allCountries.splitlines()
    allCountries = [country[:-5].lower() for country in allCountries]
    ### Entrez votre code ###
    searchHits = []
    for country in allCountries:
        if stringToFind in country:
            searchHits.append(country)
    return searchHits


### Ne pas toucher ###
if __name__ == "__main__":
    inputStringToFind = input().lower()
    print(main(inputStringToFind))

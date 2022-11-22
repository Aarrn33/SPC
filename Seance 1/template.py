#L'objectif est de trouver la liste des pays contenants un string (stringToFind)
def main(stringToFind):
    ### Ne pas toucher ###
    with open("country_list.txt", "r", encoding="utf-8") as file:
        allCountries = file.read()
    allCountries = allCountries.splitlines()
    allCountries = [country[:-5] for country in allCountries]
    ### Entrez votre code ###


if __name__ == "__main__":
    inputStringToFind = input()
    main(inputStringToFind)

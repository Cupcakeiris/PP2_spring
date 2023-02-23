import datetime

with open("C:\KBTU\\2nd semester\pp2\TSIS6\dir-and-files\\task7-txt-copy\countriesLetterA.txt", "r") as file:
    with open("C:\KBTU\\2nd semester\pp2\TSIS6\dir-and-files\\task7-txt-copy\moveCountries.txt", "w") as f:
        for line in file:
            f.write(line)
        f.write(f"\n\nFile moved on {datetime.datetime.now()}")
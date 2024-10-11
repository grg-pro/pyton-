import random
"""Играть в викторину."""
# List of famous people and their birthdates
famous_people = [
    ("Albert Einstein", "14.03.1879"),
    ("Isaac Newton", "04.01.1643"),
    ("Galileo Galilei", "15.02.1564"),
    ("Marie Curie", "07.11.1867"),
    ("Charles Darwin", "12.02.1809"),
    ("Nikola Tesla", "10.07.1856"),
    ("Leonardo da Vinci", "15.04.1452"),
    ("Thomas Edison", "11.02.1847"),
    ("Ada Lovelace", "10.12.1815"),
    ("Alan Turing", "23.06.1912"),
    ("Stephen Hawking", "08.01.1942"),
    ("Nikolaus Copernicus", "19.02.1473"),
    ("Johannes Kepler", "27.12.1571"),
    ("Max Planck", "23.04.1858"),
    ("Erwin Schrödinger", "12.08.1887"),
    ("Louis Pasteur", "27.12.1822"),
    ("Marie Curie", "07.11.1867"),
    ("Niels Bohr", "07.10.1885"),
    ("Richard Feynman", "11.05.1918"),
    ("Ernest Rutherford", "30.08.1871"),
    ("Enrico Fermi", "29.09.1901"),
    ("Robert Oppenheimer", "22.04.1904"),
    ("Paul Dirac", "08.08.1902"),
    ("Werner Heisenberg", "05.12.1901"),
    ("Hans Bethe", "02.07.1906"),
    ("Richard Dawkins", "26.03.1941"),
    ("Carl Sagan", "09.11.1934"),
    ("Jane Goodall", "03.04.1934"),
    ("Richard Leakey", "19.12.1944"),
    ("Jacques Cousteau", "11.06.1910"),
    ("David Attenborough", "08.05.1926"),
    ("Dian Fossey", "16.01.1932"),
    ("Sylvia Earle", "30.08.1935"),
    ("Rachel Carson", "27.05.1907"),
    ("Margaret Mead", "16.12.1901"),
    ("Louis Leakey", "07.08.1903"),
    ("Stephen Jay Gould", "10.09.1941"),
    ("James Watson", "06.04.1928"),
    ("Francis Crick", "08.06.1916"),
    ("Rosalind Franklin", "25.07.1920")
]

# Function to convert date to readable format
def format_date(date_str):
    months = ["января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентября", "октября", "ноября", "декабря"]
    day, month, year = date_str.split('.')
    return f"{int(day)} {months[int(month) - 1]} {year} года"


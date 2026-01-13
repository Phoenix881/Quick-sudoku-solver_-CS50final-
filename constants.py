# Initial markings, placeholders
markings_for_rendering = [
    ' ', ' ', ' ',  ' ', ' ', ' ',  ' ', ' ', ' ',
    ' ', ' ', ' ',  ' ', ' ', ' ',  ' ', ' ', ' ', 
    ' ', ' ', ' ',  ' ', ' ', ' ',  ' ', ' ', ' ', 
    ' ', ' ', ' ',  ' ', ' ', ' ',  ' ', ' ', ' ', 
    ' ', ' ', ' ',  ' ', ' ', ' ',  ' ', ' ', ' ', 
    ' ', ' ', ' ',  ' ', ' ', ' ',  ' ', ' ', ' ', 
    ' ', ' ', ' ',  ' ', ' ', ' ',  ' ', ' ', ' ', 
    ' ', ' ', ' ',  ' ', ' ', ' ',  ' ', ' ', ' ', 
    ' ', ' ', ' ',  ' ', ' ', ' ',  ' ', ' ', ' '
]
markings_for_calculation = [
    0, 0, 0,  0, 0, 0,  0, 0, 0,
    0, 0, 0,  0, 0, 0,  0, 0, 0,
    0, 0, 0,  0, 0, 0,  0, 0, 0,

    0, 0, 0,  0, 0, 0,  0, 0, 0,
    0, 0, 0,  0, 0, 0,  0, 0, 0,
    0, 0, 0,  0, 0, 0,  0, 0, 0,

    0, 0, 0,  0, 0, 0,  0, 0, 0,
    0, 0, 0,  0, 0, 0,  0, 0, 0,
    0, 0, 0,  0, 0, 0,  0, 0, 0
]
# Markings that user inputted
# While solving sudoku we cannot change these values
constant_markings_indexes = []

# Acceptable flags
acceptable_flags = ["-h", "--help", "-r", "--rules"]

# First goes column and then row, DE means column D row D, Column|Row
positions = [
    'AA', 'BA', 'CA', 'DA', 'EA', 'FA', 'GA', 'HA', 'IA', 
    'AB', 'BB', 'CB', 'DB', 'EB', 'FB', 'GB', 'HB', 'IB', 
    'AC', 'BC', 'CC', 'DC', 'EC', 'FC', 'GC', 'HC', 'IC', 
    'AD', 'BD', 'CD', 'DD', 'ED', 'FD', 'GD', 'HD', 'ID', 
    'AE', 'BE', 'CE', 'DE', 'EE', 'FE', 'GE', 'HE', 'IE', 
    'AF', 'BF', 'CF', 'DF', 'EF', 'FF', 'GF', 'HF', 'IF', 
    'AG', 'BG', 'CG', 'DG', 'EG', 'FG', 'GG', 'HG', 'IG', 
    'AH', 'BH', 'CH', 'DH', 'EH', 'FH', 'GH', 'HH', 'IH', 
    'AI', 'BI', 'CI', 'DI', 'EI', 'FI', 'GI', 'HI', 'II'
]

position_to_index = {
    "AA": 0,  "BA": 1,  "CA": 2,   "DA": 3,  "EA": 4,  "FA": 5,   "GA": 6,  "HA": 7,  "IA": 8,
    "AB": 9, "BB": 10, "CB": 11,  "DB": 12, "EB": 13, "FB": 14,  "GB": 15, "HB": 16, "IB": 17,
    "AC": 18, "BC": 19, "CC": 20,  "DC": 21, "EC": 22, "FC": 23,  "GC": 24, "HC": 25, "IC": 26,

    "AD": 27, "BD": 28, "CD": 29,  "DD": 30, "ED": 31, "FD": 32,  "GD": 33, "HD": 34, "ID": 35,
    "AE": 36, "BE": 37, "CE": 38,  "DE": 39, "EE": 40, "FE": 41,  "GE": 42, "HE": 43, "IE": 44,
    "AF": 45, "BF": 46, "CF": 47,  "DF": 48, "EF": 49, "FF": 50,  "GF": 51, "HF": 52, "IF": 53,

    "AG": 54, "BG": 55, "CG": 56,  "DG": 57, "EG": 58, "FG": 59,  "GG": 60, "HG": 61, "IG": 62,
    "AH": 63, "BH": 64, "CH": 65,  "DH": 66, "EH": 67, "FH": 68,  "GH": 69, "HH": 70, "IH": 71,
    "AI": 72, "BI": 73, "CI": 74,  "DI": 75, "EI": 76, "FI": 77,  "GI": 78, "HI": 79, "II": 80
}

square_one = [
    0,  1,  2,
    9,  10, 11,
    18, 19, 20
    ]
square_two = [
    3,  4,  5,
    12, 13, 14,
    21, 22, 23
]
square_three = [
    6,  7,  8,
    15, 16, 17,
    24, 25, 26
]
    
square_four = [
    27, 28, 29,
    36, 37, 38,
    45, 46, 47
]
square_five = [
    30, 31, 32,
    39, 40, 41,
    48, 49, 50
]
square_six = [
    33, 34, 35,
    42, 43, 44,
    51, 52, 53
]
    
square_seven = [
    54, 55, 56,
    63, 64, 65,
    72, 73, 74
]
square_eight = [
    57, 58, 59,
    66, 67, 68,
    75, 76, 77
]
square_nine = [
    60, 61, 62,
    69, 70, 71,
    78, 79, 80
]

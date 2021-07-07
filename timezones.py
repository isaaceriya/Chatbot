#INSTALLATION OF PYTZ MODULE IS REQUIRED BEFORE USE OR ERRORS WILL OCCUR!

from datetime import datetime
from pytz import timezone

#Formatting structure to be used by the function in its output.

fmt = '%d/%m/%Y %H:%M:%S'

# Function for interpreting users input and assigning the correct function for the  desired time.

def interpreter(country):
# UTC 0
    if any(x in country for x in ["uk", "great britain", "england", "wales", "ireland", "northern ireland", "republic of ireland", "scotland", "cote d'ivoire","ivory coast", "burkina faso", "faroe islands", "gambia", "ghana", "guinea", "guinea-bissau", "iceland", "liberia", "mali", "mauritania", "portugal", "madeira", "canary islands", "senegal", "sierra leone", "togo", "guernsey", "isle of man", "jersey", "saint helena"]):
        return utc_plus_0()

# UTC+ timezones
# UTC +1
    elif any(x in country for x in ["albania", "algeria", "andorra", "angola", "austria", "belgium", "benin", "bosnia and herzegovina", "cameroon", "central african republic", "chad", "republic of the congo", "croatia", "czech republic", "denmark", "equatorial guinea", "france", "gabon", "germany", "hungary", "italy", "kosovo", "liechtenstein", "luxembourg", "macedonia", "malta", "monaco", "montenegro", "morocco", "netherlands", "niger", "nigeria", "norway", "poland", "san marino", "sau tome and principe", "serbia", "slovakia", "slovenia", "spain", "balearic islands", "ceuta", "melilla", "sweden", "switzerland", "tunisia", "gibraltar", "vatican city", "western sahara"]):
        return utc_plus_1()
# UTC +2
    elif any(x in country for x in ["botswana", "bulgaria", "burundi", "cyprus", "egypt", "estonia", "finland", "greece", "israel", "jordan", "latvia", "lebanon", "lesotho", "lithuania", "libya", "malawi", "transnistria", "moldova", "mozambique", "nambia", "state of palestine", "romania", "rwanda", "south africa", "sudan", "swaziland", "syria", "akrotiri and dhekelia", "zambia", "zimbabwe"]):
        return utc_plus_2()
# UTC +3
    elif any(x in country for x in ["bahrain", "belarus", "comoros", "djibouti", "eritrea", "ethiopia", "iraq", "kenya", "kuwait", "madagascar", "qatar", "saudi arabia", "somalia", "prince edward islands", "south sudan", "tanzania", "turkey", "uganda", "yemen"]):
        return utc_plus_3()
# UTC +3:30
    elif any(x in country for x in ["iran"]):
        return utc_plus_3_30()
# UTC +4
    elif any(x in country for x in ["armenia", "azerbaijan", "crozet islands", "glorioso islands", "tromelin island", "reunion", "georgia", "mauritius", "oman", "seychelles", "united arab emirates", "uae"]):
        return utc_plus_4()
# UTC +4:30
    elif any(x in country for x in ["afghanistan"]):
        return utc_plus_4_30()
# # UTC +5
    elif any(x in country for x in ["ile amsterdam", "ile saint-paul", "kerguelen islands", "maldives", "pakistan", "tajikistan", "turkmenistan", "uzbekistan"]):
        return utc_plus_5()
# UTC +5:30
    elif any(x in country for x in ["india", "sri lanka"]):
        return utc_plus_5_30()
# UTC +5:45
    elif any(x in country for x in ["nepal"]):
        return utc_plus_5_45()
# UTC +6
    elif any(x in country for x in ["bangladesh", "bhutan", "kyrgyzstan", "british indian ocean territory"]):
        return utc_plus_6()
# UTC +6:30
    elif any(x in country for x in ["cocos islands", "keeling islands", "cocos keeling islands", "cocos (keeling) islands", "myanmar", "burma"]):
        return utc_plus_6_30()
# UTC +7
    elif any(x in country for x in ["christmas islands", "cambodia", "laos", "thailand", "vietnam"]):
        return utc_plus_7()
# UTC +8
    elif any(x in country for x in ["brunei", "china", "hong kong", "malaysia", "philippines", "singapore", "taiwan"]):
        return utc_plus_8()
# UTC +9
    elif any(x in country for x in ["japan", "north korea", "palau", "south korea", "timor leste", "timor-liste"]):
        return utc_plus_9()
# UTC +10
    elif any(x in country for x in ["tasmania", "guam", "northern mariana islands"]):
        return utc_plus_10()
# UTC +10:30
    elif any(x in country for x in ["lord howe island"]):
        return utc_plus_10_30()
# UTC +11
    elif any(x in country for x in ["norfolk island", "new caledonia", "solomon islands", "vanuatu"]):
        return utc_plus_11()
# UTC +12
    elif any(x in country for x in ["wallis and futuna", "fiji", "gilbert islands", "marshall islands", "nauru", "new zealand", "tuvalu", "wake islands"]):
        return utc_plus_12()
# UTC +12:45
    elif any(x in country for x in ["chatham islands"]):
        return utc_plus_12_45_45()
# UTC +13
    elif any(x in country for x in ["phoenix islands", "tokelau", "samoa", "tonga"]):
        return utc_plus_13()
# UTC +14
    elif any(x in country for x in ["line islands"]):
        return utc_plus_14()

    else:
        return none

# functions for UTC +  timezones.

def utc_plus_0():
    '''function to find and return the current UTC time'''
    utc_plus_0 = timezone('Etc/GMT')
    utc_0 = datetime.now(utc_plus_0)
    return utc_0.strftime(fmt)
utc_plus_0()

def utc_plus_1():
    '''function to find and return the current UTC+1 time'''
    utc_plus_1 = timezone('Etc/GMT-1')
    utc_1 = datetime.now(utc_plus_1)
    return utc_1.strftime(fmt)
utc_plus_1()

def utc_plus_2():
    '''function to find and return the current UTC+2 time'''
    utc_plus_2 = timezone('Etc/GMT-2')
    utc_2 = datetime.now(utc_plus_2)
    return utc_2.strftime(fmt)
utc_plus_2()

def utc_plus_3():
    '''function to find and return the current UTC+3 time'''
    utc_plus_3 = timezone('Etc/GMT-3')
    utc_3 = datetime.now(utc_plus_3)
    return utc_3.strftime(fmt)
utc_plus_3()

def utc_plus_4():
    '''function to find and return the current UTC+4 time'''
    utc_plus_4 = timezone('Etc/GMT-4')
    utc_4 = datetime.now(utc_plus_4)
    return utc_4.strftime(fmt)
utc_plus_4()

def utc_plus_5():
    '''function to find and return the current UTC+5 time'''
    utc_plus_5 = timezone('Etc/GMT-5')
    utc_5 = datetime.now(utc_plus_5)
    return utc_5.strftime(fmt)
utc_plus_5()

def utc_plus_6():
    '''function to find and return the current UTC+6 time'''
    utc_plus_6 = timezone('Etc/GMT-6')
    utc_6 = datetime.now(utc_plus_6)
    return utc_6.strftime(fmt)
utc_plus_6()

def utc_plus_7():
    '''function to find and return the current UTC+7 time'''
    utc_plus_7 = timezone('Etc/GMT-7')
    utc_7 = datetime.now(utc_plus_7)
    return utc_7.strftime(fmt)
utc_plus_7()

def utc_plus_8():
    '''function to find and return the current UTC+8 time'''
    utc_plus_8 = timezone('Etc/GMT-8')
    utc_8 = datetime.now(utc_plus_8)
    return utc_8.strftime(fmt)
utc_plus_8()

def utc_plus_9():
    '''function to find and return the current UTC+9 time'''
    utc_plus_9 = timezone('Etc/GMT-9')
    utc_9 = datetime.now(utc_plus_9)
    return utc_9.strftime(fmt)
utc_plus_9()

def utc_plus_10():
    '''function to find and return the current UTC+10 time'''
    utc_plus_10 = timezone('Etc/GMT-10')
    utc_10 = datetime.now(utc_plus_10)
    return utc_10.strftime(fmt)
utc_plus_10()

def utc_plus_11():
    '''function to find and return the current UTC+11 time'''
    utc_plus_11 = timezone('Etc/GMT-11')
    utc_11 = datetime.now(utc_plus_11)
    return utc_11.strftime(fmt)
utc_plus_11()

def utc_plus_12():
    '''function to find and return the current UTC+12 time'''
    utc_plus_12 = timezone('Etc/GMT-12')
    utc_12 = datetime.now(utc_plus_12)
    return utc_12.strftime(fmt)
utc_plus_12()

def utc_plus_13():
    '''function to find and return the current UTC+13 time'''
    utc_plus_13 = timezone('Etc/GMT-13')
    utc_13 = datetime.now(utc_plus_13)
    return utc_13.strftime(fmt)
utc_plus_13()

def utc_plus_14():
    '''function to find and return the current UTC+14 time'''
    utc_plus_14 = timezone('Etc/GMT-14')
    utc_14 = datetime.now(utc_plus_14)
    return utc_14.strftime(fmt)
utc_plus_14()

# functions for UTC - timezones.

def utc_minus_1():
    '''function to find and return the current UTC-1 time'''
    utc_minus_1 = timezone('Etc/GMT+1')
    utc_1 = datetime.now(utc_minus_1)
    return utc_1.strftime(fmt)
utc_minus_1()

def utc_minus_2():
    '''function to find and return the current UTC-2 time'''
    utc_minus_2 = timezone('Etc/GMT+2')
    utc_2 = datetime.now(utc_minus_2)
    return utc_2.strftime(fmt)
utc_minus_2()

def utc_minus_3():
    '''function to find and return the current UTC-3 time'''
    utc_minus_3 = timezone('Etc/GMT+3')
    utc_3 = datetime.now(utc_minus_3)
    return utc_3.strftime(fmt)
utc_minus_3()

def utc_minus_4():
    '''function to find and return the current UTC-4 time'''
    utc_minus_4 = timezone('Etc/GMT+4')
    utc_4 = datetime.now(utc_minus_4)
    return utc_4.strftime(fmt)
utc_minus_4()

def utc_minus_5():
    '''function to find and return the current UTC-5 time'''
    utc_minus_5 = timezone('Etc/GMT+5')
    utc_5 = datetime.now(utc_minus_5)
    return utc_5.strftime(fmt)
utc_minus_5()

def utc_minus_6():
    '''function to find and return the current UTC-6 time'''
    utc_minus_6 = timezone('Etc/GMT+6')
    utc_6 = datetime.now(utc_minus_6)
    return utc_6.strftime(fmt)
utc_minus_6()

def utc_minus_7():
    '''function to find and return the current UTC-7 time'''
    utc_minus_7 = timezone('Etc/GMT+7')
    utc_7 = datetime.now(utc_minus_7)
    return utc_7.strftime(fmt)
utc_minus_7()

def utc_minus_8():
    '''function to find and return the current UTC-8 time'''
    utc_minus_8 = timezone('Etc/GMT+8')
    utc_8 = datetime.now(utc_minus_8)
    return utc_8.strftime(fmt)
utc_minus_8()

def utc_minus_9():
    '''function to find and return the current UTC-9 time'''
    utc_minus_9 = timezone('Etc/GMT+9')
    utc_9 = datetime.now(utc_minus_9)
    return utc_9.strftime(fmt)
utc_minus_9()

def utc_minus_10():
    '''function to find and return the current UTC-10 time'''
    utc_minus_10 = timezone('Etc/GMT+10')
    utc_10 = datetime.now(utc_minus_10)
    return utc_10.strftime(fmt)
utc_minus_10()

def utc_minus_11():
    '''function to find and return the current UTC-11 time'''
    utc_minus_11 = timezone('Etc/GMT+11')
    utc_11 = datetime.now(utc_minus_11)
    return utc_11.strftime(fmt)
utc_minus_11()

def utc_minus_12():
    '''function to find and return the current UTC-12 time'''
    utc_minus_12 = timezone('Etc/GMT+12')
    utc_12 = datetime.now(utc_minus_12)
    return utc_12.strftime(fmt)
utc_minus_12()

#Functions for oddball timezones: UTC+/- 00:15, 00:30, 00:45.

def utc_minus_9_30():
    '''function to find and return the current UTC -9:30 time'''
    utc_minus_9_30 = timezone('Pacific/Marquesas')
    utc_9_30 = datetime.now(utc_minus_9_30)
    return utc_9_30.strftime(fmt)
utc_minus_9_30()

def utc_minus_3_30():
    '''function to find and return the current UTC -3:30 time'''
    utc_minus_3_30 = timezone('Canada/Newfoundland')
    utc_3_30 = datetime.now(utc_minus_3_30)
    return utc_3_30.strftime(fmt)
utc_minus_3_30()

def utc_plus_3_30():
    '''function to find and return the current UTC +3:30 time'''
    utc_plus_3_30 = timezone('Iran')
    utc_3_30 = datetime.now(utc_plus_3_30)
    return utc_3_30.strftime(fmt)
utc_plus_3_30()

def utc_plus_4_30():
    '''function to find and return the current UTC +4:30 time'''
    utc_plus_4_30 = timezone('Asia/Kabul')
    utc_4_30 = datetime.now(utc_plus_4_30)
    return utc_4_30.strftime(fmt)
utc_plus_4_30()

def utc_plus_5_30():
    '''function to find and return the current UTC +5:30 time'''
    utc_plus_5_30 = timezone('Indian/Mahe')
    utc_5_30 = datetime.now(utc_plus_5_30)
    return utc_5_30.strftime(fmt)
utc_plus_5_30()

def utc_plus_5_45():
    '''function to find and return the current UTC +5:45 time'''
    utc_plus_5_45 = timezone('Asia/Kathmandu')
    utc_5_45 = datetime.now(utc_plus_5_45)
    return utc_5_45.strftime(fmt)
utc_plus_5_45()

def utc_plus_6_30():
    '''function to find and return the current UTC +6:30 time'''
    utc_plus_6_30 = timezone('Indian/Cocos')
    utc_6_30 = datetime.now(utc_plus_6_30)
    return utc_6_30.strftime(fmt)
utc_plus_6_30()

def utc_plus_8_45():
    '''function to find and return the current UTC +8:45 time'''
    utc_plus_8_45 = timezone('Australia/Eucla')
    utc_8_45 = datetime.now(utc_plus_8_45)
    return utc_8_45.strftime(fmt)
utc_plus_8_45()

def utc_plus_9_30():
    '''function to find and return the current UTC +9:30 time'''
    utc_plus_9_30 = timezone('Australia/Broken_Hill')
    utc_9_30 = datetime.now(utc_plus_9_30)
    return utc_9_30.strftime(fmt)
utc_plus_9_30()

def utc_plus_10_30():
    '''function to find and return the current UTC +10:30 time'''
    utc_plus_10_30 = timezone('Australia/Lord_Howe')
    utc_10_30 = datetime.now(utc_plus_10_30)
    return utc_10_30.strftime(fmt)
utc_plus_10_30()

def utc_plus_12_45():
    '''function to find and return the current UTC +12:45 time'''
    utc_plus_12_45 = timezone('Pacific/Chatham')
    utc_12_45 = datetime.now(utc_plus_12_45)
    return utc_12_45.strftime(fmt)
utc_plus_12_45()
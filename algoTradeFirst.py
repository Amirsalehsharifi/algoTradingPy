from typing import Counter


ethC10Days=[1826,1814,1817,1821,1880,1938,1930,1929,1941,1934]
ethO10Days=[1814,1817,1821,1880,1938,1930,1929,1941,1934,1988]
ethL10Days=[1802,1805,1763,1807,1879,1924,1913,1927,1934,1925]
ethH10Days=[1837,1835,1843,1880,1972,1944,1945,1958,1959,1999]

counter=int(input("Enter candle position"))
shadowDown=ethO10Days[counter]-ethL10Days[counter]
shadowUp=ethH10Days[counter]-ethO10Days[counter]
if shadowDown > shadowUp:
    print("Buy")
elif shadowUp > shadowDown :
        print("sell")
else:
    print("no trade")
        

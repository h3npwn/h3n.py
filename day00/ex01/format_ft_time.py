from datetime import datetime

date = datetime.today()
datx = date.timestamp() #toget my timestamps in floatpoints as unix second from eboch btw "1970";
str = f" Seconds since January 1, 1970: {datx:,.4f}"
str2 = f"or {datx:,.2e} in scientific notation\n"
print(str,str2,date.strftime("%b %d %Y"))

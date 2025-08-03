from datetime import datetime, timezone, timedelta
import pytz

# Usando pytz
date_sp = datetime.now(tz=pytz.timezone('America/Sao_Paulo'))
date_oslo = datetime.now(tz=pytz.timezone('Europe/Oslo'))

# Usando datetime
date_sp = datetime.now(timezone(timedelta(hours=2)))
date_oslo = datetime.now(timezone(timedelta(hours=-3)))

print(date_sp)
print(date_oslo)

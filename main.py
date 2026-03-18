from src.extract import Extract
from src.load import Load

ext = Extract()
ld = Load()

ch = ext.extract_country('China')
ld.create_sqlite_table(ch, "univerdades", "unir_ch")

fr = ext.extract_country('France')
ld.create_sqlite_table(fr, "univerdades", "unir_fr")

it = ext.extract_country('Italy')
ld.create_sqlite_table(it, "univerdades", "unir_it")

import pandas as pd
import statistics
import matplotlib.pyplot as plt


# Lecture CSV file 
file_path = 'jfreechart-test-stats.csv'
#Pour separer les columns
df = pd.read_csv(file_path, delimiter=',', skiprows=1, header=None)

#column names 
column_names = ['class', 'TLOC', 'WMC', 'TASSERT']  # Adjust based on your actual column names

df.columns = column_names

# ajoute tout les TLOC, WMC, TASSERT dans leurs array assign
tloc_values = df['TLOC'].tolist()
wmc_values = df['WMC'].tolist()
tassert_values = df['TASSERT'].tolist()

#avec l'aide de statistics calcule la mediane et la retourne
tloc_mediane = str(statistics.median(tloc_values))

wmc_mediane = str(statistics.median(wmc_values))

tassert_mediane = str(statistics.median(tassert_values))

print("mediane pour TLOC : " + tloc_mediane)

print("mediane pour WMC : " + wmc_mediane)

print("mediane pour TASSERT : " + tassert_mediane)


data = {
    'TLOC': tloc_values,
    'WMC': wmc_values,
    'TASSERT': tassert_values,
}

df = pd.DataFrame(data)

# Création des boîtes à moustaches
plt.boxplot([df['TLOC'], df['WMC'], df['TASSERT']], labels=['TLOC', 'WMC', 'TASSERT'])

# Ajoutez un titre et des étiquettes d'axe
plt.title('Boîtes à moustaches pour TLOC, WMC et TASSERT')
plt.xlabel('Métriques')
plt.ylabel('NombreS')

# Affichez la boîte à moustaches
plt.show()


#source : https://www.w3schools.com/python/ref_stat_median.asp#:~:text=The%20statistics.,in%20a%20set%20of%20data.
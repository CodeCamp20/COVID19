import matplotlib.pyplot as plt
import pandas as pd
covid_data= pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/03-17-2020.csv')
covid_data['Active'] = covid_data['Confirmed'] - covid_data['Deaths'] - covid_data['Recovered']
result = covid_data.groupby('Country/Region')['Confirmed', 'Deaths', 'Recovered', 'Active'].sum().reset_index()
#print(result) 
names = covid_data['Country/Region']
values = covid_data['Active']
#plt.subplot(131)
plt.figure(figsize=(159, 159))
plt.bar(names,values, width=0.5,align='center', linewidth=3.0, alpha=1)
plt.xticks(names)
plt.show()

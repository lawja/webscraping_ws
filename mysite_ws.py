from bs4 import BeautifulSoup
import urllib
import matplotlib.pyplot as plt

page = urllib.request.urlopen('http://www.jlawrence.co/ws').read()

soup = BeautifulSoup(page, "html5lib")

ages = soup.find_all("td", class_="age")
weights = soup.find_all("td", class_="weight")

ages_int = []
weights_int = []

for a in ages:
    ages_int.append(int(a.text))

for w in weights:
    weights_int.append(int(w.text))


plt.plot(ages_int,weights_int)
plt.ylabel('Weight')
plt.xlabel('Age')
plt.show()
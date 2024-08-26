import pandas as pd
import matplotlib.pyplot as plt

file = open("ciphertext.txt", "rt")

freqletters = "eariotnslcudpmhgbfywkvxzjq"


freq = {'a': 0, 
        'b': 0,
        'c': 0,
        'd': 0,
        'e': 0,
        'f': 0,
        'g': 0,
        'h': 0,
        'i': 0,
        'j': 0,
        'k': 0,
        'l': 0,
        'm': 0,
        'n': 0,
        'o': 0,
        'p': 0,
        'q': 0,
        'r': 0,
        's': 0,
        't': 0,
        'u': 0,
        'v': 0,
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0}



for line in file:
  line = line.strip()
  for letter in line:
    if letter in freq:
      freq[letter] += 1
      

# Convert the dictionary to a pandas DataFrame
df = pd.DataFrame.from_dict(freq, orient='index', columns=['Frequency'])

# Sort the DataFrame by frequency in descending order
df = df.sort_values(by='Frequency', ascending=False)

# Plot the histogram
plt.bar(df.index, df['Frequency'])
plt.xlabel('Letter')
plt.ylabel('Frequency')
plt.title('Frequency of Letters')
plt.show()


for item in pd.DataFrame.itertuples(df):
  print(item)
  print(item, " --> ", freqletters[])
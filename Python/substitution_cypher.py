import pandas as pd
import matplotlib.pyplot as plt

file = open("Python/ciphertext.txt", "rt")

#letters in order of frequency
freqletters = "eitoasnrlcudpmhgbfywkvxzjq"

#dictionary to store the frequency of each letter
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


#count the frequency of each letter in the file
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
#plt.show()


#create a decrypted file

#need to create a keymap
#need to iterate through the encrypted file and replace each letter with its match
#need to write the decrypted file

keymap = pd.DataFrame()

data = []
for index, item in enumerate(pd.DataFrame.itertuples(df)):
  #print(item[0], " --> ", freqletters[index])
  data.append([item[0], freqletters[index]])

keymap = pd.DataFrame(data, columns=['Encrypted', 'Decrypted'])


decrypted_text = ""

file = open("Python/ciphertext.txt", "rt")

for line in file:
  line = line.strip()
  for letter in line:
    if letter in keymap['Encrypted'].values:
      row = keymap.loc[keymap['Encrypted'] == letter]
      decrypted_text += row['Decrypted'].values[0]
    else:
      decrypted_text += letter

print(decrypted_text)

decrypted_file = open("Python/decrypted.txt", "wt")
decrypted_file.write(decrypted_text)
decrypted_file.close()

def premier(mot):
    for i in range(0, len(mot)):
        if mot[i] in '0123456789':
            return mot[i]
            break

def dernier(mot):
    for i in range(len(mot)-1, -1, -1):
        if mot[i] in '0123456789':
            return mot[i]
            break

s = 0


with open('data.txt', 'r') as file:
    for line in file:
        line = line.strip() 
        if line:  
            ch = premier(line) + dernier(line)
            s += int(ch)  

print("Somme totale=:", s)

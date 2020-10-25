import math

data = []
test_data = []

#./bases/train_59.data
with open('teste2.data', 'r') as f:
    for lines in f.readlines():
        atributos = lines.strip('\n').split(',')
        data.append([(x) for x in atributos])

with open('./bases/test_59.data', 'r') as f:
    for lines in f.readlines():
        atributos = lines.strip('\n').split(',')
        test_data.append([(x) for x in atributos])

#Classes: forro,rap,sertanejo,samba,axe,bossa_nova

#print(test_data)

def database_info(data, verbose=True):
    class_forro, class_rap, class_sertanejo = 0, 0, 0
    class_samba, class_axe, class_bossa_nova = 0, 0, 0
    size_data = len(data)
    for classe in data:
        if classe[-1] == 'forro':
            class_forro += 1
        elif classe[-1] == 'rap':
            class_rap += 1
        elif classe[-1] == 'sertanejo':
            class_sertanejo += 1
        elif classe[-1] == 'samba':
            class_samba += 1 
        elif classe[-1] == 'axe':
            class_axe += 1
        else:
            class_bossa_nova += 1
    if verbose:
        print(size_data)
        print(class_forro)
        print(class_rap)
        print(class_sertanejo)
        print(class_samba)
        print(class_axe)
        print(class_bossa_nova)
    return size_data

#database_info(data)

def dist_euclidiana(p1, p2):
    tam, somatorio = len(p1), 0
    for index in range(tam - 1):
        somatorio += math.pow((float(p1[index])) - float(p2[index]), 2)
           

    return math.sqrt(somatorio)

def knn(B, X, K):
    distancias = {}
    for i in range(len(B)):
        d = dist_euclidiana(B[i], X)
        distancias[i] = float("%.1f" %d)
        #distancias.append(d)
    
   
    print(distancias)
    k_vizinhos = sorted(distancias, key=distancias.get) [:K]

   
    print(k_vizinhos)

    class_forro, class_rap, class_sertanejo = 0, 0, 0
    class_samba, class_axe, class_bossa_nova = 0, 0, 0
    
 
    for index in k_vizinhos:
        if B[0][-1] == 'forro':
            class_forro += 1
        elif B[index][-1] == 'rap':
            class_rap += 1
        elif B[index][-1] == 'sertanejo':
            class_sertanejo += 1
        elif B[index][-1] == 'samba':
            class_samba += 1
        elif B[index][-1] == 'axe':
            class_axe += 1
        else:
            class_bossa_nova += 1

    print(class_forro)
    print(class_rap)
    print(class_sertanejo)
    print(class_samba)
    print(class_axe)
    print(class_bossa_nova)
    
    classes = {class_forro: "Forro", class_rap: "Rap", class_sertanejo: "Sertanejo", class_samba: "Samba", 
                class_axe: "Axe", class_bossa_nova: "Bossa Nova"}


    final = max(classes)
    print(classes[final])
  
test_set =['0.105427', '0.011920', '0.004542', '0.004157', '0.038710', '0.004929', '0.003536', 
'0.004924', '0.005008', '0.002890', '0.002276', '0.012975', '0.005249', '0.004302', '0.003201', 
'0.003844', '0.005252', '0.005366', '0.009262', '0.007713', '0.003259', '0.005614', '0.040116', 
'0.005543', '0.004365', '0.007894', '0.011015', '0.004688', '0.006485', '0.004489', '0.004256', 
'0.008006', '0.006416', '0.002812', '0.005359', '0.031842', '0.005424', '0.004126', '0.006764', 
'0.010242', '0.003975', '0.006114', '0.003572', '0.002822', '0.003240', '0.004008', '0.008755', 
'0.003115', '0.003994', '0.005932', '0.006311', '0.003501', '0.005894', '0.032992', '0.004959', 
'0.007008', '0.009491', '0.157076', '0.303046', 'samba']
teste_set2 = ['2','3','3','2']
teste_set3 = ['55','58', '0']
knn(data, teste_set3, 12)

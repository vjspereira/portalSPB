import csv
import os
import subprocess
 
results = []
dados = []
with open('gits.csv') as File:
    reader = csv.DictReader(File)
    for row in reader:
        results.append(row)
    
counter =0
with open('commits.csv', 'w') as csvfile:
    fieldnames = ['projeto', 'hash', 'usuario','data']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for result in results:
        if counter < 500:
            try:
                os.system('git clone '+result['GIT']+' ./repositorios/repo'+str(counter))
                output = subprocess.check_output("cd ./repositorios/repo"+str(counter)+" && git log --date=format:'%d/%m/%y' --pretty=format:'%h; %an; %ad'", shell=True)


                #Se o repositorio nao eh vazio
                if output:
                    dados = str(output).replace("/n",';').replace("\n",';').split(';')
                    if len(dados) == 3:
                        writer.writerows([{'projeto': result['GIT'],
                                               'hash': dados[0],
                                               'usuario': dados[1],
                                               'data': dados[2]}])
                    else:
                        for i in range(0,len(dados)-3,3):
                            writer.writerows([{'projeto': result['GIT'],
                                                   'hash': dados[i],
                                                   'usuario': dados[i+1],
                                                   'data': dados[i+2]}])


                os.system('sudo rm -R ./repositorios/repo'+str(counter))
                counter+=1
            except:
                os.system('sudo rm -R ./repositorios/repo'+str(counter))
                counter+=1
            
            

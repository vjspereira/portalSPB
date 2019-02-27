# Scripts mineração do Portal SPB
Projeto contendo os scripts utilizados para extração dos commits e colaboração do Portal do Software Público Brasileiro.

# Extração de Commits

O script python commits_extract.py é responsável pela extração completa do histório de commits de cada repositório pertencente ao arquivo gits.csv. Neste caso, o csv já está preenchido com os repositórios do Portal SPB até a data de maio de 2018. Porém, o arquivo pode possuir qualquer repositório git.
Cada repositório será clonado e terá a lista de commits inserida em um arquivo de commits mestre. Após a escrita, o clone será apagado.

# Extração de Colaboração

O shell script collaboration_extract.sh realiza a extração da tupla user/file_altered para todas os commits já realizados no repositório. O script deve ser rodado dentro de cada repositório. No fim de cada execução, será gerado um output em csv com os dados.

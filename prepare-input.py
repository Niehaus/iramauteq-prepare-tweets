import os
import sys

hashtag = sys.argv[1]
data_inicial = sys.argv[2]  # 2020-01-01
data_final = sys.argv[3] # 2020-12-31
max_tweets = sys.argv[4]
arquivo = sys.argv[5]

# print('a procura será \n snscrape --jsonl --max-results ' + max_tweets + ' twitter-search "#' + hashtag + ' since:' + data_inicial + ' until:'+ data_final+ '" > arquivodestino.json"')
print("Paramêtros")
print("Hashtag: ", hashtag)
print("Data Inicial: ", data_inicial)
print("Data Inicial: ", data_final)
print("Máximo de Tweets: ", max_tweets)

os.system('echo "$(snscrape --jsonl --max-results ' + max_tweets + ' twitter-search "#' + hashtag + ' since:' + data_inicial + ' until:'+ data_final+ '" > ' + arquivo +'.json)"')
print("Busca Finalizada => Arquivo de Saíoda:", arquivo)


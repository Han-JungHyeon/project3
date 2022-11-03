import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

data = pd.read_csv('weart_data.csv')

tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(data['Hash_tag'])
# print('TF-IDF 행렬의 크기(shape) :',tfidf_matrix.shape)

cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
# print('코사인 유사도 연산 결과 :',cosine_sim.shape)

title_to_index = dict(zip(data['Title'], data.index))

def get_recommendations(title, cosine_sim=cosine_sim):
    # 선택한 그림의 타이틀로부터 해당 그림의 인덱스를 받아온다.
    idx = title_to_index[title]

    # 해당 그림와 모든 그림와의 유사도를 가져온다.
    sim_scores = list(enumerate(cosine_sim[idx]))

    # 유사도에 따라 그림들을 정렬한다.
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # 가장 유사한 5개의 그림를 받아온다.
    sim_scores = sim_scores[1:6]

    # 가장 유사한 5개의 그림의 인덱스를 얻는다.
    movie_indices = [idx[0] for idx in sim_scores]

    # 가장 유사한 5개의 그림의 제목을 리턴한다.
    return data[['Title', 'Artist', 'URL', 'img']].iloc[movie_indices]

print(get_recommendations('과일 그릇과 신문'))


import pickle

with open('model.pkl', 'wb') as f:
    pickle.dump(cosine_sim, f)
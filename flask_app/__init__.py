from flask import Flask, render_template, request
import pickle
import pandas as pd

def create_app():

    data = pd.read_csv('weart_data.csv')
    model = None
    with open('model.pkl', 'rb') as pf:
        model = pickle.load(pf)
    title_to_index = dict(zip(data['Title'], data.index))

    app = Flask(__name__)

    @app.route('/')
    def home():
        return render_template('home.html')

    @app.route('/predict', methods=['POST'])
    def get_recommendations():
        cosine_sim=model
        title = request.form['title']
        idx = title_to_index[title]
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:6]
        movie_indices = [idx[0] for idx in sim_scores]
        pred = data[['Title', 'Artist', 'URL', 'img']].iloc[movie_indices]
        pred_t1 = pred.iloc[0, 0]
        pred_a1 = pred.iloc[0, 1]
        pred_u1 = pred.iloc[0, 2]
        pred_i1 = pred.iloc[0, 3]
        pred_t2 = pred.iloc[1, 0]
        pred_a2 = pred.iloc[1, 1]
        pred_u2 = pred.iloc[1, 2]
        pred_i2 = pred.iloc[1, 3]
        pred_t3 = pred.iloc[2, 0]
        pred_a3 = pred.iloc[2, 1]
        pred_u3 = pred.iloc[2, 2]
        pred_i3 = pred.iloc[2, 3]
        pred_t4 = pred.iloc[3, 0]
        pred_a4 = pred.iloc[3, 1]
        pred_u4 = pred.iloc[3, 2]
        pred_i4 = pred.iloc[3, 3]
        pred_t5 = pred.iloc[4, 0]
        pred_a5 = pred.iloc[4, 1]
        pred_u5 = pred.iloc[4, 2]
        pred_i5 = pred.iloc[4, 3]
        x = data[['Title', 'Artist', 'img']].iloc[idx]
        x_t = x.iloc[0]
        x_a = x.iloc[1]
        x_i = x.iloc[2]
        return render_template('pred.html', pred_t1=pred_t1, pred_a1=pred_a1, pred_u1=pred_u1, pred_i1=pred_i1, pred_t2=pred_t2, pred_a2=pred_a2, pred_u2=pred_u2, pred_i2=pred_i2, pred_t3=pred_t3, pred_a3=pred_a3, pred_u3=pred_u3, pred_i3=pred_i3, pred_t4=pred_t4, pred_a4=pred_a4, pred_u4=pred_u4, pred_i4=pred_i4, pred_t5=pred_t5, pred_a5=pred_a5, pred_u5=pred_u5, pred_i5=pred_i5, x_t=x_t, x_a=x_a, x_i=x_i)
    
    return app
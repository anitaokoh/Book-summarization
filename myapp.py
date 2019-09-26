from flask import Flask, render_template,request
# from flask_bootstrap import Bootstrap
import pandas as pd
# from bokeh.plotting import figure
# from bokeh.embed import components

df = pd.read_csv('data/book1_df.csv')
emotions = df['emotion_label'].values.tolist()
chapters = df['chapter'].values.tolist()

# def create_figure(x, y):
#     p = figure(plot_width = 400, plot_height = 400)
#     p.line(x, y,
#         line_width = 2, color = "green")
    # p.xaxis.axis_label = 'Chapters'
    #
	# # Set the y axis label
	# p.yaxis.axis_label = 'Emotion'
    # return p


app = Flask(__name__)
# Bootstrap(app)
# app.run(debug=True)

@app.route('/')
def home():
    books = ['The Subtle Art of not giving a fuck by Mark',
    'Think Like A Freak by Steven_D._Levit']
    return render_template("main.html", BOOKS=books)

@app.route('/summary')
def summary():
#     print(dict(request.args))
    new = dict(request.args)
    # print(list(new.keys())[0])
    # choice = new['title']
    # # chapter = new.get("chapter","1")
    # new_df = df[df['chapter']==1]
    # summary = new_df['summary_5'][0]
    # chapter = new["chapter"]
    # new_df = df[df['chapter']==int(chapter)]
    # summary = new_df['summary_5'][0]


    if list(new.keys())[0] == 'title':
        choice = new["title"]
        new_df = df[df['chapter']==1]
        CHAPTERS = new_df['Chapter'].values[0]
        sub_title = new_df['Sub_title'].values[0]
        summary = new_df['summary_5'].values[0]
        emo = new_df['emotion_analysis_10'].values[0]
    else:
        # list(new.keys())[0] == 'chapter':
        choice=df['Title'].values[0]
        chapter = new["chapter"]
        new_df = df[df['chapter']==int(chapter)]
        CHAPTERS = new_df['Chapter'].values[0]
        sub_title = new_df['Sub_title'].values[0]
        summary = new_df['summary_5'].values[0]
        emo = new_df['emotion_analysis_10'].values[0]
    return render_template("summary.html", CHOICE=choice, CHAPTERS=CHAPTERS, SUBTITLE=sub_title, summary=summary, EMO=emo)


if __name__ == '__main__':
    app.run(debug=True)
# @app.route('/viz')
# def visualization():
#     plot = create_figure(emotions,chapters)
#     script, div = components(plot)
#     return render_template("viz.html", script=script, div=div)

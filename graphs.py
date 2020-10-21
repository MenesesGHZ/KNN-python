import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

def display_knn_graph(X,Y,points,predictions,category_names,category_colors):

    # Sorting Data
    points1 = np.array([ X[i] for i in range(len(Y)) if Y[i] == 0 ])
    x1 = points1[:,0]
    y1 = points1[:,1]

    points2 = np.array([ X[i] for i in range(len(Y)) if Y[i] == 1 ])
    x2 = points2[:,0]
    y2 = points2[:,1]


    # Creating and Configuring Graph layout
    n_subgraphs = 3
    fig = make_subplots(rows=1, cols=n_subgraphs)
    fig.update_layout(
        autosize=True,
        height=500,
    )

    # Creating traces
    name_trace_1 = category_names[0]+" point"
    name_trace_2 = category_names[1]+" point"
    trace_1 = go.Scatter(x=x1, y=y1,name=name_trace_1,mode='markers',marker_size=35,marker_color=category_colors[category_names[0]])
    trace_2 =  go.Scatter(x=x2, y=y2, name=name_trace_2,mode='markers',marker_size=35,marker_color=category_colors[category_names[1]])


    # Creating predicted traces and adding all traces to the figure
    for i in range(n_subgraphs):
        # creating predicted trace
        x = points[i]
        prediction = predictions[i]
        predicted_category = category_names[prediction]
        predicted_trace = go.Scatter(x=[x[0]], y=[x[1]], name=predicted_category+" predicted point",
                    mode='markers',marker_size=40,marker_color=category_colors[predicted_category+"_pred"]
                    )
        # Adding traces
        trace_1.name = name_trace_1 + " " + str(i)
        trace_2.name = name_trace_2 + " " +str(i)
        fig.add_trace(trace_1,row=1,col=i+1)
        fig.add_trace(trace_2,row=1,col=i+1)
        fig.add_trace(predicted_trace,row=1,col=i+1)


    fig.show()
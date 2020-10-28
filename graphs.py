import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def display_knn_graph(X,y,colors_by_label):
    
    fig = plt.figure(1, figsize=(20, 15))
    ax = Axes3D(fig, elev=48, azim=134)
    colors = [ colors_by_label[label] for label in y]
    print(colors)
    ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=colors, cmap=plt.cm.Set1, edgecolor='k', s=X[:, 3]*50)
    
    for name, label in [('Iris-virginica', 0), ('Iris-setosa', 1), ('Iris-versicolor', 2)]:
        ax.text3D(X[y == label, 0].mean(),
                  X[y == label, 1].mean(),
                  X[y == label, 2].mean(),
                  name,
                  horizontalalignment='center',
                  bbox=dict(alpha=.5, edgecolor='w',
                  facecolor='w'),size=25)

    ax.set_title("3D visualization", fontsize=40)
    ax.set_xlabel("Sepal Length [cm]", fontsize=25)
    ax.w_xaxis.set_ticklabels([])
    ax.set_ylabel("Sepal Width [cm]", fontsize=25)
    ax.w_yaxis.set_ticklabels([])
    ax.set_zlabel("Petal Length [cm]", fontsize=25)
    ax.w_zaxis.set_ticklabels([])

    plt.show()





def display_knn_test_graph(X,Y,points,predictions,category_names,category_colors):

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
        height=500)

    # Creating traces
    name_trace_1 = category_names[0]+" point"
    name_trace_2 = category_names[1]+" point"
    trace_1 = go.Scatter(x=x1, y=y1,name=name_trace_1,mode='markers',marker_size=35,marker_color=category_colors[category_names[0]])
    trace_2 = go.Scatter(x=x2, y=y2, name=name_trace_2,mode='markers',marker_size=35,marker_color=category_colors[category_names[1]])


    # Creating predicted traces and adding all traces to the figure
    for i in range(n_subgraphs):
        # creating predicted trace
        x = points[i]
        prediction = predictions[i]
        predicted_category = category_names[prediction]
        predicted_trace = go.Scatter(x=[x[0]], y=[x[1]], name=predicted_category+" predicted point",
                    mode='markers',marker_size=40,marker_color=category_colors[predicted_category+"_pred"])
        # Adding traces
        trace_1.name = name_trace_1 + " " + str(i)
        trace_2.name = name_trace_2 + " " +str(i)
        fig.add_trace(trace_1,row=1,col=i+1)
        fig.add_trace(trace_2,row=1,col=i+1)
        fig.add_trace(predicted_trace,row=1,col=i+1)


    fig.show()

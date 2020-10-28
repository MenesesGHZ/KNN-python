import numpy as np
import math
from knn import KNN
from graphs import display_knn_graph

def test():
    # Dataset -> Labeled Examples 
    X = np.array([
            [1, 3.6],   #blue
            [2.2, 6.4], #blue
            [3.3, 0.8], #blue
            [3.8, 7.4], #orange
            [4.3, 5.1], #blue
            [5.6, 9.2], #orange
            [5.6, 2.8], #orange
            [6.8, 8.2], #orange
            [6.8, 1.8], #orange
            [7.9, 8.2], #blue
            [7.9, 3.7], #orange
            [9.1, 7.3]  #blue
        ])
    Y = np.array([[1,1,1,0,1,0,0,0,0,1,0,1]]).T

    # Loading Model
    euclidean_norm = lambda v1,v2: math.sqrt(sum((v1-v2)**2))
    knn_model = KNN(X,Y,norm=euclidean_norm,k=5)
    
    # Test Data
    interval = (0,10)
    random_points = np.array([
        np.random.uniform(*interval,2),
        np.random.uniform(*interval,2),
        np.random.uniform(*interval,2)
    ])
    
    # Predictions
    predictions = knn_model.predict(random_points)

    # Display Results with Plotly  
    category_names = ["orange","blue"]
    category_colors = {"orange":"rgba(255,165,0,0.8)",
                        "blue":"rgba(0, 255, 255,0.9)",
                        "blue_pred":"rgba(0,0,255,0.75)",
                        "orange_pred":"rgba(255,70,0,0.8)"}
    display_knn_graph(X,Y,random_points,predictions,category_names,category_colors)



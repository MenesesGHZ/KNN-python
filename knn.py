class KNN():
    def __init__(self,X=list(),Y=list(),norm=None,k=3):
        self.X = X 
        self.Y = Y
        self.norm = norm
        self.k = 3

    def load_data(self,X,Y,norm,k=3):
        self.X = X 
        self.Y = Y
        self.norm = norm
        self.k = 3
    
    def predict(self,X):
        predictions = list()
        for x in X:
            neighbours_distance_index = list()
            
            # Calculating distance between 'x' and 'x_i' 
            for i in range(len(self.X)):
                d = self.norm(x,self.X[i])
                neighbours_distance_index.append((d,i))

            # sorting by shortest distance and picking 'k' nearest neighbours.
            neighbours_distance_index = sorted(neighbours_distance_index)
            k_nearest_neighbours = neighbours_distance_index[:self.k]

            # Getting the label of the 'k' nearest neighbours 
            k_neighbours_label = [self.Y[index][0] for _,index in k_nearest_neighbours]

            # `Predicting`
            labels = list(set(k_neighbours_label))
            max_count = 0
            for label in labels:
                counter = k_neighbours_label.count(label)
                if max_count < counter:
                    prediction = label
                    max_count = counter
            predictions.append(prediction)
        return predictions
    

    
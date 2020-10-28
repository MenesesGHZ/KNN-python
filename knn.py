class KNN():
    def __init__(self,X=list(),Y=list(),norm=None,k=3):
        self.X = X 
        self.Y = Y
        self.norm = norm
        self.k = k
 
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
                # if the label is a string, save the whole label name; else it MUST be numeric, save the number of the class which belongs too. 
            k_neighbours_label = [self.Y[index] if isinstance(self.Y[index],str) else self.Y[index][0] for _,index in k_nearest_neighbours ]
            print(k_neighbours_label)
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
    

    

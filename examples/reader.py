import pandas
def read_dataset(data_path):
    data = pandas.read_csv(data_path)
    train_set = data.iloc[:100,:]
    test_set = data.iloc[100::,:]
    x_train = train_set.iloc[:,0:-1].to_numpy()
    y_train = train_set.iloc[:,-1].to_numpy()
    x_test = train_set.iloc[:,0:-1].to_numpy()
    y_test = train_set.iloc[:,-1].to_numpy()
    return x_train,y_train,x_test,y_test
    

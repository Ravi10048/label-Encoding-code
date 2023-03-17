# Import LabelEncoder (for encoding specific part)
from sklearn import preprocessing

# Creating labelEncoder
le = preprocessing.LabelEncoder()

# Converting string labels into numbers.
data['salary']=le.fit_transform(data['salary'])
data['sales']=le.fit_transform(data['sales'])

save_encoded=data.to_csv("encoded.csv")


//by this we can a csv file but by tfidvectorize output is not a dataframe

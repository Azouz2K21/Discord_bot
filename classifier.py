import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.impute import SimpleImputer

# Load data
data = pd.read_csv('Student Mental health.csv')

# Encode categorical variables
le = LabelEncoder()
data[['Choose your gender','What is your course?','Marital status','Do you have Depression?','Do you have Anxiety?','Do you have Panic attack?','Did you seek any specialist for a treatment?']] = data[['Choose your gender','What is your course?','Marital status','Do you have Depression?','Do you have Anxiety?','Do you have Panic attack?','Did you seek any specialist for a treatment?']].apply(le.fit_transform)

# convert 'Your current year of Study' to numerical values
year_map = {'year 1':1, 'Year 1':1, 'year 2':2, 'Year 2':2, 'year 3':3, 'Year 3':3, 'year 4':4, 'Year 4':4}
data['Your current year of Study'] = data['Your current year of Study'].map(year_map)

# convert 'What is your CGPA?' to numerical values
cgpa_map = {'0.00 - 1.99':1,'2.00 - 2.49':2,'2.50 - 2.99':3,'3.00 - 3.49':4, '3.50 - 4.00':5}
data['What is your CGPA?'] = data['What is your CGPA?'].map(cgpa_map)

# Split data into training and test sets
X = data[['Choose your gender','Age','What is your course?','Your current year of Study','What is your CGPA?','Marital status']]
y = data[['Do you have Depression?','Do you have Anxiety?','Do you have Panic attack?']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
print(X_train)

# Create an imputer with mean strategy
imputer = SimpleImputer(strategy='mean')

# Fit the imputer on the training data
imputer.fit(X_train)

# Transform the training and test data
X_train = imputer.transform(X_train)
X_test = imputer.transform(X_test)

# Train decision tree classifier
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

# Make predictions on test set
y_pred = clf.predict(X_test)
print(X_test)
print(y_pred)
# Calculate accuracy
acc = accuracy_score(y_test, y_pred)
print(f'Accuracy: {acc}')
const LRpkg = require('ml-logistic-regression')
const LogisticRegression = LRpkg.LogisticRegression || LRpkg.default || LRpkg
const { Matrix } = require('ml-matrix')

// > Step 1: Training Data (X = Vector | y = label: 1=postive, 0=negative)
const X = new Matrix([
    [1,0],
    [0,1],
    [2,0],
    [0,3]
])

const y = [1, 0, 1, 0]

// > Step 2: Train model
const logreg = new LogisticRegression({ numStep: 5000, learningRate: 5e-3});
logreg.train(X, y)

// > Step 3: Predict Sentiment
const prediction = logreg.predict(new Matrix([[3, 0]]))
console.log(prediction)
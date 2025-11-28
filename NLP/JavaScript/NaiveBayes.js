/**
 * NaiveBayes using NLP Libraries - Natural (improved)
 */
const natural = require('natural')
const classifier = new natural.BayesClassifier()

// Simple preprocessing: lowercase the text to reduce token sparsity
const preprocess = (s) => (s || '').toLowerCase()

// -- Training data: more varied examples (including negative sentences that contain "love/loved")
classifier.addDocument(preprocess('I love this!'), 'positive')
classifier.addDocument(preprocess('This is terrible. I hate this'), 'negative')
classifier.addDocument(preprocess('My coursera subscription expired :('), 'negative')
classifier.addDocument(preprocess('I miss my old stuffs :('), 'negative')

// Negative examples that contain words like "love" or "loved" to teach context
classifier.addDocument(preprocess('I loved her so much, but she left me'), 'negative')
classifier.addDocument(preprocess('I loved him but he broke my heart :('), 'negative')
classifier.addDocument(preprocess('I loved her and now I feel empty'), 'negative')
classifier.addDocument(preprocess('I loved it, but it ended badly :('), 'negative')

// Positive examples to balance
classifier.addDocument(preprocess('I absolutely love this product'), 'positive')
classifier.addDocument(preprocess('What a fantastic experience, I love it'), 'positive')
classifier.addDocument(preprocess('I am so happy and I love this!'), 'positive')
classifier.addDocument(preprocess('This made me smile :)'), 'positive')

// Emoticons and short tokens
classifier.addDocument(preprocess(':('), 'negative')
classifier.addDocument(preprocess(':-('), 'negative')
classifier.addDocument(preprocess(':)'), 'positive')
classifier.addDocument(preprocess(':-)'), 'positive')

classifier.train()


const print_result = (result, input, classifications) => {
    console.log(`\n|------------- Input Text -------------|\n    >${input}\n|--------------------------------------|\n`)
    // Show confidence scores
    if (classifications && classifications.length) {
        const top = classifications[0]
        const pct = Math.round(top.value * 1000) / 10 // one decimal
        console.log(`Top prediction: ${top.label} (${pct}%)\n`)
        console.log('All scores:', classifications.map(c => `${c.label}: ${c.value.toFixed(4)}`).join(', '))
    }

    if (result === 'positive'){
        console.log(`\nResult:\n

█▀█ █▀█ █▀ █ ▀█▀ █ █░█ █▀▀
█▀▀ █▄█ ▄█ █ ░█░ █ ▀▄▀ ██▄
                `)
    }
    if (result === 'negative'){
        console.log(`\nResult:\n

█▄░█ █▀▀ █▀▀ ▄▀█ ▀█▀ █ █░█ █▀▀
█░▀█ ██▄ █▄█ █▀█ ░█░ █ ▀▄▀ ██▄
                `)
    }
}

const input = "My heart... I loved her :("
const processed = preprocess(input)
const test = classifier.classify(processed)
const classifications = classifier.getClassifications(processed)
print_result(test, input, classifications)

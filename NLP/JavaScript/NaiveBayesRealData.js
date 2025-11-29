const natural = require('natural')
const classifier = new natural.BayesClassifier()
const fs = require('node:fs').promises

const preprocess = s => (s || '')
    .toLowerCase()
    .replace(/https?:\/\/\S+/gi, '')
    .replace(/@\w+/g, '')
    .replace(/[#]/g, '')
    .replace(/\s+/g, ' ')
    .trim()

async function loadTweetsFromFile(path) {
    const raw = await fs.readFile(path, 'utf8')
    // > Try JSON array
    try {
        const parsed = JSON.parse(raw)
        if (Array.isArray(parsed)) return parsed
        // > if parsed is a single onject:
        return [parsed]
    } catch (e) {
        return raw
            .split(/\r?\n/)
            .map(line => line.trim())
            .map(line => {
                try {
                    return JSON.parse(line)
                } catch(_) {
                    return null
                }
            })
            .filter(Boolean)
    }
}

async function buildAndTrain() {
    const negativePath = './twitter_samples/negative_tweets.json'
    const positivePath = './twitter_samples/positive_tweets.json'

    const negTweets = await loadTweetsFromFile(negativePath)
    for (const t of negTweets) {
        const text = t.text || t.full_text || ''
        if (!text.trim()) continue
        classifier.addDocument(preprocess(text), 'negative')
    }

    const posTweets = await loadTweetsFromFile(positivePath)
    for (const t of posTweets) {
        const text = t.text || t.full_text || ''
        if (!text.trim()) continue
        classifier.addDocument(preprocess(text), 'positive')
    }

    classifier.train()
    console.log('Training finished. Documents:', classifier.docs.length)
}

// > Main
function main() {
    const sample = "My heart... I loved her :(";
    const p = preprocess(sample)
    console.log('Input:', sample)
    console.log('Prediction:', classifier.classify(p))
    console.log('Scores:', classifier.getClassifications(p))
}

buildAndTrain()
    .then(() => main())
    .catch(err => console.error('Error:', err))

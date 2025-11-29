const natural = require('natural')
const classifier = new natural.BayesClassifier()
const fs = require('node:fs')

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

fs.readFile('./twitter_samples/negative_tweets.json', 'utf-8', (err, data) => {
    if (err) {
        console.log("Error reading negative_tweets.json");
        return;
    }
    console.log(data);
})

console.log(classifier)
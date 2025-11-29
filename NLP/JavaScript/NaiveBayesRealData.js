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

fs.readFile('./twitter_samples/negative_tweets.json', 'utf-8', (err, data) => {
    if (err) {
        console.log("Error reading negative_tweets.json");
        return;
    }
    console.log(data);
})

console.log(classifier)
const natural = require('natural')
const classifier = new natural.BayesClassifier()
const fs = require('node:fs').promises
const chalk = require('chalk').default || require('chalk')

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
    const sample = "ttnimd";
    const p = preprocess(sample)

    const classifications = classifier.getClassifications(p) || []
    // show raw (very small) scores in exponential form
    if (classifications.length) {
        console.log('Raw scores:', classifications.map(c => `${c.label}: ${c.value.toExponential(3)}`).join(', '))
    } else {
        console.log('Raw scores: -- none --')
    }

    // normalize for clearer percentages
    const sum = classifications.reduce((s, c) => s + c.value, 0)
    let top = classifications[0] || { label: classifier.classify(p), value: 0 }

    if (sum > 0) {
        const normalized = classifications
            .map(c => ({ label: c.label, pct: (c.value / sum) * 100 }))
            .map(n => {
                const col = n.label === 'positive' ? chalk.green : n.label === 'negative' ? chalk.red : chalk.yellow
                return col(`${n.label}: ${n.pct.toFixed(1)}%`)
            })
            .join(', ')
        console.log('Normalized scores:', normalized)

        // choose top by raw value then compute normalized pct for display
        top = classifications.reduce((a, b) => a.value >= b.value ? a : b)
        const topPct = (top.value / sum) * 100
        const formattedPrediction = top.label === 'positive'
            ? chalk.green.bold(`${top.label} (${topPct.toFixed(1)}%)`)
            : top.label === 'negative'
                ? chalk.red.bold(`${top.label} (${topPct.toFixed(1)}%)`)
                : chalk.yellow.bold(`${top.label} (${topPct.toFixed(1)}%)`)
        console.log('Prediction:', formattedPrediction)
    } else {
        // fallback when scores underflow to zero
        const pct = Math.round((top.value || 0) * 1000) / 10
        const formattedPrediction = top.label === 'positive'
            ? chalk.green.bold(`${top.label} (${pct}%)`)
            : top.label === 'negative'
                ? chalk.red.bold(`${top.label} (${pct}%)`)
                : chalk.yellow.bold(`${top.label} (${pct}%)`)
        console.log('Prediction:', formattedPrediction)
    }

    console.log('Input:', sample)
    if (classifications.length) {
        const score = classifications
            .map(c => {
                const col = c.label === 'positive' ? chalk.green : c.label === 'negative' ? chalk.red : chalk.yellow
                // show raw-percent for debug (may be tiny)
                return col(`${c.label}: ${(c.value * 100).toFixed(6)}%`)
            })
            .join(', ')
        console.log('Scores (raw percents):', score)
    } else {
        console.log("Scores: -- not available --")
    }
}

const start = process.hrtime.bigint()

buildAndTrain()
    .then(() => {
        main()
        const end = process.hrtime.bigint()
        const ms = Number(end - start) / 1e6
        console.log(chalk.cyan.bold(`Elapsed time: ${ms.toFixed(1)} ms`))
    })
    .catch(err => console.error('Error:', err))

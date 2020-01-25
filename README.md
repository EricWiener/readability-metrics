# Readability Metrics
This project is based extremely heavily on [mmautner's package](https://github.com/mmautner/readability). Modifications were made to support the analysis of large documents.

## Inspiration
When using mmautner's package, the entire document needed to be passed in at once:
```python
large_str = "...."
rd = Readability(large_str)
print('ARI: ', rd.ARI())
```

However, while doing an analysis of Supreme Court transcripts since 1956 across various metrics, my personal computer was not able to load and the needed documents all at once. In order to account for this, I created this package, which allows for pieces of documents to be passed in. Furthermore, the text is not stored, only the resulting calculations. Lastly, all metrics are calculated and returned each time, so individual calculations don't need to be performed.

## Installation
Readability metrics can be installed from PyPi:
```
$ pip3 install readability-metrics
```

## Usage
Readability metrics can be used as follows (note it is imported as `import metrics`):

```python
import metrics # import package

rdm = metrics.Readability()
rdm.analyze_text("This is a sentence.")
rdm.analyze_text("This is part of the same document.")
rdm.analyze_text("This is also part of the same document.")
rdm.get_results()

# can further modify
rdm.analyze_text("This is also part of the same document.")
rdm.get_results()

# can clear and start new analysis
rdm.clear()
rdm.analyze_text("This is also part of the same document.")
rdm.get_results()
```

You can also calculate readability metrics across multiple categories. For instance, if you had a transcript, you could calculate metrics for all speakers at once:

```python
import metrics
from collections import defaultdict

let transcript = [
    ('John George', 'Words said by John George'),
    ('Apple Dunkin', 'Words said by Apple Dunkin'),
    # ...
]

readability_per_speaker = defaultdict(lambda: metrics.Readability())

# Calculate readability metrics
for dialogue in transcript:
    readability_per_speaker[dialogue[0]].analyze_text(dialogue[1])

# Calculate results
for speaker in readability_per_speaker:
    dic[key] = dic[key].get_results()

# readability_per_speaker now in form:
{
    "SPEAKER NAME": {
        {
            'ARI': 12.163787878787879,
            'FleschReadingEase': 58.2319, 
            'FleschKincaidGradeLevel': 11.2857,
            'GunningFogIndex': 14.5465,
            'SMOGIndex': 12.287087810503355,
            'ColemanLiauIndex': 9.5226,
            'LIX': 46.467171717171716,
            'RIX': 5.375
        }
    },
    # more speakers ...
}
```

## Contribution
Contributions are welcome. Please create a pull request or email me at ericwiener3@gmail.com. Also feel free to create an issue if you need help with something.

## Testing
Testing can be run with pytest. Simple navigate to the directory and run `pytest`.

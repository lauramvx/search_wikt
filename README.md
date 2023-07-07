### Search Wiktionary

A simple command-line tool for searching English Wiktionary using Wiktionary Parser ([click](https://github.com/Suyash458/WiktionaryParser)).

Wiktionary definitions are licensed under CC BY-SA 4.0. Visit wiktionary at wiktionary.org ([click](wiktionary.org)).

This project is currently a work in progress.
#### Installation
To install, type:
```
pip install search_wikt
```
To run the program, type:
```
py -m search_wikt apricot --language English
```
or any other word or language you'd like to search. Run `py -m search_wikt -h` or `--help` for a more detailed explanation.

Alternatively, to clone the repository type:
```
git clone https://github.com/lauramvx/search_wikt
```
then `cd` to the project directory and run:
```
py src\search_wikt\__main__.py apricot --language English
```
##### Examples
```
py -m search_wikt hunig -l "Old English"
```

```
hunig
From Proto-West Germanic *hunag, from Proto-Germanic *hunagą. Cognate with Old Frisian hunig, Old Saxon honeg, and Old High German honag; also Old Norse hunang, from the alternative form *hunangą.

IPA: /ˈxu.nij/, [ˈhu.nij]
noun
huniġ n
honey
```
```
py -m search_wikt ac -l "Old English" -ex
```
```
ac 1
From Proto-Germanic *aiks.

IPA: /ɑːk/
IPA: /ɑk/
noun
āc f
oak (wood or tree)
(poetic) an oaken ship
(masculine) the runic character ᚪ (/a/)
ac 2
From Proto-Germanic *ak.

IPA: /ɑːk/
IPA: /ɑk/
conjunction
ac
but
but instead: in this sense ac should sometimes be translated as "but," but most often it is best left untranslated


Sēo æx forġiett, ac þæt trēow ġeman.The axe forgets, but  the tree remembers.
The axe forgets, but  the tree remembers.
Ne ġēotaþ wē tēaras, ac blōd.We don't shed tears, we shed blood.
We don't shed tears, we shed blood.
Nōn egō, sed tū: “Nā iċ, ac þū.” Nōn bōs est, sed equus: “Nis hit nā oxa, ac is hors.”Non ego, sed tu: “Not me, you.” Non bos est, sed equus: “It's not an ox, it's a horse.”
Non ego, sed tu: “Not me, you.” Non bos est, sed equus: “It's not an ox, it's a horse.”
```

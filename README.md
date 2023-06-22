### Search Wiktionary

A simple command-line tool for searching Wiktionary using WiktionaryParser ([click](https://github.com/Suyash458/WiktionaryParser))

#### Installation
No pip module yet, so you'll have to clone the repository for now.
```
git clone https://github.com/lauramvx/search_wikt
```
Then `cd` to the project directory and run:
```
py src\search_wikt\core.py word [-h, --help] [-l, --language <language>] [-e, --etymology]
[-i, --ipa] [-ex, --examples] [-r, --related] [-d, --default | -rd, --restore_defaults]
```
Run `py src\search_wikt\core.py -h` or `--help` for a more detailed explanation.

##### Examples
```
py src\search_wikt\core.py hunig -l "Old English"
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
py src\search_wikt\core.py ac -l "Old English" -ex -r
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
#### Issues
When attempting to pipe the output to a file I get the following error:
```
UnicodeEncodeError: 'charmap' codec can't encode characters in position 6-7: character maps to <undefined>
```
Attaching the string method `.encode("utf-8")` to the main printed strings (lines 159 and 165) fixes this, but it outputs raw unicode codes instead of characters and it also breaks the terminal formating.

Upstream, unless I'm missing something, WiktionaryParser doesn't seem to grab citations attached to examples, nor does it reproduce all types of related words; this is an issue when searching Old English words.

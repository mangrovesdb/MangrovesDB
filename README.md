# MangrovesDB Documentations

## Sphinx Quick Start

<code> $ sphinx-quickstart </code>


## Make HTML
Move to the docs folder and run this command.
```
$ make html
```

## Writing Considerations in rst files

- 1- ```=================``` is for the ```H1``` titles;
- 2- ```-----------------``` is considered for the ```H2```;
- 3- ```+++++++++++++++++``` is considered for the ```H3```;


## Convert md to pdf file
```
grip your_markdown.md
```

## Need Help
check this out: https://chiplicity.readthedocs.io/en/latest/Using_Sphinx/ShowingCodeExamplesInSphinx.html



## Cuation and Dangers
```
.. admonition:: Caution

    Please first *install* the **pre-requierments**...
```
```
.. DANGER::
   Beware killer rabbits!
```


## Libs and installation methos

### sphinxemoji
```bash
pip install sphinxemoji
```
[refrence](https://sphinxemojicodes.readthedocs.io/en/stable/#supported-codes)
some useful emojis are: :dart:, :flame:, :flags:, :flushed:, :grinning:, :heart:, :heavy_check_mark:, ✔️ :heavy_check_mark:, ❤️ :heart:,
🥵 :hot_face:, ⌛ :hourglass:, ⏳ :hourglass_flowing_sand:, ♨️ :hotsprings:, 😘 :kissing_heart:, 🔵 :large_blue_circle:, 🔷 :large_blue_diamond:, 🔶 :large_orange_diamond:, 🍁 :maple_leaf:, ⛔ :no_entry:, 🚫 :no_entry_sign:, 🛑 :octagonal_sign:, 👉🏻:point_right_tone1:, 🔴 :red_circle:,🙁:slight_frown:,🙂:slight_smile:,🙁:slightly_frowning_face:,🙂:slightly_smiling_face:, 🛑:stop_sign:, ⏱️:stopwatch:, 😛:stuck_out_tongue:,😝:stuck_out_tongue_closed_eyes:,😜:stuck_out_tongue_winking_eye:,😎:sunglasses:
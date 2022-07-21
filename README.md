# Workshop: Python Intensive Training


_[UC Davis DataLab](https://datalab.ucdavis.edu/)_  
_Fall 2022_  
_Instructor: Maggie Berrens <<mlberrens@ucdavis.edu>>, Parker Bremer <<parkerbremer@ucdavis.edu>>, Frank Cerasoli <<ftcerasoli@ucdavis.edu>>_  

* [Reader](https://ucdavisdatalab.github.io/python_intensive_training/)
* [Event Page](https://datalab.ucdavis.edu/eventscalendar/YOUR_EVENT/)

This four-day course is designed to prepare incoming (or experienced) graduate students with little to no coding experience for the coding demands that many graduate courses and research often require. The bootcamp will take place over September 6th-9th from 5pm-7pm on campus in the Shields 360 (DataLab classroom). This is a great opportunity to learn a new skill and meet other graduate students! Each session will begin with about an hour of demonstration to teach fundamental Python topics. This will be followed by time where students can work on an assignment with each other and ask questions to volunteers. The assignment each day will build off the previous sessions so by the end you will have a complete Python project!

## Goals

After this workshop, learners will be familiar with:

* Basic Python programming syntax
* Commonly used libraries such as NumPy and Pandas 
* Visualization tools, writing reusable functions
* Identifying where to go to learn more.

## Prerequisites

No prior programming experience is necessary.

## Contributing

The course reader is a live webpage, hosted through GitHub, where you can enter
curriculum content and post it to a public-facing site for learners.

To make alterations to the reader:

1.  Run `git pull`, or if it's your first time contributing, see the
    [Setup](#setup) section of this document.

2.  Edit an existing chapter file or create a new one. Chapter files may be 
    either Markdown files (`.md`) or Jupyter Notebook files (`.ipynb`). Either 
    is fine, but you must remain consistent across the reader (i.e. don't mix 
    and match filetypes). Put all chapter filess in the `chapters/` directory.
    Enter your text, code, and other information directly into the file. Make 
    sure your file:

    - Follows the naming scheme `##_topic-of-chapter.md/ipynb` (the only 
      exception is `index.md/ipynb`, which contains the reader's front page).
    - Begins with a first-level header (like `# This`). This will be the title
      of your chapter. Subsequent section headers should be second-level
      headers (like `## This`) or below.

    Put any supporting resources in `data/` or `img/`.

3.  Run the command `jupyter-book build .` in a shell at the top level of the
    repo to regenerate the HTML files in the `_build/`.

4.  When you're finished, `git add`:
    - Any files you edited directly
    - Any supporting media you added to `img/`

    Then `git commit` and `git push`. This updates the `main` branch of the
    repo, which contains source materials for the web page (but not the web
    page itself).

5.  Run the command `ghp-import -n -p -f _build/html` in a shell at the top
    level of the repo to update the `gh-pages` branch of the repo. This uses
    the [`ghp-import` Python package][ghp-import], which you will need to
    install first (`pip install ghp-import`). The live web page will update
    automatically after 1-10 minutes.

[ghp-import]: https://github.com/c-w/ghp-import


## Setup

### Python Packages

We recommend using [conda][] to manage Python dependencies. The `env.yaml` file
in this repo contains a list of packages necessary to build the reader. You can
create a new conda environment with all of the packages listed in that file
with this shell command:

```sh
conda env create --file env.yaml
```

[conda]: https://docs.conda.io/en/latest/

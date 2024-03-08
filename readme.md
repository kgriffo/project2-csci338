# Project 2 -- CLI Giphy Tool

Let's revisit [Lab 4]("../../labs/lab4) and [Lab 5]("../../labs/lab5")
and build a CLI interface for [Giphy](https://giphy.com/).

There are several goals with this project.

1. Practice more with Python & Poetry
2. Practice with static analysis tools
3. Practice reading documentation
4. Practice with writing tests
5. Practice building a CLI tool
6. Practice with an external API
7. Practice managing an API key

## Overview

We'll build a CLI (Command Line Interface) tool in Python. With the
exception of VS Code, nearly every tool we've interacted with this
semester (Git, Docker, ls, rm, etc) is a CLI tool.

It turns out that there are some [generally accepted patterns for
writing command line tools](https://clig.dev/), and when we get used
to those patterns it becomes much easier to use them.

To build out our Giphy CLI program, we'll use
[Click](https://click.palletsprojects.com/en/8.1.x/), a Python library
designed for building beautiful APIs.

You may also use [Typer](https://typer.tiangolo.com/) if you'd
prefer. Typer actually uses `click` under the hood but it has some
nice additions relating to typing via Python type hints. I will
provide sample code for click (below) but not for Typer.

## Basic Design

Your tool should offer several subcommands. The easiest one should be
an interface to the trending gifs.

```
$ gif trending
1) Snl Lessons GIF by Saturday Night Live (https://gph.is/g/a9zoOWA)
2) Happy Birthday GIF by Mumbai Indians (https://gph.is/g/ZywWQ8e)
3) Clap Applause GIF by Kyle Gordon (https://gph.is/g/aj2dOR9)
4) Happy I Love You GIF by Warner Bros. Deutschland (https://gph.is/g/ZYbwj3n)
5) Happy So Excited GIF by TikTok (https://gph.is/g/4D3zkPZ)
```

You should also be able to just list the top two trending items.

```
$ gif trending --count=2
1) Snl Lessons GIF by Saturday Night Live (https://gph.is/g/a9zoOWA)
2) Happy Birthday GIF by Mumbai Indians (https://gph.is/g/ZywWQ8e)
```

It should also support searching. By default, it should support 5
results.

```
$ gif search hello
1) Halloween Hello GIF by This GIF Is Haunted (https://gph.is/g/EGxb0Xl)
2) Valentines Day Love GIF by BREAD TREE (https://gph.is/g/Z7gGnBB)
3) Robin Williams Hello GIF by 20th Century Fox Home Entertainment (https://gph.is/2zoREKd)
4) Elmo Hello GIF by Sesame Street (https://gph.is/2wP0MpT)
5) Pick Up Hello GIF by The Drew Barrymore Show (https://gph.is/g/4bxdgNn)
```

But you should also be able to specify the count.

```
$ gif search --count=2 hello
1) Halloween Hello GIF by This GIF Is Haunted (https://gph.is/g/EGxb0Xl)
2) Valentines Day Love GIF by BREAD TREE (https://gph.is/g/Z7gGnBB)
```

If you use the `--markdown` flag, the results should be printed out in
markdown's image format.

```
$ gif search --count=2 --markdown hello
1) ![Halloween Hello GIF by This GIF Is Haunted](https://media3.giphy.com/media/9XeR2SAyL9YixCYN0b/200_d.gif?cid=911f4fa255teryoob19pwa7r7ny3qppxwu9zeij1llf5p3qx&ep=v1_gifs_search&rid=200_d.gif&ct=g)
2) ![Valentines Day Love GIF by BREAD TREE](https://media0.giphy.com/media/WOwiryOPA0G6jhKqB0/200_d.gif?cid=911f4fa255teryoob19pwa7r7ny3qppxwu9zeij1llf5p3qx&ep=v1_gifs_search&rid=200_d.gif&ct=g)
```

These combinations should work for the `trending` subcommand as well.

Last, but not least, you should be able to use the `--lucky` flag
(inspired by Google's old "I'm Feeling Lucky" button) to just print a
single result with no numbers.

```
$ gif search --lucky --markdown hello
![Halloween Hello GIF by This GIF Is Haunted](https://media3.giphy.com/media/9XeR2SAyL9YixCYN0b/200_d.gif?cid=911f4fa255teryoob19pwa7r7ny3qppxwu9zeij1llf5p3qx&ep=v1_gifs_search&rid=200_d.gif&ct=g)
```

This is actually cool because if you have `pbcopy` (or some
equivalent), you can pipe the result to your clipboard and then paste
it into a github comment.

```
$ gif search --lucky --markdown hellow | pbcopy
```

## Getting Started

1. Create an account and an API key on [the giphy developer site](https://developers.giphy.com).

2. Make sure your API key is working with curl (replace API_KEY with your API key):

```
$ curl "https://api.giphy.com/v1/gifs/trending?api_key=API_KEY&limit=25&offset=0&rating=g"
```

3. Set up your poetry project as we did in Lab 4 and Lab 5. You'll
want to add `click` and `requests` as a dependency.

4. Write a quick and dirty Python program that constructs the URL with
your API key and gets some data back. Note that the data will be json,
so you can use the response's `.json()` method to get the response
back as a Python dictionary.

5. Once you have that all scaffolded, you are ready to start really
working.

6. Create a new repository in Github for your project, and add Sarah
and Semmy as collaborators.

7. Scaffold things with the click example code below, and experiment
with options and arguments. Once you have something basic working, you
can make your first pull request!

## API Key Security

Note that the API key should not be hardcoded into your program nor
checked into your repository. Think of it as a password.

A common way of injecting credentials into your program is to use
environment variables. The simplest way to do that is to set up the
environment variable when you run it:

```
$ GIPHY_API_KEY=whatever poetry run python main.py
```

Now in your Python program, you can extract it by using the
`os.environ` object.

```
import os

API_KEY=os.environ["GIPHY_API_KEY"]
print(API_KEY)
```

This should print `whatever`.

## Software Design

For this project you'll use the
[click](https://click.palletsprojects.com/en/8.1.x/) library to build
a CLI. Here's a simple scaffold to get you started with click.

```
import click


@click.group()
def gif():
    print("hello from giphy cli!")


@gif.command()
def trending():
    print("trending subcommand called!")


@gif.command()
def search():
    print("search subcommand called!")


if __name__ == "__main__":
    gif()
```

This gives you quite a bit of functionality. For example, you get a
help display:

```
$ poetry run python gif.py --help
Usage: gif.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  search
  trending
```

And you get your two subcommands automagically:

```
$ poetry run python gif.py search
hello from giphy cli!
search subcommand called!

$ poetry run python gif.py trending
hello from giphy cli!
trending subcommand called!
```

This does not give you any options. You'll need to read the [click
documentation on
options](https://click.palletsprojects.com/en/8.1.x/options/) to learn
how to do that.

For the search command, you'll also need to add an argument for the
search terms. You'll need to read the [click documentation on
arguments](https://click.palletsprojects.com/en/8.1.x/arguments/) to
learn how to manage arguments.

You could easily hack this together from here, but let's try to make
it a bit more testable. To do that, we'll `GiphyCLI` class and a
`GiphyAPI` class. These will be imported into your main program above.

The `GiphyCLI` class will expose two methods: `trending` and
`search`. Those will take arguments representing the options that are
could potentially be sent in.

The Giphy class methods will call into the GiphyAPI class to actually
make the request to the back-end API.

The problem you'll have to solve is how to best test this. You should
write some unit tests that do not acutally call into the Giphy API
(small tests) to make sure your code is working as expected. You
should also have separate tests that do actually call into the Giphy
API (medium tests).

You'll probably want to start on the `GiphyAPI` class first, then the
`GiphyCLI` class and then wire those into the scaffolded `click`
program from above. You should write your tests as you're writing the
classes.

## Grading

**Meets Expectations (guarantees a C)**
1. Minimum number of pull requests (3-4) spaced out over the project
timeline.
2. Working `GiphyAPI` class.
3. Working "medium" tests for the `GiphyAPI` class.
4. A `check` script that runs black, isort and flake8 with no failures
or warnings.

**Exceeds Expectations (guarantees a B)**
1. A working `GiphyCLI` class.
2. "small" and "medium" tests for the `GiphyCLI` class.

**Greatly Exceeds Expectations (guarantess an A)**
1. Everything wired up and working as described in the description
above.
2. Program can be bundled and run directly with the `gif` command (so
without poetry)
3. Note that the bundle should /NOT/ include the API key (which means
the user of the program will have to provide their own API key as an
environment variable)

**Redefines Expectations**
1. As usual, I don't know what this will look like because if I did I
would expect it!

## Tips

### Use Poetry Outside of Docker

Since this project is a simple Python tool, you don't /have/ to use
docker, which may make it easier. You most likely have a version of
Python 3 installed on your system. You can confirm this by running
python from the command line:

```
$ python --version
Python 3.12.2
```

You can also confirm you have Pip:

```
$ pip --version
pip 23.2.1 from /usr/lib/python3.12/site-packages/pip (python 3.12)
```

If you have both of those things, you don't have to use docker. You'll
just need to install poetry globally on your system.

```
$ pip install poetry
```

### Example Queries

Once you have your api key, you can experiment with the API by using curl.

```
$ curl "https://api.giphy.com/v1/gifs/trending?api_key={API_KEY}&limit=25&offset=0&rating=g"
$ curl "https://api.giphy.com/v1/gifs/search?api_key={API_KEY}&q=hello&limit=25&offset=0&rating=g"
```

You can also use [Giphy's API
Explorer](https://developers.giphy.com/explorer/) to experiment with
requests.

### Bundling Tips (Coming Soon)
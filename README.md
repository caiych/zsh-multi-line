#Why
*history* cannot handle multi-line command properly. It will break them into
pieces. So you will never find a complete multi-line command when you are
accessing the history using search.

#How
When you are editing a long command, hit `CTRL-B`. `$EDITOR` will pop out and
let you continue editing the command. After you finished, save and exit
`$EDITOR`, you will get your command in one line. Then your command is ready to
run.

#What
When hitting `CTRL-B`, `split_lines.py` is executed to split the current command
and try to split your command so that the line won't be too long to make you
easier to navigate.

When you exit your `$EDITOR`, `join_lines.py` is executed to replace `\\n` with
a space, and put them in your prompt.

#Install
I wrote install.py to make it easier for you to install.
```
> git clone https://github.com/caiych/zsh-multi-line.git ~/zsh-multi-line
> ~/zsh-multi-line/install.py
```

If you don't trust me, just crack `install.py`. It's quite simple.


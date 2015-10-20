multi_line() {
	FILENAME=/tmp/multi_line_edit_$(date +"%s").sh
	echo $LBUFFER | %%location%%/split_lines.py > $FILENAME
	$EDITOR $FILENAME < /dev/tty
	LBUFFER=$(%%location%%/join_lines.py < $FILENAME)
	zle redisplay
}

zle -N multi_line
bindkey '^B' multi_line

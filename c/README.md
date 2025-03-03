All your files will be compiled on Ubuntu 20.04 LTS using `gcc`, using the options `-Wall -Werror -Wextra -pedantic -std=gnu89`

All your files should end with a new line

Your code should use the `Betty` style

To run the Betty linter just with command `betty <filename>:`

* To install [Betty](https://github.com/alx-tools/Betty)

Clone the [repo](https://github.com/alx-tools/Betty) to your local machine

`cd`into the Betty directory

Install the linter with `sudo ./install.sh`

`emacs` or `vi` a new file called `betty`, and copy the script below:
```
#!/bin/bash
# Simply a wrapper script to keep you from having to use betty-style
# and betty-doc separately on every item.
# Originally by Tim Britton (@wintermanc3r), multiargument added by
# Larry Madeo (@hillmonkey)

BIN_PATH="/usr/local/bin"
BETTY_STYLE="betty-style"
BETTY_DOC="betty-doc"

if [ "$#" = "0" ]; then
    echo "No arguments passed."
    exit 1
fi

for argument in "$@" ; do
    echo -e "\n========== $argument =========="
    ${BIN_PATH}/${BETTY_STYLE} "$argument"
    ${BIN_PATH}/${BETTY_DOC} "$argument"
done
```

Once saved, exit file and change permissions to apply to all users with`chmod a+x betty`

Move the `betty` file into `/bin/` directory or somewhere else in your`$PATH` with `sudo mv betty /bin/`

You can now type `betty <filename>` to run the Betty linter!
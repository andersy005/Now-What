# Getting Started with tmux

## Sessions 

```$ tmux```
- By running tmux with no arguments, you create a brand new session.
- It is useful to think of a tmux session as a login on your computer.
- Also, it is useful to think of tmux as a mini operating system that manages running programs, windows, and more, all within a session.

## Naming Sessions

```$ tmux rename-session lab```


## The prefix key

- There is a special key in tmux called the prefix key that is used to perform most of the
keyboard shortcuts. Its default binding in tmux is ```Ctrl + b```, but you can change that if you prefer something else or if
it conflicts with a key in a program you often use within tmux. 

## Creating another window

- Press ```Ctrl + b```, then ```c```

## Jump back to previously opened window

- Press ```Ctrl + b```, then ```l```

## Switch to a window directly by its number.

- Press ```Ctrl + b ```, then the number window to jump to that window.

**NOTE:** 
- tmux allows you to keep just one terminal window open, and this window can have a
multitude of different windows within it, closing all the different running processes. Closing
this terminal window won't terminate the running processes; tmux will continue humming
along in the background with all of the programs running behind the scenes.

## Help on Key bindings

- Press ```Ctrl + b ```, then ```?``` to see your screen change to show a list with bind-key to the left.

- Press ```Ctrl + s``` and you'll see a prompt appear that says Search Down:, where you can type a
string and it will search the help document for that string.

- To get out
of any screens, generated by tmux, simply press ```q``` for quit.

- To open the choose window interface, simply type ```<Prefix>```, w since w was the key shown
in the help bound to choose-window and voilà
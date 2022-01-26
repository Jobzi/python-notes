After installing zsh, we can perform the customisation.
## Themes
First we start from the themes, ZSH provides a variety of themes that can be viewed in the official repository of [Themes - OhMyZsh](https://github.com/ohmyzsh/ohmyzsh/wiki/Themes).

To open the configuration file you can use `vim` or `nano` in my case, I used nano to edit the configuration file `.zshrc`.

```terminal
$ nano ~/.zshrc
```

In order to enable a theme, set ZSH_THEME to the name of the theme in your ~/.zshrc, before sourcing Oh My Zsh; for example: ZSH_THEME=robbyrussell If you do not want any theme enabled, just set ZSH_THEME to blank: ZSH_THEME=""
or you can select from the list of themes provided by the GitHub repository.

## Plugins
To install plugins, the OhMyZsh repository has a list of plugins that can be added to the terminal. You can check the list here [Plugins](https://github.com/ohmyzsh/ohmyzsh/wiki/Plugins).

Enable a plugin by adding its name to the plugins array in your .zshrc file (found in the $HOME directory). For example, this enables the `rails`, `git` and `ruby` plugins, in that order:
```sh
plugins=(rails git ruby)
```
NOTE: elements in zsh arrays are separated by whitespace (spaces, tabs, newlines...). DO NOT use commas.


#### zsh-autosuggestions
1. Clone this repository into `$ZSH_CUSTOM/plugins` (by default `~/.oh-my-zsh/custom/plugins`)

    ```sh
    git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
    ```

2. Add the plugin to the list of plugins for Oh My Zsh to load (inside `~/.zshrc`):

    ```zsh
    plugins=( 
        # other plugins...
        zsh-autosuggestions
    )
    ```

3. Start a new terminal session.

#### zsh-syntax-highlighting

1. Clone this repository in oh-my-zsh's plugins directory:

    ```zsh
    git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
    ```

2. Activate the plugin in `~/.zshrc`:

    ```zsh
    plugins=( 
        # other plugins...
        zsh-autosuggestions
    )
    ```

3. Restart zsh (such as by opening a new instance of your terminal emulator).

#### Top Plugins Here:
- [Plugins - OhMyZsh](https://safjan.com/top-popular-zsh-plugins-on-github/)

# Favourite Zsh features
### Help with Git
   
> Everyone has their favourite aliases for git commands. oh-my-zsh has a bunch out of the box too.
![Help with Git](https://code.joejag.com/assets/2014/git_aliases.jpg)

### Tab completion on ‘cd’

>In Bash when you press `<TAB>` you get prompted with a list of files in the current directory. In the context of the cd command this isn’t particularly useful, as you can only go into directories. Zsh knows this and only shows you the possible valid destinations.
![Tab completion](https://code.joejag.com/assets/2014/cd_after.jpg)
### shorthand ‘ls’
>You don’t have to type whole directory names, just type the first few letters enough to make it unique and Zsh will work the rest out.
![shorthand](https://code.joejag.com/assets/2014/ls_shorthand_before.jpg)
>Hey presto!
![shorthand-after](https://code.joejag.com/assets/2014/ls_shorthand_after.jpg)

#### See More Features Here 
- [Features](https://code.joejag.com/2014/why-zsh.html)
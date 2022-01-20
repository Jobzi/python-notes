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

    ```sh
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
    plugins=( [plugins...] zsh-syntax-highlighting)
    ```

3. Restart zsh (such as by opening a new instance of your terminal emulator).
# NVIM

This is my personal configuration of nvim.

1. Install nvim, lua and luajit
```sh
pacman -S neovim lua luajit
```

2. Install `packer`
```sh
git clone --depth 1 https://github.com/wbthomason/packer.nvim ~/.local/share/nvim/site/pack/packer/start/packer.nvim
```

3. Download dots-neovim
```sh
cd ~/.config
git clone git@github.com:nestor784/dots-neovim.git
mv dots-neovim/ nvim/ 
```

4. Install dependencies
```sh
# Ruby
pacman -S ruby
gem install neovim

# Python
pacman -S python tk python-pynvim pyenv python-virtualenv
yay -S pyenv-virtualenv

pyenv install -l
pyenv install 2.7.18 
pyenv install 3.11.4
pyenv activate py3nvim 
pip install pynvim
pyenv deactivate
pyenv activate py2nvim 
pip install pynvim
pyenv deactivate

# Nodejs npm
pacman -S nodejs npm
npm install -g neovim

# Perl
pacman -S perl

# LaTeX
pacman -S texlive-basic texlive-latex texlive-latexextra texlive-bibtexextra texlive-binextra biber xdotool

# Find sty files
pacman -F package.sty
```

Add python providers to nvim/lua/settings.lua

```lua
--To find paths, run pyenv which python, when stay in the virtualenv 
g.python_host_prog = '/home/nestor/.pyenv/versions/py2nvim/bin/python'

g.python3_host_prog = '/home/nestor/.pyenv/versions/py3nvim/bin/python'
```

Como crear un entorno virtual con `venv`  
```bash
python -m venv .venv
source .venv/bin/activate
deactivate
```


### Shortcuts

* Vimtex
Al presionar `;ls` se busca dicha linea de código en el PDF.
Al presionar `<ctrl><left-click>` se busca dicho texto del PDF en el editor.

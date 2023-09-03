local g = vim.g
local o = vim.o

o.spelllang = 'en_us'
g.python_host_prog = '/home/nestor/.pyenv/versions/py2nvim/bin/python'
g.python3_host_prog = '/home/nestor/.pyenv/versions/py3nvim/bin/python'
o.guifont = 'Hack Nerd Font'

o.number = true
o.relativenumber = true
o.showmatch = true

o.background = 'dark'
o.encoding = 'UTF-8'

o.clipboard = 'unnamedplus'
o.ignorecase = true
o.showcmd = true

-- Undo and backup options
o.backup = false
o.swapfile = false
o.undofile = true
o.undodir = '/home/nestor/.config/nvim/undo'

-- Nvim tree toggle
g.loaded_netrw = 1
g.loaded_netrwPlugin = 1
o.termguicolors = true
o.mouse = nil

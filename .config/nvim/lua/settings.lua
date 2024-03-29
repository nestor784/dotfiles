local g = vim.g
local o = vim.o
local api = vim.api

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

o.shiftwidth = 4
o.tabstop = 4
o.softtabstop = 4

-- Undo and backup options
o.backup = false
o.swapfile = false
o.undofile = true
o.undodir = '/home/nestor/.config/nvim/undo'

g.loaded_netrw = 1
g.loaded_netrwPlugin = 1
o.termguicolors = true
o.mouse = nil

-- Blade
local BladeFiletype = api.nvim_create_augroup('BladeFiletypeRelated', { clear = true })
api.nvim_create_autocmd(
	{'BufNewFile', 'BufRead'},
	{pattern = "*.blade.php", command = "set ft=blade", group= BladeFiletype}
)

-- Lua initialization file
vim.cmd[[colorscheme neon]]

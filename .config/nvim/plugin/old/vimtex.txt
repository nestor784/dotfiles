local g = vim.g
local map = vim.keymap

--g.vimtex_view_enabled = 1
g.vimtex_view_method = 'zathura'

g.vimtex_context_pdf_viewer = 'okular'
g.vimtex_quickfix_mode = 0
g.vimtex_view_general_options = [[--unique file:@pdf\#src:@line@tex]]

g.vimtex_compiler_method = 'latexmk'

vim.keymap.set('n','<localleader>v','<plug>(vimtex-view)')

vim.api.nvim_create_autocmd('FileType',{ pattern = 'tex', 
callback = function ()
	vim.opt.shiftwidth = 2 
	vim.keymap.set("","<F9>",'<esc>:w<CR>:VimtexCompile<CR>')
end
})

g.maplocalleader = ';'
map.set('n','<localleader>ls','<Plug>(vimtex-view)')


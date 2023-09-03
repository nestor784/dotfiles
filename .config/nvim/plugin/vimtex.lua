local g = vim.g

g.vimtex_view_enabled = 1
g.vimtex_view_method = 'zathura'

g.vimtex_view_general_viewer = 'okular'
g.vimtex_view_general_options = [['--unique file:@pdf\#src:@line@tex']]

g.vimtex_compiler_method = 'latexmk'

vim.keymap.set('n','<localleader>v','<plug>(vimtex-view)')

vim.api.nvim_create_autocmd('FileType',{ pattern = 'tex', 
callback = function ()
	vim.opt.shiftwidth = 2 
	vim.keymap.set("","<F9>",'<esc>:w<CR>:VimtexCompile<CR>')
end
})



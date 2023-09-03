require("neo-tree").setup({
      enable_git_status =true,
      filesystem = {
        window = {
          mappings = {
            ["<F5>"] = "refresh",
            ["o"] = "open",
          }
        },
	filtered_items = {
	  visible = true,
	  hide_dotfiles = false,
	}
      },
})

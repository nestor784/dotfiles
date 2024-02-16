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
	},
	commands = {
		-- Override delete to use trash instead of rm
		delete = function(state)
			local inputs = require "neo-tree.ui.inputs"
			local path = state.tree:get_node().path
			local msg = "Are you sure you want to delete " .. path
			inputs.confirm(msg, function(confirmed)
				if not confirmed then return end
				
				vim.fn.system({ "trash", vim.fn.fnameescape(path) })
				require("neo-tree.sources.manager").refresh(state.name)
			end)
		end,
      	},
	},
})

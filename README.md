Terraform support for Sublime Text 3
====================================

Fork of [Terraform.tmLanguage][base_repo] with some sweet improvements.

Features:

* Syntax highlighting for `.tf` and `.tfvars` files.
* Format on save using `terraform fmt` (only available in version >= 0.6.15)

Installation
------------

### Using Package Control

1. Having [Package Control](https://packagecontrol.io/installation) installed
2. Open the palette by pressing `Ctrl+Shift+P` (Win, Linux) or `Cmd+Shift+P` (OS X).
3. Select _"Package Control: Install package"_
4. Select _"Terraform"_

### Manually

1. Open the Sublime Text Packages folder
    - OS X: `~/Library/Application Support/Sublime Text 3/Packages/`
    - Windows: `%APPDATA%/Sublime Text 3/Packages/`
    - Linux (Ubuntu/Debian): `~/.config/sublime-text-3/Packages/`

2. Clone this repo:

        $ git clone https://github.com/tmichel/sublime-terraform

## Configuration

The defaults are available in the [Terraform.sublime-settings`][settings_file]
file.

[base_repo]: github.com/alexlouden/Terraform.tmLanguage
[settings_file]: Terraform.sublime-settings

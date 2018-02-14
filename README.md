Terraform support for Sublime Text 3
====================================

Fork of [Terraform.tmLanguage][base_repo] with some sweet improvements.

### Features:

* Syntax highlighting for `.tf` and `.tfvars` files.
* Format on save using `terraform fmt` (only available in version >= 0.6.15)
* Code completion for resources and data sources
* Snippets

Installation
------------

### Using Package Control

1. Having [Package Control](https://packagecontrol.io/installation) installed
2. Open the palette by pressing `Ctrl+Shift+P` (Win, Linux) or `Cmd+Shift+P` (OS X).
3. Select _"Package Control: Add Repository"_
4. Enter `https://github.com/tmichel/Terraform.tmLanguage`
5. Open command palette again
6. Select _"Package Control: Install Package"_
7. Select _"Terraform.tmLanguage"_

### Manually

1. Open the Sublime Text Packages folder
    - OS X: `~/Library/Application Support/Sublime Text 3/Packages/`
    - Windows: `%APPDATA%/Sublime Text 3/Packages/`
    - Linux (Ubuntu/Debian): `~/.config/sublime-text-3/Packages/`

2. Clone this repo:

        $ git clone https://github.com/voltechs/Terraform.tmLanguage

## Configuration

The defaults are available in the [Terraform.sublime-settings][settings_file]
file.

## Development

To update the completion files you will need Ruby 2.2+

1. Install Ruby
2. `bundle install`
3. `bundle exec rake completions`

[base_repo]: https://github.com/alexlouden/Terraform.tmLanguage
[settings_file]: Terraform.sublime-settings

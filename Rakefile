require "nokogiri"
require "net/http"
require "uri"
require "json"

BASE_URL = "https://www.terraform.io"
RESOURCE_PATTERN = %r{^/docs/providers/\w+/r}
DATA_SOURCE_PATTERN = %r{^/docs/providers/\w+/d}
PROVIDERS = %w[aws template terraform postgresql]

task :default => ["resources.py"]

task "resources.py" do
  resources    = PROVIDERS.flat_map { |provider| get_resources(provider, RESOURCE_PATTERN) }
  data_sources = PROVIDERS.flat_map { |provider| get_resources(provider, DATA_SOURCE_PATTERN) }

  write_completion_file("Resources", scope: "meta.resource.type.terraform", completions: resources)
  write_completion_file("Data Sources", scope: "meta.data-source.type.terraform", completions: data_sources)
end

def write_completion_file(name, completions={})
  File.open("Completions/#{name}.sublime-completions", "w") do |f|
    f.write(JSON.pretty_generate(completions))
  end
end

def get_resources(provider, pattern)
  uri = URI("https://www.terraform.io/docs/providers/#{provider}/index.html")
  get_terraform_resource_keys(uri, pattern)
end

def get_terraform_resource_keys(uri, href_pattern)
  html = download_and_parse(uri)
  html.css(".nav.docs-sidenav ul.nav > li > a").select { |a| a["href"] =~ href_pattern }.map { |a| a.text }
end

def download_and_parse(uri)
  resp = Net::HTTP.get(uri)
  Nokogiri::HTML(resp)
end

def get_providers
  uri = URI("https://www.terraform.io/docs/providers/index.html")
  html = download_and_parse(uri)
  html.search("li.active ul.nav > li > a").map do |a|
    [a.text, URI(BASE_URL + a["href"])]
  end
end

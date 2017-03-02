require "nokogiri"
require "net/http"
require "uri"
require "json"

BASE_URL = "https://www.terraform.io"
RESOURCE_PATTERN = %r{^/docs/providers/\w+/r}
DATA_SOURCE_PATTERN = %r{^/docs/providers/\w+/d/}

desc "Generate completion files"
task :completions do
  threads = get_providers.map do |provider, uri|
    res_thr = Thread.new { get_terraform_resource_keys(uri, RESOURCE_PATTERN) }
    dat_thr = Thread.new { get_terraform_resource_keys(uri, DATA_SOURCE_PATTERN) }

    [res_thr, dat_thr]
  end

  completions = threads.each_with_object(Hash.new { |h,k| h[k] = [] }) do |(res, data), hash|
    hash[:resources] += res.value
    hash[:data_sources] += data.value
  end

  completions[:data_sources] << "external"

  write_completion_file("Resources", scope: "meta.resource.type.terraform", completions: completions[:resources].sort)
  write_completion_file("Data Sources", scope: "meta.data-source.type.terraform", completions: completions[:data_sources].sort)
end

desc "List providers"
task :providers do
  puts get_providers.map(&:first)
end

def write_completion_file(name, completions={})
  File.open("Completions/#{name}.sublime-completions", "w") do |f|
    f.write(JSON.pretty_generate(completions))
  end
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

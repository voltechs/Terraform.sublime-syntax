import sublime
import sublime_plugin

from .resources import resources, data_sources

class ResourceCompletion(sublime_plugin.EventListener):
    selector = 'source.terraform'

    def on_query_completions(self, view, prefix, locations):
        loc = locations[0]
        if not view.match_selector(loc, ResourceCompletion.selector):
            return None

        if not self._is_resource_key(view, loc):
            return None

        line = view.substr(view.line(loc)).strip()
        filename = None

        result = []
        if line.startswith('resource'):
            result = self._convert_to_completion_result(resources)
        elif line.startswith('data'):
            result = self._convert_to_completion_result(data_sources)
        else:
            return None

        return (result, sublime.INHIBIT_WORD_COMPLETIONS)

    def _convert_to_completion_result(self, list):
        return [[x, x] for x in list]

    def _is_resource_key(self, view, loc):
        '''
        Determines whether the current location is inside the resource key or not.

        Give a resource declaration `resource "aws_instance" "myinstance" {}`, the
        resource key is aws_instance.
        '''

        _, col = view.rowcol(loc)
        line = view.substr(view.line(loc))[0:col]
        parts = line.split(' ')

        return len(parts) <= 2

class VariableCompletion(sublime_plugin.EventListener):
    def on_query_completions(self, view, prefix, locations):
        return None

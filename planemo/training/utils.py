"""Module contains code for the Requirement, Reference and some general functions for training."""

import collections

import oyaml as yaml


class Requirement(object):
    """Class to describe a training requirement."""

    def __init__(self, req_type="internal", topic_name="introduction", title=None, tutorials=None, link=None):
        """Init a Requirement instance."""
        self.type = req_type
        self.topic_name = topic_name
        self.tutorials = tutorials
        self.title = title
        self.link = link

    def init_from_dict(self, metadata):
        """Init from a dictionary generated by export_to_ordered_dict."""
        self.type = metadata['type']
        if self.type == 'internal':
            self.topic_name = metadata['topic_name']
            if 'tutorials' in metadata:
                self.tutorials = metadata['tutorials']
        else:
            self.title = metadata['title']
            if self.type == 'external':
                self.link = metadata['link']

    def export_to_ordered_dict(self):
        """Export the requirement into an ordered dictionary."""
        req = collections.OrderedDict()
        req['type'] = self.type
        if self.type == 'internal':
            req['topic_name'] = self.topic_name
            if self.tutorials:
                req['tutorials'] = self.tutorials
        else:
            req['title'] = self.title
            if self.type == 'external':
                req['link'] = self.link
        return req


class Reference(object):
    """Class to describe a training reference."""

    def __init__(self, authors="authors et al", title="the title", link="link", summary=""):
        """Init a Reference instance."""
        self.authors = authors
        self.title = title
        self.link = link
        self.summary = summary

    def init_from_dict(self, metadata):
        """Init from a dictionary generated by export_to_ordered_dict."""
        self.authors = metadata['authors']
        self.title = metadata['title']
        self.link = metadata['link']
        if 'summary' in metadata:
            self.summary = metadata['summary']

    def export_to_ordered_dict(self):
        """Export the reference into an ordered dictionary."""
        ref = collections.OrderedDict()
        ref['authors'] = self.authors
        ref['title'] = self.title
        ref['link'] = self.link
        ref['summary'] = self.summary
        return ref


def load_yaml(filepath):
    """Load the content of a YAML file to a dictionary."""
    with open(filepath, "r") as m_file:
        content = yaml.load(m_file)
    return content


def save_to_yaml(content, filepath):
    """Save a dictionary to a YAML file."""
    with open(filepath, 'w') as stream:
        yaml.safe_dump(content,
                       stream,
                       indent=2,
                       default_flow_style=False,
                       default_style='',
                       explicit_start=True,
                       encoding='utf-8',
                       allow_unicode=True)

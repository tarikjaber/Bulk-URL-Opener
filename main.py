# -*- coding: utf-8 -*-

import sys
import os
from pathlib import Path

plugindir = Path.absolute(Path(__file__).parent)
paths = (".", "lib", "plugin")
sys.path = [str(plugindir / p) for p in paths] + sys.path

import yaml
import webbrowser
from flowlauncher import FlowLauncher

class TabOpener(FlowLauncher):

    def query(self, query):
        # Load the YAML file containing the tab groups
        with open("tab_groups.yaml", "r") as f:
            tab_groups = yaml.safe_load(f)

        # Filter the tab groups based on the user's query
        matching_groups = [
            group for group in tab_groups if query.lower() in group["name"].lower()]

        # Create a result item for each matching group
        # Create a result item for each matching group
        # Create a result item for each matching group
        results = []
        for group in matching_groups:
            results.append({
                "Title": group["name"],
                "SubTitle": "Open tabs",
                "IcoPath": "Images/app.png",
                "JsonRPCAction": {
                    "method": "open_tabs",
                    "parameters": [[tab for tab in group["tabs"]]]
                }
            })

        return results

    def open_tabs(self, tabs):
        # Open the specified tabs in the default web browser
        for tab in tabs:
            webbrowser.open(tab)


if __name__ == "__main__":
    TabOpener()

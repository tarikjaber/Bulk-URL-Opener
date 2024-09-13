# -*- coding: utf-8 -*-
import sys
import os
import subprocess
from pathlib import Path

plugindir = Path.absolute(Path(__file__).parent)
paths = (".", "lib", "plugin")
sys.path = [str(plugindir / p) for p in paths] + sys.path

import yaml
import webbrowser
from flowlauncher import FlowLauncher

class TabOpener(FlowLauncher):

    def query(self, query):
        browser_name = self.rpc_request['settings']['default_browser']
        open_tabs_in_new_window = self.rpc_request['settings']['open_tabs_in_new_window']
        
        # Load the YAML file containing the tab groups
        with open("tab_groups.yaml", "r") as f:
            tab_groups = yaml.safe_load(f)

        # Filter the tab groups based on the user's query
        matching_groups = [
            group for group in tab_groups if query.lower() in group["name"].lower()]

        # Create a result item for each matching group
        results = []

        for group in matching_groups:
            if open_tabs_in_new_window:
                results.append({
                    "Title": group["name"],
                    "SubTitle": "Open tabs",
                    "IcoPath": "Images/app.png",
                    "JsonRPCAction": {
                        "method": "open_tabs_new_window",
                        "parameters": [group["tabs"], browser_name]
                    }
                })
            else:
                results.append({
                    "Title": group["name"],
                    "SubTitle": "Open tabs",
                    "IcoPath": "Images/app.png",
                    "JsonRPCAction": {
                        "method": "open_tabs",
                        "parameters": [group["tabs"]],
                    }
                })


        return results

    def open_tabs(self, tabs):
        # Open the specified tabs in the default web browser
        for tab in tabs:
            webbrowser.open(tab)

    def open_tabs_new_window(self, tabs, browser_name):
        subprocess.run(['start', browser_name, '/new-window', tabs[0]], shell=True)
        for tab in tabs[1:]:
            subprocess.run(['start', browser_name, "/new-tab", tab], shell=True)

if __name__ == "__main__":
    TabOpener()

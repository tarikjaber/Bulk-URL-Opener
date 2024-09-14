# -*- coding: utf-8 -*-
import sys
import subprocess
from pathlib import Path
import logging
from os.path import expanduser

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
        
        logger = logging.getLogger()
        home = expanduser("~")
        logging.basicConfig(filename=home + '\\bulk.log', encoding='utf-8', level=logging.DEBUG)

        parts = query.split(" ")

        group_entered = parts[0]
        search_query = " ".join(parts[1:])

        # Load the YAML file containing the tab groups
        with open("tab_groups.yaml", "r") as f:
            tab_groups = yaml.safe_load(f)

        # Filter the tab groups based on the user's query
        matching_groups = [
            group for group in tab_groups if group_entered.lower() in group["name"].lower()]

        # Create a result item for each matching group
        results = []

        for group in matching_groups:
            tabs = group["tabs"]
            group_name = group["name"]
            query_in_config = group.get("query", "")

            query = search_query if search_query else query_in_config
            title = f"{group_name} with '{query}'" if query else group_name

            if open_tabs_in_new_window:
                results.append({
                    "Title": title,
                    "SubTitle": "Open tabs",
                    "IcoPath": "Images/app.png",
                    "JsonRPCAction": {
                        "method": "open_tabs_new_window",
                        "parameters": [tabs, browser_name, query]
                    }
                })
            else:
                results.append({
                    "Title": title,
                    "SubTitle": "Open tabs",
                    "IcoPath": "Images/app.png",
                    "JsonRPCAction": {
                        "method": "open_tabs",
                        "parameters": [tabs, query],
                    }
                })

        return results

    def open_tabs(self, tabs, query):
        # Open the specified tabs in the default web browser
        for tab in tabs:
            query_tab = tab.replace("%s", query)
            webbrowser.open(query_tab)

    def open_tabs_new_window(self, tabs, browser_name, query):
        first_tab = tabs[0].replace("%s", query)
        subprocess.run(['start', browser_name, '/new-window', first_tab], shell=True)

        for tab in tabs[1:]:
            query_tab = tab.replace("%s", query)
            subprocess.run(['start', browser_name, "/new-tab", query_tab], shell=True)

if __name__ == "__main__":
    TabOpener()

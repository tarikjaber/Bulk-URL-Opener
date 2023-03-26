# -*- coding: utf-8 -*-

import demjson


class FlowLauncherAPI:

    @classmethod
    def change_query(cls, query, requery: bool = False):
        """
        change flow launcher query
        """
        print(demjson.encode({
            "method": "Flow.Launcher.ChangeQuery",
            "parameters": [query, requery]}))

    @classmethod
    def shell_run(cls, cmd):
        """
        run shell commands
        """
        print(demjson.encode({
            "method": "Flow.Launcher.ShellRun",
            "parameters": [cmd]}))

    @classmethod
    def close_app(cls):
        """
        close flow launcher
        """
        print(demjson.encode({
            "method": "Flow.Launcher.CloseApp",
            "parameters": []}))

    @classmethod
    def hide_app(cls):
        """
        hide flow launcher
        """
        print(demjson.encode({
            "method": "Flow.Launcher.HideApp",
            "parameters": []}))

    @classmethod
    def show_app(cls):
        """
        show flow launcher
        """
        print(demjson.encode({
            "method": "Flow.Launcher.ShowApp",
            "parameters": []}))

    @classmethod
    def show_msg(cls, title: str, sub_title: str, ico_path: str = ""):
        """
        show messagebox
        """
        print(demjson.encode({
            "method": "Flow.Launcher.ShowMsg",
            "parameters": [title, sub_title, ico_path]}))

    @classmethod
    def open_setting_dialog(cls):
        """
        open setting dialog
        """
        print(demjson.encode({
            "method": "Flow.Launcher.OpenSettingDialog",
            "parameters": []}))

    @classmethod
    def start_loadingbar(cls):
        """
        start loading animation in flow launcher
        """
        print(demjson.encode({
            "method": "Flow.Launcher.StartLoadingBar",
            "parameters": []}))

    @classmethod
    def stop_loadingbar(cls):
        """
        stop loading animation in flow launcher
        """
        print(demjson.encode({
            "method": "Flow.Launcher.StopLoadingBar",
            "parameters": []}))

    @classmethod
    def reload_plugins(cls):
        """
        reload all flow launcher plugins
        """
        print(demjson.encode({
            "method": "Flow.Launcher.ReloadPlugins",
            "parameters": []}))

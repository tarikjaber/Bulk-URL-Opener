## Bulk URL Opener
This plugin allows you to open multiple URLs at once. It reads groups of tabs from `tab_groups.yaml`at:
```
%APPDATA%\FlowLauncher\Settings\tab_groups.yaml
```
In portable mode, open the userdata folder by searching "userdata" in Flow Launcher. Then create
`tab_groups.yaml` in the Settings folder.

**Example**: This file contains 2 groups - `demo` and `demo2`.

```yaml
- name: demo
  tabs:
    - https://www.google.com
    - https://www.youtube.com
- name: demo2
  tabs:
    - https://www.youtube.com
    - https://www.google.com
    - https://www.wikipedia.com
    - https://www.github.com
```

## Search Queries

You can also open URLs with search queries. Just add `%s` in a URL where you want a search query 
to be inserted. If you type `bu demo3 hello world` in the flow box then `%s` will be replaced with "hello world".

**Default Search Queries**: You can have a "default" search by adding a `query: <default search>` key-value pair to a tab group. 
For example, in the group `demo3` below, all sites with `%s` will be replaced with "test" if no search term is provided.

```yaml
- name: demo3
  query: test
  tabs:
    - https://www.youtube.com/results?search_query=%s
    - https://www.google.com/search?q=%s
    - https://www.wikipedia.com
    - https://www.github.com
```
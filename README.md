## Bulk URL Opener
This plugin allows you to open multiple URLs at once. It reads groups of tabs from `tab_groups.yaml`
in the Plugins Directory (accessible by expanding the accordion for the plugin and clicking on the folder icon
in the bottom right).

An example group called `demo` is provided in the file. You can add as many groups as you want.

For example, if you wanted to add a group called `demo2`, then you could add the following to `tab_groups.yaml`:

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

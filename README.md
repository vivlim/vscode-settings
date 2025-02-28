use with `zokugun.sync-settings`


## example settings.yml

```yaml
# current machine's name, optional; it can be used to filter settings or in the commit message
hostname: "viv-pc"
# more details at https://github.com/zokugun/vscode-sync-settings/blob/master/docs/hostname.md

# selected profile, required
profile: cool-profile-name

repository:
  type: git
  url: git@github.com:vivlim/vscode-settings.git
  branch: main
# how to personalize the commit messages at https://github.com/zokugun/vscode-sync-settings/blob/master/docs/commit-messages.md
```

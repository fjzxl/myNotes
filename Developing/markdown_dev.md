# Markdown配置

## vscode插件

Markdown Preview Enhanced \
Markdown All in One \
Markdownlint \
Local history \
Paste Image

## 配置

```json
{
    "markdown.copyFiles.destination": {
        "*.md": "Source/pics/${relativeFileDirname}/${documentBaseName}-${fileName}"
    },
    "[markdown]": {
        "editor.defaultFormatter": "DavidAnson.vscode-markdownlint"
    },
   
    "markdown-preview-enhanced.codeBlockTheme": "github-dark.css",
    "markdown-preview-enhanced.previewTheme": "one-dark.css",
    "markdown-preview-enhanced.automaticallyShowPreviewOfMarkdownBeingEdited": true,
    "markdown-preview-enhanced.imageFolderPath": "Source/pics",
    "markdownlint.run": "onType",
}
```
